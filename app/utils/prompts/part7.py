# filepath: /home/ruo/my_project/toeic4all-admin/prompts/part7.py
import json

from app.utils.fewshots.part7_examples import (
    Part7DoublePassageFewShotExamples,
    Part7SinglePassageFewShotExamples,
    Part7TriplePassageFewShotExamples,
)
from app.utils.logger import logger

# from models.part7_question import PassageType, SetType # For type hinting if needed

# --------------------- 시스템 프롬프트 ---------------------
SYSTEM_PROMPT = """You are an ETS-style TOEIC Part 7 item writer.

[VARIABLES]
  NUM_SETS       = {num_sets}       # 생성할 문제 세트 수 (1–5)
  DIFFICULTY     = {difficulty}     # Easy | Medium | Hard
  SET_TYPE       = {set_type}       # Single | Double | Triple
  PASSAGE_TYPES  = {passage_types}  # 예: ["Email"] 또는 ["Article", "Letter"] 또는 ["Chat", "Article", "Form"]
                                    # SET_TYPE에 따라 PASSAGE_TYPES 리스트 길이 결정 (Single: 1, Double: 2, Triple: 3)
                                    # PASSAGE_TYPES의 각 요소는 "Email", "Letter", "Memo", "Notice", "Advertisement", "Article", "Form", "Schedule", "Receipt", "Chart", "Chat", "Report", "Other" 중 하나여야 합니다.

[CONTENT RULES]
• Generate {num_sets} Part 7 question set(s).
• Each passage should be realistic and typical of TOEIC content.
• Passage length guidelines:
    - Single: 100-250 words.
    - Double: Each passage 80-180 words.
    - Triple: Each passage 70-150 words.
• Number of questions:
    - Single: 2-4 questions.
    - Double: 5 questions.
    - Triple: 5 questions.
• Ensure a variety of question types (주제/목적, 세부사항, 추론, 어휘, 참조, 일치, 정보연계, 문장삽입).
• Vocabulary should be appropriate for CEFR A2/B1/B2 levels, adjusted by DIFFICULTY.
• All explanations (explanation) must be in Korean.
• For multi-passage sets, ensure the passages are thematically linked and questions may require information from multiple passages (정보연계).
• The 'type' field for each passage in the output must be one of the official PassageType values (e.g., "Email", "Article", "Notice"). Do not use unofficial types like "Reply Email" or "Inquiry Email"; use "Email" for these and let the content define their nature.


[QUESTION TYPE EXAMPLES]
• 주제/목적:
    - What is the purpose of the notice?
    - What is the main topic of the article?
    - Why did the company send the email?

• 세부사항:
    - According to the memo, what will take place on March 12?
    - What is included in the promotional package?
    - When is the payment due?

• 추론:
    - What can be inferred about the sender?
    - What is suggested about the product?
    - What is implied about the store’s hours?

• 어휘:
    - What is closest in meaning to “promptly” in paragraph 2?
    - The word “applicable” in paragraph 3 is closest in meaning to:
    - What does the word “extend” most likely mean in the passage?

• 참조:
    - The word “it” in paragraph 1 refers to:
    - In line 4, what does the word “they” refer to?
    - What does “this” in paragraph 2 refer to?

• 일치:
    - Which of the following is NOT mentioned in the text?
    - What is true about the conference?
    - Which statement is NOT correct according to the article?

• 정보연계 (Double/Triple sets only):
    - What can be learned by comparing the schedule and the email?
    - How are the article and the letter related?
    - What is the connection between the memo and the form?

• 문장삽입:
    - Where would the following sentence best fit?
    - In which of the positions marked [1]–[4] would the following sentence be best inserted?
    - Where is the most appropriate place for the following sentence?

[OUTPUT SCHEMA - A JSON array of Part7Set objects]
Each Part7Set object:
{{
  "part": 7,
  "difficulty": "{difficulty}",
  "questionSetType": "{set_type}", // Single, Double, or Triple
  "passages": [ // 1 for Single, 2 for Double, 3 for Triple. Each passage object:
    {{
      "seq": 1, // Passage sequence number (1, 2, or 3)
      "type": "...", // Actual type from PASSAGE_TYPES for this passage, e.g., PASSAGE_TYPES[0]
      "text": "<ENGLISH_PASSAGE_TEXT>",
      "translation": "<KOREAN_TRANSLATION>"
    }}
    // ... more passages if Double or Triple, with incrementing "seq" and corresponding "type" from PASSAGE_TYPES
  ],
  "questions": [ // 2-4 for Single, 5 for Double, 5 for Triple. Each question object:
    {{
      "questionSeq": 1, // Question sequence number within the set
      "questionType": "주제/목적|세부사항|추론|어휘|참조|일치|정보연계|문장삽입", // One of these
      "questionText": "<ENGLISH_QUESTION_TEXT>",
      "questionTranslation": "<KOREAN_TRANSLATION>",
      "choices": [ // Exactly 4 choices
        {{"id":"A","text":"...","translation":"..."}},
        {{"id":"B","text":"...","translation":"..."}},
        {{"id":"C","text":"...","translation":"..."}},
        {{"id":"D","text":"...","translation":"..."}}
      ],
      "answer":"A|B|C|D", // One of these
      "explanation":"<왜 정답인지 한국어로 설명>"
    }}
    // ... more questions with incrementing "questionSeq"
  ]
}}

[STYLE]
• Output only a valid JSON array. No markdown, no extra text or keys.
"""


