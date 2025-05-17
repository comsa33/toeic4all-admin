from fastapi import APIRouter, BackgroundTasks, HTTPException, Query

from app.schemas.admin.part7_schemas import (
    Part7GenerationRequest,
    Part7GenerationResponse,
)
from app.services.question_service import QuestionService

router = APIRouter()


@router.post("/generate", response_model=Part7GenerationResponse)
async def generate_part7_questions(
    request: Part7GenerationRequest,
    background_tasks: BackgroundTasks,
    store_in_db: bool = Query(True, description="결과를 데이터베이스에 저장할지 여부"),
    return_sets: bool = Query(
        False, description="생성된 문제 세트 데이터를 응답에 포함할지 여부"
    ),
):
    """
    Part 7 지문 이해 문제 세트를 생성합니다.

    - **num_sets**: 생성할 문제 세트 수 (1-5)
    - **difficulty**: 난이도 (Easy, Medium, Hard)
    - **set_type**: 문제 세트 유형 (Single, Double, Triple)
    - **passage_types**: 지문 유형 리스트 - set_type에 따라 길이가 달라짐
    - **store_in_db**: 생성된 문제를 DB에 저장할지 여부
    - **return_sets**: 생성된 문제 데이터를 응답에 포함할지 여부
    """
    question_service = QuestionService()
    try:
        sets = await question_service.generate_part7_questions(
            request.num_sets,
            request.difficulty,
            request.set_type,
            request.passage_types,
        )

        if not sets:
            raise HTTPException(
                status_code=500, detail="문제 세트 생성에 실패했습니다."
            )

        # 백그라운드에서 DB 저장 작업 처리
        if store_in_db:
            background_tasks.add_task(question_service.store_part7_questions, sets)

        return Part7GenerationResponse(
            success=True,
            count=len(sets),
            message=f"{len(sets)}개의 Part 7 {request.set_type} 문제 세트가 생성되었습니다.",
            sets=sets if return_sets else None,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"문제 생성 중 오류 발생: {str(e)}")


@router.get("/passage_types")
async def get_part7_passage_types():
    """Part 7 지문 유형 목록을 반환합니다."""
    passage_types = [
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
    return passage_types


@router.get("/set_types")
async def get_part7_set_types():
    """Part 7 문제 세트 유형 및 필수 지문 개수를 반환합니다."""
    set_types = {
        "Single": {"description": "단일 지문 세트", "required_passages": 1},
        "Double": {"description": "이중 지문 세트", "required_passages": 2},
        "Triple": {"description": "삼중 지문 세트", "required_passages": 3},
    }
    return set_types
