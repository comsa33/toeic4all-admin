from enum import Enum
from typing import Any

from google import genai
from google.genai import types
from pydantic import BaseModel

from app.config import settings
from app.utils.models.part5_question import Part5Question
from app.utils.models.part6_question import Part6Set
from app.utils.models.part7_question import Part7Set
from app.utils.prompts.part5 import build_part5_prompt
from app.utils.prompts.part5 import get_fewshot_examples as part5_get_fewshot_examples
from app.utils.prompts.part6 import build_part6_prompt
from app.utils.prompts.part6 import get_fewshot_examples as part6_get_fewshot_examples
from app.utils.prompts.part7 import build_part7_prompt
from app.utils.prompts.part7 import get_fewshot_examples as part7_get_fewshot_examples

API_KEY = settings.gemini_api_key


def generate_part5_questions(
    num: int, difficulty: str, category: str, subcategory: str
) -> list[Part5Question] | BaseModel | dict[Any, Any] | Enum | None:
    """
    Gemini API를 통해 Part5 문제를 생성합니다.
    :param num: 생성할 문제 수 (1~10)
    :param difficulty: 난이도 (Easy, Medium, Hard)
    :param category: 카테고리 (e.g., "문법", "어휘")
    :param subcategory: 서브 카테고리 (e.g., "시제", "전치사")
    :return: List[Part5Question]
    """
    client = genai.Client(api_key=API_KEY)

    sys_prompt = build_part5_prompt(num, difficulty, category, subcategory)
    fewshots = part5_get_fewshot_examples(subcategory)

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        config=types.GenerateContentConfig(
            system_instruction=sys_prompt,
            response_mime_type="application/json",
            response_schema=list[Part5Question],
        ),
        contents=fewshots,
    )
    return response.parsed


def generate_part6_sets(
    num_sets: int, difficulty: str, passage_type: str
) -> list[Part6Set] | BaseModel | dict[Any, Any] | Enum | None:
    """
    Gemini API를 통해 Part6 문제 세트를 생성합니다.
    :param num_sets: 생성할 문제 세트 수 (1~10)
    :param difficulty: 난이도 (Easy, Medium, Hard)
    :param passage_type: 지문 유형 (Email/Letter, Notice 등)
    :return: List[Part6Set]
    """
    client = genai.Client(api_key=API_KEY)

    sys_prompt = build_part6_prompt(num_sets, difficulty, passage_type)
    fewshots = part6_get_fewshot_examples(passage_type)

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        config=types.GenerateContentConfig(
            system_instruction=sys_prompt,
            response_mime_type="application/json",
            response_schema=list[Part6Set],
        ),
        contents=fewshots,
    )
    return response.parsed


def generate_part7_sets(
    num_sets: int, difficulty: str, set_type: str, passage_types: list[str]
) -> list[Part7Set] | BaseModel | dict[Any, Any] | Enum | None:
    """
    Gemini API를 통해 Part7 문제 세트를 생성합니다.
    :param num_sets: 생성할 문제 세트 수 (1~5)
    :param difficulty: 난이도 (Easy, Medium, Hard)
    :param set_type: 문제 세트 유형 (Single, Double, Triple)
    :param passage_types: 지문 유형 리스트 (e.g., ["Email"], ["Article", "Letter"])
    :return: List[Part7Set]
    """
    client = genai.Client(api_key=API_KEY)

    sys_prompt = build_part7_prompt(num_sets, difficulty, set_type, passage_types)
    fewshots = part7_get_fewshot_examples(set_type, passage_types)

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",  # 또는 "gemini-1.5-pro-preview-0409"
        config=types.GenerateContentConfig(
            system_instruction=sys_prompt,
            response_mime_type="application/json",
            response_schema=list[Part7Set],
        ),
        contents=fewshots,
    )
    return response.parsed
