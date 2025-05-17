from typing import List, Literal

from pydantic import BaseModel, Field


class Choice(BaseModel):
    id: Literal["A", "B", "C", "D"]
    text: str
    translation: str


class VocabularyItem(BaseModel):
    word: str
    meaning: str
    partOfSpeech: str
    example: str | None = None
    exampleTranslation: str | None = Field(None, alias="exampleTranslation")


class Part5Question(BaseModel):
    part: int = Field(5, frozen=True)
    questionCategory: Literal["문법", "어휘", "전치사/접속사"]
    questionSubType: str
    difficulty: Literal["Easy", "Medium", "Hard"]

    questionText: str
    questionTranslation: str

    choices: List[Choice] = Field(min_length=4, max_length=4)
    answer: Literal["A", "B", "C", "D"]

    explanation: str
    vocabulary: List[VocabularyItem] | None = None
