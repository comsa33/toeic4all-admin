import asyncio
import time

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query

from app.schemas.admin.part6_schemas import (
    Part6GenerationRequest,
    Part6GenerationResponse,
)
from app.services.question_service import QuestionService
from app.utils.logger import logger

router = APIRouter()
_active_tasks = set()
_task_lock = asyncio.Lock()


async def get_question_service() -> QuestionService:
    """QuestionService 의존성 주입 함수"""
    return QuestionService()


@router.post("/generate", response_model=Part6GenerationResponse)
async def generate_part6_questions(
    request: Part6GenerationRequest,
    background_tasks: BackgroundTasks,
    store_in_db: bool = Query(True, description="결과를 데이터베이스에 저장할지 여부"),
    return_sets: bool = Query(
        False, description="생성된 문제 세트 데이터를 응답에 포함할지 여부"
    ),
    question_service: QuestionService = Depends(get_question_service),
):
    """
    Part 6 문맥 이해 문제 세트를 생성합니다.

    - **num_sets**: 생성할 문제 세트 수 (1-10)
    - **difficulty**: 난이도 (Easy, Medium, Hard)
    - **passage_type**: 지문 유형 (Email/Letter, Notice 등)
    - **store_in_db**: 생성된 문제를 DB에 저장할지 여부
    - **return_sets**: 생성된 문제 데이터를 응답에 포함할지 여부
    """
    # 작업 ID 생성 (중복 제거용)
    task_id = f"part6_{request.passage_type}_{request.difficulty}_{request.num_sets}_{int(time.time())}"

    try:
        logger.info(
            f"Generating Part 6 sets: {request.passage_type}, {request.difficulty}, count={request.num_sets}"
        )

        sets = await question_service.generate_part6_questions(
            request.num_sets, request.difficulty, request.passage_type
        )

        if not sets:
            raise HTTPException(
                status_code=500, detail="문제 세트 생성에 실패했습니다."
            )

        # 백그라운드에서 DB 저장 작업 처리 (중복 방지)
        if store_in_db:

            async def store_sets_task():
                try:
                    async with _task_lock:
                        if task_id in _active_tasks:
                            logger.warning(
                                f"Task {task_id} is already in progress, skipping"
                            )
                            return
                        _active_tasks.add(task_id)

                    success, error_msg = await question_service.store_part6_questions(
                        sets
                    )

                    if not success:
                        logger.error(f"Failed to store Part 6 sets: {error_msg}")
                finally:
                    async with _task_lock:
                        _active_tasks.discard(task_id)

            background_tasks.add_task(store_sets_task)

        return Part6GenerationResponse(
            success=True,
            count=len(sets),
            message=f"{len(sets)}개의 Part 6 문제 세트가 생성되었습니다.",
            sets=sets if return_sets else None,
        )

    except Exception as e:
        logger.exception(f"Error in generate_part6_questions: {str(e)}")
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


@router.get("/active-tasks", include_in_schema=False)
async def get_active_tasks():
    """현재 진행 중인 작업 목록 (디버깅용)"""
    async with _task_lock:
        return {"active_tasks": list(_active_tasks)}
