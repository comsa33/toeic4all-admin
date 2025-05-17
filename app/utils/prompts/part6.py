import json

from app.utils.fewshots.part6_examples import Part6FewShotExamples

# --------------------- 시스템 프롬프트 ---------------------
SYSTEM_PROMPT = """You are an ETS-style TOEIC Part 6 item writer.

[VARIABLES]
  NUM_PASSAGES   = {num}          # 생성할 문제 세트 수 (1–10)
  DIFFICULTY     = {difficulty}   # Easy | Medium | Hard
  PASSAGE_TYPE   = {ptype}        # Email/Letter | Memo | Advertisement | ...
  (각 세트는 질문유형 4종을 1개씩 포함해야 함)

[QUESTION-TYPE 설명]
  • 어휘/문법   : 시제·수일치·품사 등 단어/구조 선택
  • 연결어     : 접속사·전환 부사 등 논리 연결어 선택
  • 문장 삽입   : 4개 문장 중 빈칸에 가장 자연스러운 문장 선택
  • 문장 위치   : 지문 안 (A)(B)(C)(D) 마커 중 문장을 넣을 위치 선택

[CONTENT RULES]
• 지문 길이 80–120 words, realistic business context.
• 지문에는 **정확히 3개의 ___(blank)** 포함.
• 문장 위치 문제를 위해 A, B, C, D 위치 마커를 본문에 삽입 (예: "(A) ... (B) ... (C) ... (D)").
• 문장 위치 문제 → blankNumber는 4.
• questions 배열 길이 = 4, questionType 4종 각각 1개.
• CEFR A2/B1/B2 어휘 범위 내에서 난이도 조절.
• 모든 해설(explanation)은 한국어.

[OUTPUT SCHEMA]
{{
  "part": 6,
  "difficulty": "{difficulty}", 
  "passageType": "{ptype}",
  "passage": "<ENGLISH_PASSAGE_WITH_4____AND_(A)-(D)_MARKERS>",
  "passageTranslation": "<KOREAN_TRANSLATION>",
  "questions": [
    {{
      "blankNumber": 1,
      "questionType": "연결어|어휘/문법|문장 삽입|문장 위치",
      "choices": [
        {{"id":"A","text":"...","translation":"..."}},
        {{"id":"B","text":"...","translation":"..."}},
        {{"id":"C","text":"...","translation":"..."}},
        {{"id":"D","text":"...","translation":"..."}}
      ],
      "answer":"A|B|C|D",
      "explanation":"<왜 정답인지 한국어로 설명>"
    }}
    /* repeat blankNumber 2–4 */
  ]
}}

[STYLE]
• 출력은 JSON 배열만 반환 (no markdown, no extra keys).
"""


# --------------------- 프롬프트 빌더 ---------------------
def build_part6_prompt(num: int, difficulty: str, ptype: str) -> str:
    """SYSTEM_PROMPT에 변수 주입 후 반환"""
    if not (1 <= num <= 10):
        raise ValueError("NUM_PASSAGES must be 1–10")
    return SYSTEM_PROMPT.format(num=num, difficulty=difficulty, ptype=ptype)


# --------------------- Few-shot 매핑 ---------------------
_FEWSHOT = {
    "Notice": Part6FewShotExamples.notice,
    "Email/Letter": Part6FewShotExamples.email_letter,  # 클래스 속성명에 맞춤
    "Advertisement": Part6FewShotExamples.advertisement,
    "Article": Part6FewShotExamples.article,
    "Instruction": Part6FewShotExamples.instruction,
    "Form": Part6FewShotExamples.form,
    "Schedule": Part6FewShotExamples.schedule,
    "Newsletter": Part6FewShotExamples.newsletter,
    "Memo": Part6FewShotExamples.memo,
}


def get_fewshot_examples(ptype: str) -> str:
    """해당 passageType 퓨샷을 JSON 문자열로 반환"""
    data = _FEWSHOT.get(ptype, [])
    # ensure_ascii=False → 한글 그대로, indent=2 → 가독성
    return json.dumps(data, ensure_ascii=False, indent=2)
