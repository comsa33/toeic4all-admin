import asyncio
import time
import uuid
from typing import List, Optional, Set, Tuple

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
    """

    # 작업 추적용 클래스 속성
    _pending_tasks: Set[str] = set()
    _task_lock = asyncio.Lock()

    async def _register_task(self, task_id: str) -> bool:
        """작업 등록 (중복 방지)"""
        async with self._task_lock:
            if task_id in self._pending_tasks:
                return False
            self._pending_tasks.add(task_id)
            return True

    async def _unregister_task(self, task_id: str) -> None:
        """작업 등록 해제"""
        async with self._task_lock:
            self._pending_tasks.discard(task_id)

    async def generate_part5_questions(
        self, num: int, difficulty: str, category: str, subcategory: str
    ) -> List[Part5Question]:
        """
        Part 5 문법/어휘 문제를 병렬로 생성합니다.
        """
        task_id = (
            f"part5_{category}_{subcategory}_{difficulty}_{num}_{int(time.time())}"
        )

        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
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
                try:
                    return generate_part5_questions(
                        batch_num, difficulty, category, subcategory
                    )
                except Exception as e:
                    logger.error(f"Error in batch generation: {str(e)}")
                    return []

            # 모든 배치를 병렬 처리
            batch_results = await asyncio.gather(
                *[process_batch(batch_num) for batch_num in batches],
                return_exceptions=False,
            )

            # 결과 합치기
            questions = []
            for batch in batch_results:
                if isinstance(batch, list):
                    questions.extend(batch)

            logger.info(f"Generated {len(questions)} Part 5 questions in parallel")
            return questions
        except Exception as e:
            logger.error(f"Error generating Part 5 questions: {str(e)}")
            return []
        finally:
            await self._unregister_task(task_id)

    async def generate_part6_questions(
        self, num_sets: int, difficulty: str, passage_type: str
    ) -> List[Part6Set]:
        """
        Part 6 문맥 이해 문제 세트를 병렬로 생성합니다.
        """
        task_id = f"part6_{passage_type}_{difficulty}_{num_sets}_{int(time.time())}"

        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
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
                try:
                    return generate_part6_sets(batch_num, difficulty, passage_type)
                except Exception as e:
                    logger.error(f"Error in Part 6 batch generation: {str(e)}")
                    return []

            # 병렬 처리
            batch_results = await asyncio.gather(
                *[process_batch(batch_num) for batch_num in batches],
                return_exceptions=False,
            )

            # 결과 합치기
            sets = []
            for batch in batch_results:
                if isinstance(batch, list):
                    sets.extend(batch)

            logger.info(f"Generated {len(sets)} Part 6 question sets in parallel")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 6 question sets: {str(e)}")
            return []
        finally:
            await self._unregister_task(task_id)

    async def generate_part7_questions(
        self, num_sets: int, difficulty: str, set_type: str, passage_types: List[str]
    ) -> List[Part7Set]:
        """
        Part 7 지문 이해 문제 세트를 병렬로 생성합니다.
        """
        task_id = f"part7_{set_type}_{'_'.join(passage_types)}_{difficulty}_{num_sets}_{int(time.time())}"

        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
            logger.info(
                f"Generating Part 7 {set_type} sets: {passage_types}, {difficulty}, count={num_sets}"
            )

            # Part 7은 더 복잡하므로 배치 크기를 더 작게 설정
            batch_size = min(
                2, num_sets
            )  # Part 7은 더 복잡해서 배치 크기를 더 작게 설정
            batches = [batch_size for _ in range(num_sets // batch_size)]

            if num_sets % batch_size:
                batches.append(num_sets % batch_size)

            async def process_batch(batch_num):
                try:
                    return generate_part7_sets(
                        batch_num, difficulty, set_type, passage_types
                    )
                except Exception as e:
                    logger.error(f"Error in Part 7 batch generation: {str(e)}")
                    return []

            # 병렬 처리
            batch_results = await asyncio.gather(
                *[process_batch(batch_num) for batch_num in batches],
                return_exceptions=False,
            )

            # 결과 합치기
            sets = []
            for batch in batch_results:
                if isinstance(batch, list):
                    sets.extend(batch)

            logger.info(
                f"Generated {len(sets)} Part 7 {set_type} question sets in parallel"
            )
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 7 question sets: {str(e)}")
            return []
        finally:
            await self._unregister_task(task_id)

    async def store_part5_questions(
        self, questions: List[Part5Question]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 5 문제를 병렬로 데이터베이스에 저장합니다.
        """
        task_id = f"store_part5_{uuid.uuid4()}"

        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            # 배치 크기 설정 (대량 데이터 처리시 최적화)
            batch_size = 50
            total_questions = len(questions)

            if total_questions <= batch_size:
                # 적은 수의 문제는 단일 세션으로 저장
                async with DocumentSession(PART5_COLLECTION) as session:
                    docs = [q.model_dump(mode="json") for q in questions]
                    result = await session.insert_many(docs)

                    if result:
                        logger.info(
                            f"Stored {len(questions)} Part 5 questions in database"
                        )
                        return True, None
                    else:
                        return False, "Failed to insert questions"
            else:
                # 대량의 문제는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_questions, batch_size):
                    end = min(i + batch_size, total_questions)
                    batches.append(questions[i:end])

                async def store_batch(batch):
                    async with DocumentSession(PART5_COLLECTION) as session:
                        docs = [q.model_dump(mode="json") for q in batch]
                        return await session.insert_many(docs)

                # 병렬 저장 실행
                results = await asyncio.gather(
                    *[store_batch(batch) for batch in batches], return_exceptions=True
                )

                # 결과 확인
                success_count = sum(
                    1 for r in results if r and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    logger.info(
                        f"Successfully stored all {total_questions} Part 5 questions in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    logger.warning(
                        f"Partially stored Part 5 questions: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    return False, "Failed to insert any questions"
        except Exception as e:
            logger.error(f"Error storing Part 5 questions: {str(e)}")
            return False, str(e)
        finally:
            await self._unregister_task(task_id)

    async def store_part6_questions(
        self, sets: List[Part6Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 6 문제 세트를 병렬로 데이터베이스에 저장합니다.
        """
        task_id = f"store_part6_{uuid.uuid4()}"

        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            # 배치 크기 설정
            batch_size = 30  # Part 6은 문서 크기가 더 크므로 배치 크기 조정
            total_sets = len(sets)

            if total_sets <= batch_size:
                # 적은 수의 세트는 단일 세션으로 저장
                async with DocumentSession(PART6_COLLECTION) as session:
                    docs = [s.model_dump(mode="json") for s in sets]
                    result = await session.insert_many(docs)

                    if result:
                        logger.info(
                            f"Stored {len(sets)} Part 6 question sets in database"
                        )
                        return True, None
                    else:
                        return False, "Failed to insert sets"
            else:
                # 대량의 세트는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_sets, batch_size):
                    end = min(i + batch_size, total_sets)
                    batches.append(sets[i:end])

                async def store_batch(batch):
                    async with DocumentSession(PART6_COLLECTION) as session:
                        docs = [s.model_dump(mode="json") for s in batch]
                        return await session.insert_many(docs)

                # 병렬 저장 실행
                results = await asyncio.gather(
                    *[store_batch(batch) for batch in batches], return_exceptions=True
                )

                # 결과 확인
                success_count = sum(
                    1 for r in results if r and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    logger.info(
                        f"Successfully stored all {total_sets} Part 6 sets in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    logger.warning(
                        f"Partially stored Part 6 sets: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    return False, "Failed to insert any sets"
        except Exception as e:
            logger.error(f"Error storing Part 6 question sets: {str(e)}")
            return False, str(e)
        finally:
            await self._unregister_task(task_id)

    async def store_part7_questions(
        self, sets: List[Part7Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 7 문제 세트를 병렬로 데이터베이스에 저장합니다.
        """
        task_id = f"store_part7_{uuid.uuid4()}"

        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            # 배치 크기 설정
            batch_size = 20  # Part 7은 문서 크기가 더 크므로 배치 크기 더 작게 조정
            total_sets = len(sets)

            if total_sets <= batch_size:
                # 적은 수의 세트는 단일 세션으로 저장
                async with DocumentSession(PART7_COLLECTION) as session:
                    docs = [s.model_dump(mode="json") for s in sets]
                    result = await session.insert_many(docs)

                    if result:
                        logger.info(
                            f"Stored {len(sets)} Part 7 question sets in database"
                        )
                        return True, None
                    else:
                        return False, "Failed to insert sets"
            else:
                # 대량의 세트는 배치로 나누어 병렬 저장
                batches = []
                for i in range(0, total_sets, batch_size):
                    end = min(i + batch_size, total_sets)
                    batches.append(sets[i:end])

                async def store_batch(batch):
                    async with DocumentSession(PART7_COLLECTION) as session:
                        docs = [s.model_dump(mode="json") for s in batch]
                        return await session.insert_many(docs)

                # 병렬 저장 실행
                results = await asyncio.gather(
                    *[store_batch(batch) for batch in batches], return_exceptions=True
                )

                # 결과 확인
                success_count = sum(
                    1 for r in results if r and not isinstance(r, Exception)
                )

                if success_count == len(batches):
                    logger.info(
                        f"Successfully stored all {total_sets} Part 7 sets in {len(batches)} batches"
                    )
                    return True, None
                elif success_count > 0:
                    logger.warning(
                        f"Partially stored Part 7 sets: {success_count}/{len(batches)} batches successful"
                    )
                    return (
                        True,
                        f"Partially stored: {success_count}/{len(batches)} batches successful",
                    )
                else:
                    return False, "Failed to insert any sets"
        except Exception as e:
            logger.error(f"Error storing Part 7 question sets: {str(e)}")
            return False, str(e)
        finally:
            await self._unregister_task(task_id)
