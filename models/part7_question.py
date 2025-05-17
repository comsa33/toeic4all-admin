from typing import Annotated, List, Literal

from pydantic import BaseModel, Field

SeqInt = Annotated[int, Field(ge=1)]


class PassageChunk(BaseModel):
    seq: SeqInt
    text: str
    translation: str | None = None


class Choice(BaseModel):
    id: Literal["A", "B", "C", "D"]
    text: str
    translation: str


class SubQuestion(BaseModel):
    questionSeq: SeqInt
    questionType: Literal[
        "주제/목적", "세부사항", "추론", "어휘", "참조", "일치", "정보연계"
    ]
    questionText: str
    questionTranslation: str
    choices: List[Choice] = Field(..., min_length=4, max_length=4)
    answer: Literal["A", "B", "C", "D"]
    explanation: str


class Part7Set(BaseModel):
    part: int = Field(7, frozen=True)
    passages: List[PassageChunk] = Field(..., min_length=1, max_length=3)
    questions: List[SubQuestion] = Field(..., min_length=2)
