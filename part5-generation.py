import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from models.part5_question import Part5Set
from prompts.part5 import build_part5_prompt, get_fewshot_examples

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


def generate_part5_questions(num: int, diff: str, cat: str, sub: str) -> list[Part5Set]:
    """
    Part 5 문제 세트를 생성하는 함수.
    """
    client = genai.Client(api_key=API_KEY)

    sys_prompt = build_part5_prompt(num, diff, cat, sub)
    fewshots = get_fewshot_examples(sub)

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-04-17",
        config=types.GenerateContentConfig(
            system_instruction=sys_prompt,
            response_mime_type="application/json",
            response_schema=list[Part5Set],
        ),
        contents=fewshots,
    )

    part5_sets: list[Part5Set] = response.parsed
    return part5_sets


if __name__ == "__main__":

    # ---- 사용자 파라미터 ------------------------------------
    NUM = 3
    DIFF = "Medium"
    CAT = "문법"
    SUB = "시제"
    # ---------------------------------------------------------

    part5_sets = generate_part5_questions(NUM, DIFF, CAT, SUB)
    print(part5_sets)
