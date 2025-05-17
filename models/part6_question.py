from typing import Annotated, List, Literal

from pydantic import BaseModel, Field

# ── 타입 별칭: 1 ~ 4 사이 정수 ───────────────────────
BlankNo = Annotated[int, Field(ge=1, le=4)]


class Choice(BaseModel):
    id: Literal["A", "B", "C", "D"]
    text: str
    translation: str


class SubQuestion(BaseModel):
    blankNumber: BlankNo
    questionType: Literal["어휘/문법", "연결어", "문장 삽입", "문장 위치"]
    choices: List[Choice] = Field(..., min_length=4, max_length=4)
    answer: Literal["A", "B", "C", "D"]
    explanation: str


class Part6Set(BaseModel):
    part: int = Field(6, frozen=True)
    passage: str
    passageTranslation: str | None = None
    questions: List[SubQuestion] = Field(..., min_length=4, max_length=4)
