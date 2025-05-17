from typing import List, Optional

from pydantic import BaseModel, Field, validator


class Part5GenerationRequest(BaseModel):
    """Part 5 문제 생성 요청 스키마"""

    num: int = Field(..., ge=1, le=30, description="생성할 문제 수 (1-30)")
    difficulty: str = Field(
        ..., description="문제 난이도", pattern="^(Easy|Medium|Hard)$"
    )
    category: str = Field(..., description="문법 카테고리")
    subcategory: str = Field(..., description="문법 서브 카테고리")

    @validator("category")
    def validate_category(cls, v):
        allowed_categories = ["문법", "어휘", "전치사/접속사"]
        if v not in allowed_categories:
            raise ValueError(
                f"카테고리는 {', '.join(allowed_categories)} 중 하나여야 합니다."
            )
        return v

    @validator("subcategory")
    def validate_subcategory(cls, v, values):
        if "category" not in values:
            return v

        category = values["category"]
        allowed_subcategories = {
            "문법": [
                "시제",
                "수동태",
                "가정법",
                "동명사/분사",
                "병렬구조",
                "관계절",
                "비교구문",
                "접속사",
            ],
            "어휘": [
                "명사",
                "동사",
                "형용사",
                "부사",
                "전치사",
                "동의어",
                "의미추론",
                "숙어/관용구",
            ],
            "전치사/접속사": ["전치사", "접속사", "전환어", "관계어"],
        }

        if (
            category in allowed_subcategories
            and v not in allowed_subcategories[category]
        ):
            raise ValueError(
                f"{category} 카테고리의 서브카테고리는 {', '.join(allowed_subcategories[category])} 중 하나여야 합니다."
            )

        return v


class Part5GenerationResponse(BaseModel):
    """Part 5 문제 생성 응답 스키마"""

    success: bool
    count: int = Field(..., description="생성된 문제 수")
    message: str = Field(default="Questions generated successfully")
    questions: Optional[List] = Field(
        default=None, description="생성된 문제 데이터(요청 시)"
    )
