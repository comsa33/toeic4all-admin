from typing import List

from app.utils.data_loader import insert_questions
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

    async def generate_part5_questions(
        self, num: int, difficulty: str, category: str, subcategory: str
    ) -> List[Part5Question]:
        """
        Part 5 문법/어휘 문제를 생성합니다.
        """
        try:
            questions = generate_part5_questions(num, difficulty, category, subcategory)
            if not isinstance(questions, list):
                raise ValueError("Generated questions are not in the expected format")
            logger.info(f"Generated {len(questions)} Part 5 questions")
            return questions
        except Exception as e:
            logger.error(f"Error generating Part 5 questions: {str(e)}")
            return []

    async def generate_part6_questions(
        self, num_sets: int, difficulty: str, passage_type: str
    ) -> List[Part6Set]:
        """
        Part 6 문맥 이해 문제 세트를 생성합니다.
        """
        try:
            sets = generate_part6_sets(num_sets, difficulty, passage_type)
            if not isinstance(sets, list):
                raise ValueError("Generated sets are not in the expected format")
            logger.info(f"Generated {len(sets)} Part 6 question sets")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 6 question sets: {str(e)}")
            return []

    async def generate_part7_questions(
        self, num_sets: int, difficulty: str, set_type: str, passage_types: List[str]
    ) -> List[Part7Set]:
        """
        Part 7 지문 이해 문제 세트를 생성합니다.
        """
        try:
            sets = generate_part7_sets(num_sets, difficulty, set_type, passage_types)
            if not isinstance(sets, list):
                raise ValueError("Generated sets are not in the expected format")
            logger.info(f"Generated {len(sets)} Part 7 {set_type} question sets")
            return sets
        except Exception as e:
            logger.error(f"Error generating Part 7 question sets: {str(e)}")
            return []

    async def store_part5_questions(self, questions: List[Part5Question]) -> None:
        """
        Part 5 문제를 데이터베이스에 저장합니다.
        """
        try:
            await insert_questions(questions, PART5_COLLECTION)
            logger.info(f"Stored {len(questions)} Part 5 questions in database")
        except Exception as e:
            logger.error(f"Error storing Part 5 questions: {str(e)}")

    async def store_part6_questions(self, sets: List[Part6Set]) -> None:
        """
        Part 6 문제 세트를 데이터베이스에 저장합니다.
        """
        try:
            await insert_questions(sets, PART6_COLLECTION)
            logger.info(f"Stored {len(sets)} Part 6 question sets in database")
        except Exception as e:
            logger.error(f"Error storing Part 6 question sets: {str(e)}")

    async def store_part7_questions(self, sets: List[Part7Set]) -> None:
        """
        Part 7 문제 세트를 데이터베이스에 저장합니다.
        """
        try:
            await insert_questions(sets, PART7_COLLECTION)
            logger.info(f"Stored {len(sets)} Part 7 question sets in database")
        except Exception as e:
            logger.error(f"Error storing Part 7 question sets: {str(e)}")
