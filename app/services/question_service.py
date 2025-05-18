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
        Part 5 문법/어휘 문제를 생성합니다.
        """
        # 문제 생성 메타데이터 생성
        task_id = (
            f"part5_{category}_{subcategory}_{difficulty}_{num}_{int(time.time())}"
        )

        # 중복 작업 체크 (선택적)
        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
            # 로깅
            logger.info(
                f"Generating Part 5 questions: {category}/{subcategory}, {difficulty}, count={num}"
            )

            questions = generate_part5_questions(num, difficulty, category, subcategory)
            if not isinstance(questions, list):
                raise ValueError("Generated questions are not in the expected format")

            logger.info(f"Generated {len(questions)} Part 5 questions")
            return questions
        except Exception as e:
            logger.error(f"Error generating Part 5 questions: {str(e)}")
            return []
        finally:
            # 작업 추적에서 제거 (중복 작업 체크 추가한 경우)
            await self._unregister_task(task_id)

    async def generate_part6_questions(
        self, num_sets: int, difficulty: str, passage_type: str
    ) -> List[Part6Set]:
        """
        Part 6 문맥 이해 문제 세트를 생성합니다.
        """
        # 작업 메타데이터 생성
        task_id = f"part6_{passage_type}_{difficulty}_{num_sets}_{int(time.time())}"

        # 중복 작업 체크
        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
            # 로깅
            logger.info(
                f"Generating Part 6 sets: {passage_type}, {difficulty}, count={num_sets}"
            )

            sets = generate_part6_sets(num_sets, difficulty, passage_type)
            if not isinstance(sets, list):
                raise ValueError("Generated sets are not in the expected format")

            logger.info(f"Generated {len(sets)} Part 6 question sets")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 6 question sets: {str(e)}")
            return []
        finally:
            # 작업 추적에서 제거
            await self._unregister_task(task_id)

    async def generate_part7_questions(
        self, num_sets: int, difficulty: str, set_type: str, passage_types: List[str]
    ) -> List[Part7Set]:
        """
        Part 7 지문 이해 문제 세트를 생성합니다.
        """
        # 작업 메타데이터 생성
        task_id = f"part7_{set_type}_{'_'.join(passage_types)}_{difficulty}_{num_sets}_{int(time.time())}"

        # 중복 작업 체크
        if not await self._register_task(task_id):
            logger.info(f"Skipping duplicate task: {task_id}")
            return []

        try:
            # 로깅
            logger.info(
                f"Generating Part 7 {set_type} sets: {passage_types}, {difficulty}, count={num_sets}"
            )

            sets = generate_part7_sets(num_sets, difficulty, set_type, passage_types)
            if not isinstance(sets, list):
                raise ValueError("Generated sets are not in the expected format")

            logger.info(f"Generated {len(sets)} Part 7 {set_type} question sets")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 7 question sets: {str(e)}")
            return []
        finally:
            # 작업 추적에서 제거
            await self._unregister_task(task_id)

    async def store_part5_questions(
        self, questions: List[Part5Question]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 5 문제를 데이터베이스에 저장합니다.

        Returns:
            Tuple[bool, Optional[str]]: (성공 여부, 오류 메시지)
        """
        # 작업 ID 생성
        task_id = f"store_part5_{uuid.uuid4()}"

        # 이미 진행 중인 작업인지 확인
        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            # DocumentSession을 사용하여 DB 작업 처리
            async with DocumentSession(PART5_COLLECTION) as session:
                docs = [q.model_dump(mode="json") for q in questions]
                result = await session.insert_many(docs)

                if result:
                    logger.info(f"Stored {len(questions)} Part 5 questions in database")
                    return True, None
                else:
                    return False, "Failed to insert questions"
        except Exception as e:
            logger.error(f"Error storing Part 5 questions: {str(e)}")
            return False, str(e)
        finally:
            # 작업 추적에서 제거
            await self._unregister_task(task_id)

    async def store_part6_questions(
        self, sets: List[Part6Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 6 문제 세트를 데이터베이스에 저장합니다.

        Returns:
            Tuple[bool, Optional[str]]: (성공 여부, 오류 메시지)
        """
        task_id = f"store_part6_{uuid.uuid4()}"

        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            async with DocumentSession(PART6_COLLECTION) as session:
                docs = [s.model_dump(mode="json") for s in sets]
                result = await session.insert_many(docs)

                if result:
                    logger.info(f"Stored {len(sets)} Part 6 question sets in database")
                    return True, None
                else:
                    return False, "Failed to insert sets"
        except Exception as e:
            logger.error(f"Error storing Part 6 question sets: {str(e)}")
            return False, str(e)
        finally:
            await self._unregister_task(task_id)

    async def store_part7_questions(
        self, sets: List[Part7Set]
    ) -> Tuple[bool, Optional[str]]:
        """
        Part 7 문제 세트를 데이터베이스에 저장합니다.

        Returns:
            Tuple[bool, Optional[str]]: (성공 여부, 오류 메시지)
        """
        task_id = f"store_part7_{uuid.uuid4()}"

        if not await self._register_task(task_id):
            return False, "Similar task already in progress"

        try:
            async with DocumentSession(PART7_COLLECTION) as session:
                docs = [s.model_dump(mode="json") for s in sets]
                result = await session.insert_many(docs)

                if result:
                    logger.info(f"Stored {len(sets)} Part 7 question sets in database")
                    return True, None
                else:
                    return False, "Failed to insert sets"
        except Exception as e:
            logger.error(f"Error storing Part 7 question sets: {str(e)}")
            return False, str(e)
        finally:
            await self._unregister_task(task_id)
