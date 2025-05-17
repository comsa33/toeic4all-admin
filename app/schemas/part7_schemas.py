from typing import List, Optional

from pydantic import BaseModel, Field, validator


class Part7GenerationRequest(BaseModel):
    """Part 7 문제 생성 요청 스키마"""

    num_sets: int = Field(..., ge=1, le=5, description="생성할 문제 세트 수 (1-5)")
    difficulty: str = Field(
        ..., description="문제 난이도", pattern="^(Easy|Medium|Hard)$"
    )
    set_type: str = Field(
        ..., description="문제 세트 유형", pattern="^(Single|Double|Triple)$"
    )
    passage_types: List[str] = Field(..., description="지문 유형 리스트")

    @validator("passage_types")
    def validate_passage_types(cls, v, values):
        if "set_type" not in values:
            return v

        set_type = values["set_type"]
        expected_length = {"Single": 1, "Double": 2, "Triple": 3}.get(set_type, 0)

        if len(v) != expected_length:
            raise ValueError(
                f"{set_type} set type requires {expected_length} passage type(s), got {len(v)}"
            )

        allowed_types = [
            "Email",
            "Letter",
            "Memo",
            "Notice",
            "Advertisement",
            "Article",
            "Form",
            "Schedule",
            "Receipt",
            "Chart",
            "Chat",
            "Report",
            "Other",
        ]

        for passage_type in v:
            if passage_type not in allowed_types:
                raise ValueError(f"Invalid passage type: {passage_type}")

        return v


class Part7GenerationResponse(BaseModel):
    """Part 7 문제 생성 응답 스키마"""

    success: bool
    count: int = Field(..., description="생성된 문제 세트 수")
    message: str = Field(default="Question sets generated successfully")
    sets: Optional[List] = Field(
        default=None, description="생성된 문제 세트 데이터(요청 시)"
    )
