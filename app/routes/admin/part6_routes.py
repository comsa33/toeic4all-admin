from fastapi import APIRouter, BackgroundTasks, HTTPException, Query

from app.schemas.admin.part6_schemas import (
    Part6GenerationRequest,
    Part6GenerationResponse,
)
from app.services.question_service import QuestionService

router = APIRouter()


@router.post("/generate", response_model=Part6GenerationResponse)
async def generate_part6_questions(
    request: Part6GenerationRequest,
    background_tasks: BackgroundTasks,
    store_in_db: bool = Query(True, description="결과를 데이터베이스에 저장할지 여부"),
    return_sets: bool = Query(
        False, description="생성된 문제 세트 데이터를 응답에 포함할지 여부"
    ),
):
    """
    Part 6 문맥 이해 문제 세트를 생성합니다.

    - **num_sets**: 생성할 문제 세트 수 (1-10)
    - **difficulty**: 난이도 (Easy, Medium, Hard)
    - **passage_type**: 지문 유형 (Email/Letter, Notice 등)
    - **store_in_db**: 생성된 문제를 DB에 저장할지 여부
    - **return_sets**: 생성된 문제 데이터를 응답에 포함할지 여부
    """
    question_service = QuestionService()
    try:
        sets = await question_service.generate_part6_questions(
            request.num_sets, request.difficulty, request.passage_type
        )

        if not sets:
            raise HTTPException(
                status_code=500, detail="문제 세트 생성에 실패했습니다."
            )

        # 백그라운드에서 DB 저장 작업 처리
        if store_in_db:
            background_tasks.add_task(question_service.store_part6_questions, sets)

        return Part6GenerationResponse(
            success=True,
            count=len(sets),
            message=f"{len(sets)}개의 Part 6 문제 세트가 생성되었습니다.",
            sets=sets if return_sets else None,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"문제 생성 중 오류 발생: {str(e)}")


@router.get("/passage_types")
async def get_part6_passage_types():
    """Part 6 지문 유형 목록을 반환합니다."""
    passage_types = [
        "Email/Letter",
        "Notice",
        "Advertisement",
        "Article",
        "Instruction",
        "Form",
        "Schedule",
        "Newsletter",
        "Memo",
    ]
    return passage_types
