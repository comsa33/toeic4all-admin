import asyncio
import time
import uuid
from typing import List, Optional, Tuple

from app.db.redis_lock import RedisClient
from app.utils.data_loader import DocumentSession
from app.utils.generation_helpers.genai_generator import (
    generate_part5_questions,
    generate_part6_sets,
    generate_part7_sets,
)
from app.utils.logger import logger
from app.utils.models.part5_question import Part5Question
from app.utils.models.part6_question import Part6Set
from app.utils.models.part7_question import Part7Set

# 데이터베이스 컬렉션 이름 상수
PART5_COLLECTION = "part5_questions"
PART6_COLLECTION = "part6_sets"
PART7_COLLECTION = "part7_sets"


class QuestionService:
    """
    문제 생성 및 데이터베이스 저장을 관리하는 서비스 클래스
    Redis를 이용한 분산 작업 관리 버전
    """

    async def _get_redis(self):
        """Redis 클라이언트 가져오기"""
        return await RedisClient.get_instance()

    async def _check_task_exists(self, task_id: str) -> bool:
        """작업 ID가 이미 존재하는지 확인"""
        redis = await self._get_redis()
        return bool(await redis.exists(f"qs:task:{task_id}"))

    async def _register_task(self, task_id: str, metadata: dict, ttl: int = 3600):
        """작업 등록 (TTL 설정)"""
        redis = await self._get_redis()
        await redis.set(f"qs:task:{task_id}", str(metadata), ex=ttl)
        await redis.sadd("qs:active_tasks", task_id)
        logger.info(f"QS Task {task_id} registered with TTL {ttl}s")

    async def _unregister_task(self, task_id: str):
        """작업 등록 해제"""
        redis = await self._get_redis()
        await redis.delete(f"qs:task:{task_id}")
        await redis.srem("qs:active_tasks", task_id)
        logger.info(f"QS Task {task_id} unregistered")

    async def _get_active_tasks(self):
        """활성 작업 목록 조회"""
        redis = await self._get_redis()
        task_ids = await redis.smembers("qs:active_tasks")
        tasks = []
        for task_id in task_ids:
            task_data = await redis.get(f"qs:task:{task_id}")
            if task_data:
                try:
                    tasks.append({"id": task_id, "metadata": task_data})
                except Exception:
                    tasks.append({"id": task_id, "metadata": str(task_data)})
        return tasks

    async def generate_part5_questions(
        self, num: int, difficulty: str, category: str, subcategory: str
    ) -> List[Part5Question]:
        """
        Part 5 문법/어휘 문제를 병렬로 생성합니다.
        """
        task_id = (
            f"qs:part5_{category}_{subcategory}_{difficulty}_{num}_{int(time.time())}"
        )

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            logger.info(f"Skipping duplicate task in QuestionService: {task_id}")
            return []

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part5_generation",
                    "category": category,
                    "subcategory": subcategory,
                    "difficulty": difficulty,
                    "num": num,
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            logger.info(
                f"Generating Part 5 questions: {category}/{subcategory}, {difficulty}, count={num}"
            )

            # 분할 처리를 위한 배치 크기 설정 (요청된 문제 수가 많을 경우 나눠서 처리)
            batch_size = 5
            batches = [batch_size for _ in range(num // batch_size)]

            if num % batch_size:
                batches.append(num % batch_size)

            # 각 배치를 비동기 병렬로 처리
            async def process_batch(batch_num):
                batch_task_id = f"{task_id}_batch_{batch_num}"
                # 중복 배치 작업 확인
                if await self._check_task_exists(batch_task_id):
                    logger.info(f"Skipping duplicate batch task: {batch_task_id}")
                    return []

                try:
                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part5_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    # 배치 생성 실행
                    result = generate_part5_questions(
                        batch_num, difficulty, category, subcategory
                    )

                    # 작업 완료 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part5_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "result_count": len(result) if result else 0,
                        },
                    )

                    return result
                except Exception as e:
                    logger.error(f"Error in batch generation: {str(e)}")
                    # 오류 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part5_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "status": "error",
                            "error": str(e),
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return []

            # 모든 배치를 병렬 처리 (타임아웃 설정)
            batch_results = await asyncio.gather(
                *[process_batch(batch_num) for batch_num in batches],
                return_exceptions=False,
            )

            # 결과 합치기
            questions = []
            for batch in batch_results:
                if isinstance(batch, list):
                    questions.extend(batch)

            # 작업 완료 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part5_generation",
                    "category": category,
                    "subcategory": subcategory,
                    "difficulty": difficulty,
                    "num": num,
                    "started_at": time.time(),
                    "completed_at": time.time(),
                    "status": "completed",
                    "question_count": len(questions),
                },
            )

            logger.info(f"Generated {len(questions)} Part 5 questions in parallel")
            return questions
        except Exception as e:
            logger.error(f"Error generating Part 5 questions: {str(e)}")
            # 오류 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part5_generation",
                    "category": category,
                    "subcategory": subcategory,
                    "difficulty": difficulty,
                    "num": num,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return []

    # 다른 메서드들도 비슷한 방식으로 개선 (store_part5_questions, generate_part6_questions 등)
    # 여기서는 store_part5_questions 개선 예시를 보여드립니다

    async def store_part5_questions(
        self, questions: List[Part5Question]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 5 문제를 병렬로 데이터베이스에 저장합니다.
        """
        task_id = f"qs:store_part5_{uuid.uuid4()}"

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            return False, "Similar task already in progress"

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part5_store",
                    "question_count": len(questions),
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            # 배치 크기 설정 (대량 데이터 처리시 최적화)
            batch_size = 50
            total_questions = len(questions)

            if total_questions <= batch_size:
                # 적은 수의 문제는 단일 세션으로 저장
                async with DocumentSession(PART5_COLLECTION) as session:
                    docs = [q.model_dump(mode="json") for q in questions]
                    result = await session.insert_many(docs)

                    if result:
                        # 작업 완료 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part5_store",
                                "question_count": len(questions),
                                "started_at": time.time(),
                                "completed_at": time.time(),
                                "status": "completed",
                            },
                        )
                        logger.info(
                            f"Stored {len(questions)} Part 5 questions in database"
                        )
                        return True, None
                    else:
                        # 실패 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part5_store",
                                "question_count": len(questions),
                                "status": "failed",
                                "error": "Failed to insert questions",
                            },
                            ttl=7200,  # 2시간 TTL (실패 기록 유지)
                        )
                        return False, "Failed to insert questions"
            else:
                # 대량의 문제는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_questions, batch_size):
                    end = min(i + batch_size, total_questions)
                    batches.append(questions[i:end])

                async def store_batch(batch, batch_index):
                    batch_task_id = f"{task_id}_batch_{batch_index}"

                    # 이미 처리된 배치인지 확인
                    if await self._check_task_exists(batch_task_id):
                        logger.info(
                            f"Skipping duplicate batch store task: {batch_task_id}"
                        )
                        return True

                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part5_store_batch",
                            "parent_task_id": task_id,
                            "batch_index": batch_index,
                            "batch_size": len(batch),
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    try:
                        # 배치 저장 실행
                        async with DocumentSession(PART5_COLLECTION) as session:
                            docs = [q.model_dump(mode="json") for q in batch]
                            result = await session.insert_many(docs)

                            # 작업 완료 상태 업데이트
                            if result:
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part5_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "batch_size": len(batch),
                                        "started_at": time.time(),
                                        "completed_at": time.time(),
                                        "status": "completed",
                                    },
                                )
                                return True
                            else:
                                # 실패 상태 업데이트
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part5_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "status": "failed",
                                    },
                                    ttl=7200,  # 2시간 TTL (실패 기록 유지)
                                )
                                return False
                    except Exception as e:
                        # 오류 상태 업데이트
                        logger.error(f"Error in batch store: {str(e)}")
                        await self._register_task(
                            batch_task_id,
                            {
                                "type": "qs:part5_store_batch",
                                "parent_task_id": task_id,
                                "batch_index": batch_index,
                                "status": "error",
                                "error": str(e),
                            },
                            ttl=7200,  # 2시간 TTL (오류 기록 유지)
                        )
                        return False

                # 병렬 저장 실행 (타임아웃 30초 설정)
                try:
                    results = await asyncio.wait_for(
                        asyncio.gather(
                            *[store_batch(batch, i) for i, batch in enumerate(batches)],
                            return_exceptions=True,
                        ),
                        timeout=30.0,  # 30초 타임아웃
                    )
                except asyncio.TimeoutError:
                    # 타임아웃 발생
                    logger.warning(f"Timeout while storing batches for task {task_id}")
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part5_store",
                            "question_count": len(questions),
                            "status": "timeout",
                            "error": "Operation timed out",
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return False, "Operation timed out"

                # 결과 확인
                success_count = sum(
                    1 for r in results if r is True and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    # 전체 작업 완료 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part5_store",
                            "question_count": len(questions),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.info(
                        f"Successfully stored all {total_questions} Part 5 questions in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    # 부분 성공 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part5_store",
                            "question_count": len(questions),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "partial_success",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.warning(
                        f"Partially stored Part 5 questions: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    # 전체 실패 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part5_store",
                            "question_count": len(questions),
                            "status": "failed",
                            "error": "Failed to insert any questions",
                        },
                        ttl=7200,  # 2시간 TTL (실패 기록 유지)
                    )
                    return False, "Failed to insert any questions"
        except Exception as e:
            # 예외 발생 시 상태 업데이트
            logger.error(f"Error storing Part 5 questions: {str(e)}")
            await self._register_task(
                task_id,
                {
                    "type": "qs:part5_store",
                    "question_count": len(questions) if questions else 0,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return False, str(e)

    async def generate_part6_questions(
        self, num_sets: int, difficulty: str, passage_type: str
    ) -> List[Part6Set]:
        """
        Part 6 문맥 이해 문제 세트를 병렬로 생성합니다.
        Redis 기반 작업 관리 적용
        """
        task_id = f"qs:part6_{passage_type}_{difficulty}_{num_sets}_{int(time.time())}"

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            logger.info(f"Skipping duplicate task in QuestionService: {task_id}")
            return []

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part6_generation",
                    "passage_type": passage_type,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            logger.info(
                f"Generating Part 6 sets: {passage_type}, {difficulty}, count={num_sets}"
            )

            # 배치 크기 (LLM API 최적화를 위해 적절히 설정)
            batch_size = min(
                3, num_sets
            )  # Part 6 세트는 복잡해서 배치 크기를 작게 설정
            batches = [batch_size for _ in range(num_sets // batch_size)]

            if num_sets % batch_size:
                batches.append(num_sets % batch_size)

            async def process_batch(batch_num):
                batch_task_id = f"{task_id}_batch_{batch_num}"
                # 중복 배치 작업 확인
                if await self._check_task_exists(batch_task_id):
                    logger.info(f"Skipping duplicate batch task: {batch_task_id}")
                    return []

                try:
                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part6_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    # 배치 생성 실행
                    result = generate_part6_sets(batch_num, difficulty, passage_type)

                    # 작업 완료 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part6_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "result_count": len(result) if result else 0,
                        },
                    )

                    return result
                except Exception as e:
                    logger.error(f"Error in Part 6 batch generation: {str(e)}")
                    # 오류 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part6_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "status": "error",
                            "error": str(e),
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return []

            # 병렬 처리 (타임아웃 설정 - 최대 60초)
            try:
                batch_results = await asyncio.wait_for(
                    asyncio.gather(
                        *[process_batch(batch_num) for batch_num in batches],
                        return_exceptions=False,
                    ),
                    timeout=60.0,
                )
            except asyncio.TimeoutError:
                logger.error(
                    f"Timeout during Part 6 batch generation for task {task_id}"
                )
                await self._register_task(
                    task_id,
                    {
                        "type": "qs:part6_generation",
                        "passage_type": passage_type,
                        "difficulty": difficulty,
                        "num_sets": num_sets,
                        "status": "timeout",
                        "error": "Batch generation timed out",
                    },
                    ttl=7200,  # 2시간 TTL (오류 기록 유지)
                )
                return []

            # 결과 합치기
            sets = []
            for batch in batch_results:
                if isinstance(batch, list):
                    sets.extend(batch)

            # 작업 완료 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part6_generation",
                    "passage_type": passage_type,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "started_at": time.time(),
                    "completed_at": time.time(),
                    "status": "completed",
                    "sets_count": len(sets),
                },
            )

            logger.info(f"Generated {len(sets)} Part 6 question sets in parallel")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 6 question sets: {str(e)}")
            # 오류 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part6_generation",
                    "passage_type": passage_type,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return []

    async def store_part6_questions(
        self, sets: List[Part6Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 6 문제 세트를 병렬로 데이터베이스에 저장합니다.
        Redis 기반 작업 관리 적용
        """
        task_id = f"qs:store_part6_{uuid.uuid4()}"

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            return False, "Similar task already in progress"

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part6_store",
                    "sets_count": len(sets),
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            # 배치 크기 설정
            batch_size = 30  # Part 6은 문서 크기가 더 크므로 배치 크기 조정
            total_sets = len(sets)

            if total_sets <= batch_size:
                # 적은 수의 세트는 단일 세션으로 저장
                async with DocumentSession(PART6_COLLECTION) as session:
                    docs = [s.model_dump(mode="json") for s in sets]
                    result = await session.insert_many(docs)

                    if result:
                        # 작업 완료 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part6_store",
                                "sets_count": len(sets),
                                "started_at": time.time(),
                                "completed_at": time.time(),
                                "status": "completed",
                            },
                        )
                        logger.info(
                            f"Stored {len(sets)} Part 6 question sets in database"
                        )
                        return True, None
                    else:
                        # 실패 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part6_store",
                                "sets_count": len(sets),
                                "status": "failed",
                                "error": "Failed to insert sets",
                            },
                            ttl=7200,  # 2시간 TTL (실패 기록 유지)
                        )
                        return False, "Failed to insert sets"
            else:
                # 대량의 세트는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_sets, batch_size):
                    end = min(i + batch_size, total_sets)
                    batches.append(sets[i:end])

                async def store_batch(batch, batch_index):
                    batch_task_id = f"{task_id}_batch_{batch_index}"

                    # 이미 처리된 배치인지 확인
                    if await self._check_task_exists(batch_task_id):
                        logger.info(
                            f"Skipping duplicate batch store task: {batch_task_id}"
                        )
                        return True

                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part6_store_batch",
                            "parent_task_id": task_id,
                            "batch_index": batch_index,
                            "batch_size": len(batch),
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    try:
                        # 배치 저장 실행
                        async with DocumentSession(PART6_COLLECTION) as session:
                            docs = [s.model_dump(mode="json") for s in batch]
                            result = await session.insert_many(docs)

                            # 작업 완료 상태 업데이트
                            if result:
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part6_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "batch_size": len(batch),
                                        "started_at": time.time(),
                                        "completed_at": time.time(),
                                        "status": "completed",
                                    },
                                )
                                return True
                            else:
                                # 실패 상태 업데이트
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part6_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "status": "failed",
                                    },
                                    ttl=7200,  # 2시간 TTL (실패 기록 유지)
                                )
                                return False
                    except Exception as e:
                        # 오류 상태 업데이트
                        logger.error(f"Error in batch store: {str(e)}")
                        await self._register_task(
                            batch_task_id,
                            {
                                "type": "qs:part6_store_batch",
                                "parent_task_id": task_id,
                                "batch_index": batch_index,
                                "status": "error",
                                "error": str(e),
                            },
                            ttl=7200,  # 2시간 TTL (오류 기록 유지)
                        )
                        return False

                # 병렬 저장 실행 (타임아웃 30초 설정)
                try:
                    results = await asyncio.wait_for(
                        asyncio.gather(
                            *[store_batch(batch, i) for i, batch in enumerate(batches)],
                            return_exceptions=True,
                        ),
                        timeout=30.0,  # 30초 타임아웃
                    )
                except asyncio.TimeoutError:
                    # 타임아웃 발생
                    logger.warning(
                        f"Timeout while storing Part 6 batches for task {task_id}"
                    )
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part6_store",
                            "sets_count": len(sets),
                            "status": "timeout",
                            "error": "Operation timed out",
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return False, "Operation timed out"

                # 결과 확인
                success_count = sum(
                    1 for r in results if r is True and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    # 전체 작업 완료 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part6_store",
                            "sets_count": len(sets),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.info(
                        f"Successfully stored all {total_sets} Part 6 sets in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    # 부분 성공 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part6_store",
                            "sets_count": len(sets),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "partial_success",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.warning(
                        f"Partially stored Part 6 sets: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    # 전체 실패 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part6_store",
                            "sets_count": len(sets),
                            "status": "failed",
                            "error": "Failed to insert any sets",
                        },
                        ttl=7200,  # 2시간 TTL (실패 기록 유지)
                    )
                    return False, "Failed to insert any sets"
        except Exception as e:
            # 예외 발생 시 상태 업데이트
            logger.error(f"Error storing Part 6 question sets: {str(e)}")
            await self._register_task(
                task_id,
                {
                    "type": "qs:part6_store",
                    "sets_count": len(sets) if sets else 0,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return False, str(e)

    async def generate_part7_questions(
        self, num_sets: int, difficulty: str, set_type: str, passage_types: List[str]
    ) -> List[Part7Set]:
        """
        Part 7 지문 이해 문제 세트를 병렬로 생성합니다.
        Redis 기반 작업 관리 적용
        """
        task_id = f"qs:part7_{set_type}_{'_'.join(passage_types)}_{difficulty}_{num_sets}_{int(time.time())}"

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            logger.info(f"Skipping duplicate task in QuestionService: {task_id}")
            return []

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part7_generation",
                    "set_type": set_type,
                    "passage_types": passage_types,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            logger.info(
                f"Generating Part 7 {set_type} sets: {passage_types}, {difficulty}, count={num_sets}"
            )

            # Part 7은 더 복잡하므로 배치 크기를 더 작게 설정
            batch_size = min(2, num_sets)
            batches = [batch_size for _ in range(num_sets // batch_size)]

            if num_sets % batch_size:
                batches.append(num_sets % batch_size)

            async def process_batch(batch_num):
                batch_task_id = f"{task_id}_batch_{batch_num}"
                # 중복 배치 작업 확인
                if await self._check_task_exists(batch_task_id):
                    logger.info(f"Skipping duplicate batch task: {batch_task_id}")
                    return []

                try:
                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part7_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    # 배치 생성 실행
                    result = generate_part7_sets(
                        batch_num, difficulty, set_type, passage_types
                    )

                    # 작업 완료 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part7_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "result_count": len(result) if result else 0,
                        },
                    )

                    return result
                except Exception as e:
                    logger.error(f"Error in Part 7 batch generation: {str(e)}")
                    # 오류 상태 업데이트
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part7_batch",
                            "parent_task_id": task_id,
                            "batch_size": batch_num,
                            "status": "error",
                            "error": str(e),
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return []

            # 병렬 처리 (타임아웃 설정 - 최대 120초, Part 7은 생성에 더 오래 걸림)
            try:
                batch_results = await asyncio.wait_for(
                    asyncio.gather(
                        *[process_batch(batch_num) for batch_num in batches],
                        return_exceptions=False,
                    ),
                    timeout=120.0,
                )
            except asyncio.TimeoutError:
                logger.error(
                    f"Timeout during Part 7 batch generation for task {task_id}"
                )
                await self._register_task(
                    task_id,
                    {
                        "type": "qs:part7_generation",
                        "set_type": set_type,
                        "passage_types": passage_types,
                        "difficulty": difficulty,
                        "num_sets": num_sets,
                        "status": "timeout",
                        "error": "Batch generation timed out",
                    },
                    ttl=7200,  # 2시간 TTL (오류 기록 유지)
                )
                return []

            # 결과 합치기
            sets = []
            for batch in batch_results:
                if isinstance(batch, list):
                    sets.extend(batch)

            # 작업 완료 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part7_generation",
                    "set_type": set_type,
                    "passage_types": passage_types,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "started_at": time.time(),
                    "completed_at": time.time(),
                    "status": "completed",
                    "sets_count": len(sets),
                },
            )

            logger.info(
                f"Generated {len(sets)} Part 7 {set_type} question sets in parallel"
            )
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 7 question sets: {str(e)}")
            # 오류 상태 업데이트
            await self._register_task(
                task_id,
                {
                    "type": "qs:part7_generation",
                    "set_type": set_type,
                    "passage_types": passage_types,
                    "difficulty": difficulty,
                    "num_sets": num_sets,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return []

    async def store_part7_questions(
        self, sets: List[Part7Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 7 문제 세트를 병렬로 데이터베이스에 저장합니다.
        Redis 기반 작업 관리 적용
        """
        task_id = f"qs:store_part7_{uuid.uuid4()}"

        # 중복 작업 확인
        if await self._check_task_exists(task_id):
            return False, "Similar task already in progress"

        try:
            # 작업 등록
            await self._register_task(
                task_id,
                {
                    "type": "qs:part7_store",
                    "sets_count": len(sets),
                    "started_at": time.time(),
                    "status": "in_progress",
                },
            )

            # 배치 크기 설정
            batch_size = 20  # Part 7은 문서 크기가 더 크므로 배치 크기 더 작게 조정
            total_sets = len(sets)

            if total_sets <= batch_size:
                # 적은 수의 세트는 단일 세션으로 저장
                async with DocumentSession(PART7_COLLECTION) as session:
                    docs = [s.model_dump(mode="json") for s in sets]
                    result = await session.insert_many(docs)

                    if result:
                        # 작업 완료 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part7_store",
                                "sets_count": len(sets),
                                "started_at": time.time(),
                                "completed_at": time.time(),
                                "status": "completed",
                            },
                        )
                        logger.info(
                            f"Stored {len(sets)} Part 7 question sets in database"
                        )
                        return True, None
                    else:
                        # 실패 상태 업데이트
                        await self._register_task(
                            task_id,
                            {
                                "type": "qs:part7_store",
                                "sets_count": len(sets),
                                "status": "failed",
                                "error": "Failed to insert sets",
                            },
                            ttl=7200,  # 2시간 TTL (실패 기록 유지)
                        )
                        return False, "Failed to insert sets"
            else:
                # 대량의 세트는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_sets, batch_size):
                    end = min(i + batch_size, total_sets)
                    batches.append(sets[i:end])

                async def store_batch(batch, batch_index):
                    batch_task_id = f"{task_id}_batch_{batch_index}"

                    # 이미 처리된 배치인지 확인
                    if await self._check_task_exists(batch_task_id):
                        logger.info(
                            f"Skipping duplicate batch store task: {batch_task_id}"
                        )
                        return True

                    # 배치 작업 등록
                    await self._register_task(
                        batch_task_id,
                        {
                            "type": "qs:part7_store_batch",
                            "parent_task_id": task_id,
                            "batch_index": batch_index,
                            "batch_size": len(batch),
                            "started_at": time.time(),
                            "status": "in_progress",
                        },
                    )

                    try:
                        # 배치 저장 실행
                        async with DocumentSession(PART7_COLLECTION) as session:
                            docs = [s.model_dump(mode="json") for s in batch]
                            result = await session.insert_many(docs)

                            # 작업 완료 상태 업데이트
                            if result:
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part7_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "batch_size": len(batch),
                                        "started_at": time.time(),
                                        "completed_at": time.time(),
                                        "status": "completed",
                                    },
                                )
                                return True
                            else:
                                # 실패 상태 업데이트
                                await self._register_task(
                                    batch_task_id,
                                    {
                                        "type": "qs:part7_store_batch",
                                        "parent_task_id": task_id,
                                        "batch_index": batch_index,
                                        "status": "failed",
                                    },
                                    ttl=7200,  # 2시간 TTL (실패 기록 유지)
                                )
                                return False
                    except Exception as e:
                        # 오류 상태 업데이트
                        logger.error(f"Error in batch store: {str(e)}")
                        await self._register_task(
                            batch_task_id,
                            {
                                "type": "qs:part7_store_batch",
                                "parent_task_id": task_id,
                                "batch_index": batch_index,
                                "status": "error",
                                "error": str(e),
                            },
                            ttl=7200,  # 2시간 TTL (오류 기록 유지)
                        )
                        return False

                # 병렬 저장 실행 (타임아웃 30초 설정)
                try:
                    results = await asyncio.wait_for(
                        asyncio.gather(
                            *[store_batch(batch, i) for i, batch in enumerate(batches)],
                            return_exceptions=True,
                        ),
                        timeout=30.0,  # 30초 타임아웃
                    )
                except asyncio.TimeoutError:
                    # 타임아웃 발생
                    logger.warning(
                        f"Timeout while storing Part 7 batches for task {task_id}"
                    )
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part7_store",
                            "sets_count": len(sets),
                            "status": "timeout",
                            "error": "Operation timed out",
                        },
                        ttl=7200,  # 2시간 TTL (오류 기록 유지)
                    )
                    return False, "Operation timed out"

                # 결과 확인
                success_count = sum(
                    1 for r in results if r is True and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    # 전체 작업 완료 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part7_store",
                            "sets_count": len(sets),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "completed",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.info(
                        f"Successfully stored all {total_sets} Part 7 sets in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    # 부분 성공 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part7_store",
                            "sets_count": len(sets),
                            "started_at": time.time(),
                            "completed_at": time.time(),
                            "status": "partial_success",
                            "batches_total": len(batches),
                            "batches_success": success_count,
                        },
                    )
                    logger.warning(
                        f"Partially stored Part 7 sets: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    # 전체 실패 상태 업데이트
                    await self._register_task(
                        task_id,
                        {
                            "type": "qs:part7_store",
                            "sets_count": len(sets),
                            "status": "failed",
                            "error": "Failed to insert any sets",
                        },
                        ttl=7200,  # 2시간 TTL (실패 기록 유지)
                    )
                    return False, "Failed to insert any sets"
        except Exception as e:
            # 예외 발생 시 상태 업데이트
            logger.error(f"Error storing Part 7 question sets: {str(e)}")
            await self._register_task(
                task_id,
                {
                    "type": "qs:part7_store",
                    "sets_count": len(sets) if sets else 0,
                    "status": "error",
                    "error": str(e),
                },
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
            return False, str(e)
