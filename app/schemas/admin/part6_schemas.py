from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class Part6GenerationRequest(BaseModel):
    """Part 6 문제 생성 요청 스키마"""

    num_sets: int = Field(..., ge=1, le=10, description="생성할 문제 세트 수 (1-10)")
    difficulty: str = Field(
        ..., description="문제 난이도", pattern="^(Easy|Medium|Hard)$"
    )
    passage_type: str = Field(
        ..., description="지문 유형 (e.g., 'Email/Letter', 'Notice')"
    )

    @field_validator("passage_type")
    def validate_passage_type(cls, v, info):
        allowed_passage_types = [
            "Email/Letter",
            "Memo",
            "Advertisement",
            "Notice",
            "Article",
            "Instruction",
            "Form",
            "Schedule",
            "Newsletter",
        ]

        if v not in allowed_passage_types:
            raise ValueError(
                f"지문 유형은 {', '.join(allowed_passage_types)} 중 하나여야 합니다."
            )

        return v


class Part6GenerationResponse(BaseModel):
    """Part 6 문제 생성 응답 스키마"""

    success: bool
    count: int = Field(..., description="생성된 문제 세트 수")
    message: str = Field(default="Question sets generated successfully")
    sets: Optional[List] = Field(
        default=None, description="생성된 문제 세트 데이터(요청 시)"
    )