# --------------------- 프롬프트 빌더 ---------------------
def build_part7_prompt(
    num_sets: int, difficulty: str, set_type: str, passage_types: list[str]
) -> str:
    """SYSTEM_PROMPT에 변수 주입 후 반환"""
    if not (1 <= num_sets <= 5):
        raise ValueError("NUM_SETS must be 1–5")
    if set_type == "Single" and len(passage_types) != 1:
        raise ValueError("Single passage set must have 1 passage type.")
    if set_type == "Double" and len(passage_types) != 2:
        raise ValueError("Double passage set must have 2 passage types.")
    if set_type == "Triple" and len(passage_types) != 3:
        raise ValueError("Triple passage set must have 3 passage types.")

    # Format passage_types as a string representation of a list for the prompt
    passage_types_str = json.dumps(passage_types)

    return SYSTEM_PROMPT.format(
        num_sets=num_sets,
        difficulty=difficulty,
        set_type=set_type,
        passage_types=passage_types_str,
    )


# --------------------- Few-shot 매핑 ---------------------
# Keys for _FEWSHOT_SINGLE are passage type strings.
# Keys for _FEWSHOT_DOUBLE and _FEWSHOT_TRIPLE are tuples of passage type strings.
_FEWSHOT_SINGLE = {
    "Email": Part7SinglePassageFewShotExamples.email,
    "Letter": Part7SinglePassageFewShotExamples.letter,
    "Memo": Part7SinglePassageFewShotExamples.memo,
    "Notice": Part7SinglePassageFewShotExamples.notice,
    "Advertisement": Part7SinglePassageFewShotExamples.advertisement,
    "Article": Part7SinglePassageFewShotExamples.article,
    "Form": Part7SinglePassageFewShotExamples.form,
    "Schedule": Part7SinglePassageFewShotExamples.schedule,
    "Receipt": Part7SinglePassageFewShotExamples.receipt,
    "Chart": Part7SinglePassageFewShotExamples.chart,
    "Chat": Part7SinglePassageFewShotExamples.chat,
    "Report": Part7SinglePassageFewShotExamples.report,
}

_FEWSHOT_DOUBLE = {
    # These keys should match the `passage_types` list provided by the user,
    # assuming the list elements are valid PassageType strings.
    # Example: if user wants Email + Reply Email, passage_types = ["Email", "Email"]
    ("Email", "Email"): Part7DoublePassageFewShotExamples.email_reply,
    ("Email", "Notice"): Part7DoublePassageFewShotExamples.email_notice,
    ("Letter", "Advertisement"): Part7DoublePassageFewShotExamples.letter_advertisement,
    ("Advertisement", "Email"): Part7DoublePassageFewShotExamples.advertisement_inquiry,
    ("Memo", "Schedule"): Part7DoublePassageFewShotExamples.memo_schedule,
    ("Article", "Chart"): Part7DoublePassageFewShotExamples.article_chart,
    ("Article", "Letter"): Part7DoublePassageFewShotExamples.article_letter,
    ("Form", "Notice"): Part7DoublePassageFewShotExamples.form_notice,
}

_FEWSHOT_TRIPLE = {
    (
        "Email",
        "Schedule",
        "Notice",
    ): Part7TriplePassageFewShotExamples.email_schedule_notice,
    ("Chat", "Article", "Form"): Part7TriplePassageFewShotExamples.chat_article_form,
    (
        "Advertisement",
        "Article",
        "Form",
    ): Part7TriplePassageFewShotExamples.advertisement_article_form,
    ("Email", "Memo", "Chart"): Part7TriplePassageFewShotExamples.email_memo_chart,
    (
        "Letter",
        "Advertisement",
        "Receipt",
    ): Part7TriplePassageFewShotExamples.letter_advertisement_receipt,
    ("Email", "Chat", "Report"): Part7TriplePassageFewShotExamples.email_chat_report,
}


def get_fewshot_examples(set_type: str, passage_types: list[str]) -> str:
    """해당 set_type과 passage_types에 맞는 퓨샷을 JSON 문자열로 반환"""
    examples = []

    if set_type == "Single":
        if len(passage_types) == 1:
            passage_type_key_single = passage_types[0]
            examples = _FEWSHOT_SINGLE.get(passage_type_key_single, [])
        else:
            logger.warning(
                f"Warning: Single set_type expects 1 passage type, got {len(passage_types)}. Returning empty list."
            )
            return json.dumps([], ensure_ascii=False, indent=2)
    elif set_type == "Double":
        if len(passage_types) == 2:
            # Explicitly create a tuple of two strings for the key
            passage_type_key_double = (passage_types[0], passage_types[1])
            examples = _FEWSHOT_DOUBLE.get(passage_type_key_double, [])
        else:
            logger.warning(
                f"Warning: Double set_type expects 2 passage types, got {len(passage_types)}. Returning empty list."
            )
            return json.dumps([], ensure_ascii=False, indent=2)
    elif set_type == "Triple":
        if len(passage_types) == 3:
            # Explicitly create a tuple of three strings for the key
            passage_type_key_triple = (
                passage_types[0],
                passage_types[1],
                passage_types[2],
            )
            examples = _FEWSHOT_TRIPLE.get(passage_type_key_triple, [])
        else:
            logger.warning(
                f"Warning: Triple set_type expects 3 passage types, got {len(passage_types)}. Returning empty list."
            )
            return json.dumps([], ensure_ascii=False, indent=2)

    if not examples:
        logger.warning(
            f"Warning: No specific few-shot examples found for set_type='{set_type}' and passage_types='{passage_types}'. Returning empty list."
        )
        return json.dumps([], ensure_ascii=False, indent=2)

    return json.dumps(examples, ensure_ascii=False, indent=2)
