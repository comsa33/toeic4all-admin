import json

from app.utils.fewshots.part5_examples import Part5FewShotExamples

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

_SUBTYPE_DESC = {
    # ─ Grammar
    "시제": "동작·상태가 일어나는 시간을 나타내는 형태(현재·과거·미래·완료·진행).",
    "수일치": "주어의 수에 따라 동사형을 일치시키는 규칙.",
    "태(수동/능동)": "능동·수동태 선택으로 행위 주체/대상을 강조.",
    "관계사": "선행사를 수식하며 절을 연결하는 who/which/that 등.",
    "비교구문": "두 대상 이상의 우열·동등 비교(more, the most 등).",
    "가정법": "사실과 다른 가정·희망·제안을 표현(0·1·2·3·혼합).",
    "부정사/동명사": "to-부정사와 동명사의 명사·형용사·부사적 용법.",
    # ─ Vocabulary
    "동의어": "의미가 비슷한 단어를 고르는 문제(big ↔ large).",
    "반의어": "반대 의미 단어를 구별(increase ↔ decrease).",
    "관용표현": "직역 불가 관습적 표현(break the ice).",
    "Collocation": "자연스러운 단어 결합(make a decision).",
    "Phrasal Verb": "동사+전/부사 결합으로 새 의미를 갖는 구동사(look after).",
    # ─ Preposition / Conjunction
    "시간/장소 전치사": "at/on/in 등 시점·기간·장소를 표시.",
    "원인/결과": "because/since (원인) ↔ so/therefore (결과) 구조.",
    "양보": "although/despite 등 역접·양보 표현.",
    "조건": "if/unless/provided (that) 등 조건절 사용.",
    "접속부사": "however/therefore 등 독립절 연결 전환어(세미콜론+쉼표).",
}

_CATEGORY_SUBTYPES = {
    "문법": [
        "시제",
        "수일치",
        "태(수동/능동)",
        "관계사",
        "비교구문",
        "가정법",
        "부정사/동명사",
    ],
    "어휘": [
        "동의어",
        "반의어",
        "관용표현",
        "Collocation",
        "Phrasal Verb",
    ],
    "전치사/접속사/접속부사": [
        "시간/장소 전치사",
        "원인/결과",
        "양보",
        "조건",
        "접속부사",
    ],
}

SYSTEM_PROMPT_TEMPLATE = """You are an ETS-style TOEIC Part 5 item writer.

[VARIABLES]
  NUM_QUESTIONS   = {num}
  DIFFICULTY      = {difficulty}
  CATEGORY        = {category}
  SUBTYPE         = {subtype}

[SUBTYPE DEFINITION]
  • {subtype} : {subtype_desc}

[AVAILABLE SUBTYPES]
{available_subtypes}

[CONTENT RULES]
• 문장 ≤ 20단어(Easy: 15단어 이하, Medium: 15~20단어 이하, Hard: 20~30단어).
• blank 는 ___ 1개.
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


def _available_subtypes_block() -> str:
    """카테고리별 세부유형을 문자열 블록으로 반환."""
    return "\n".join(
        f"  • {cat} : {', '.join(subs)}" for cat, subs in _CATEGORY_SUBTYPES.items()
    )


def build_part5_prompt(num: int, difficulty: str, category: str, subtype: str) -> str:
    """선택한 세부유형 설명을 프롬프트에 동적으로 주입."""
    if not (1 <= num <= 10):
        raise ValueError("NUM_QUESTIONS must be 1–10")

    return SYSTEM_PROMPT_TEMPLATE.format(
        num=num,
        difficulty=difficulty,
        category=category,
        subtype=subtype,
        subtype_desc=_SUBTYPE_DESC.get(subtype, "N/A"),
        available_subtypes=_available_subtypes_block(),
    )


def get_fewshot_examples(subtype: str) -> str:
    """세부유형에 맞는 few-shot JSON(리스트) 반환."""
    return json.dumps(_FEWSHOT_MAP.get(subtype, []), ensure_ascii=False, indent=2)
