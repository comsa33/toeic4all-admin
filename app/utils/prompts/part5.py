import json

from app.utils.fewshots.part5_examples import Part5FewShotExamples

SYSTEM_PROMPT_TEMPLATE = """You are an ETS-style TOEIC Part 5 item writer.

[VARIABLES]
  NUM_QUESTIONS   = {num}
  DIFFICULTY      = {difficulty}
  CATEGORY        = {category}
  SUBTYPE         = {subtype}

[AVAILABLE SUBTYPES]
  • 문법 : 시제, 수일치, 태(수동/능동), 관계사, 비교구문, 가정법, 부정사/동명사
  • 어휘 : 동의어, 반의어, 관용표현, Collocation, Phrasal Verb
  • 전치사/접속사/접속부사 : 시간/장소 전치사, 원인/결과, 양보, 조건, 접속부사

[CONTENT RULES]
• 문장 ≤ 20단어, blank 는 ___ 1개.
• Distractor 3개는 의미·형태 plausibility.
• CEFR A2/B1/B2 어휘로 난이도 통제.
• 반환은 JSON 배열: 각 원소가 “단일 문제” 객체 (스키마 아래 참조).

[OUTPUT SCHEMA]
{{
  "part": 5,
  "questionCategory": "{category}",
  "questionSubType":  "{subtype}",
  "difficulty": "{difficulty}",
  "questionText": "<ENGLISH_SENTENCE_WITH___>",
  "questionTranslation": "<KOREAN_TRANSLATION>",
  "choices": [
    {{ "id":"A","text":"...","translation":"..." }},
    {{ "id":"B","text":"...","translation":"..." }},
    {{ "id":"C","text":"...","translation":"..." }},
    {{ "id":"D","text":"...","translation":"..." }}
  ],
  "answer": "<A|B|C|D>",
  "explanation": "<Korean why correct>",
  "vocabulary":[
    {{ "word":"...","meaning":"...","partOfSpeech":"...","example":"...","exampleTranslation":"..." }}
  ]
}}

[STYLE]
• JSON only, no markdown, no extra keys.
"""


def build_part5_prompt(num: int, difficulty: str, category: str, subtype: str) -> str:
    if not (1 <= num <= 10):
        raise ValueError("NUM_QUESTIONS must be 1–10")
    return SYSTEM_PROMPT_TEMPLATE.format(
        num=num, difficulty=difficulty, category=category, subtype=subtype
    )


_FEWSHOT_MAP = {
    "시제": Part5FewShotExamples.grammar_tense,
    "수일치": Part5FewShotExamples.grammar_subject_verb_agreement,
    "태(수동/능동)": Part5FewShotExamples.grammar_voice,
    "관계사": Part5FewShotExamples.grammar_relative_clause,
    "비교구문": Part5FewShotExamples.grammar_comparative,
    "가정법": Part5FewShotExamples.grammar_conditional,
    "부정사/동명사": Part5FewShotExamples.grammar_infinitive_gerund,
    "동의어": Part5FewShotExamples.vocabulary_synonym,
    "반의어": Part5FewShotExamples.vocabulary_antonym,
    "관용표현": Part5FewShotExamples.vocabulary_idiom,
    "Collocation": Part5FewShotExamples.vocabulary_collocation,
    "Phrasal Verb": Part5FewShotExamples.vocabulary_phrasal_verb,
    "시간/장소 전치사": Part5FewShotExamples.preposition_time_place,
    "원인/결과": Part5FewShotExamples.conjunction_cause_effect,
    "양보": Part5FewShotExamples.conjunction_concession,
    "조건": Part5FewShotExamples.conjunction_condition,
    "접속부사": Part5FewShotExamples.conjunction_preposition_conjunctive_adverb,
}


def get_fewshot_examples(subtype: str) -> str:
    """세부유형에 맞는 few-shot JSON(리스트) 반환."""
    return json.dumps(_FEWSHOT_MAP.get(subtype, []), ensure_ascii=False, indent=2)
