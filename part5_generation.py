import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from models.part5_model import Part5Question
from prompts.part5_prompt import build_part5_prompt, get_fewshot_examples

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


def generate_part5_questions(
    num: int, diff: str, cat: str, sub: str
) -> list[Part5Question]:
    client = genai.Client(api_key=API_KEY)

    sys_prompt = build_part5_prompt(num, diff, cat, sub)
    fewshots = get_fewshot_examples(sub)

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
