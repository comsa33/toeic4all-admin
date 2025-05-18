import asyncio
import time

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query

from app.schemas.admin.part5_schemas import (
    Part5GenerationRequest,
    Part5GenerationResponse,
)
from app.services.question_service import QuestionService
from app.utils.logger import logger

router = APIRouter()
_active_tasks = set()
_task_lock = asyncio.Lock()


async def get_question_service() -> QuestionService:
    """QuestionService 의존성 주입 함수"""
    return QuestionService()


@router.post("/generate", response_model=Part5GenerationResponse)
async def generate_part5_questions(
    request: Part5GenerationRequest,
    background_tasks: BackgroundTasks,
    store_in_db: bool = Query(True, description="결과를 데이터베이스에 저장할지 여부"),
    return_questions: bool = Query(
        False, description="생성된 문제 데이터를 응답에 포함할지 여부"
    ),
    question_service: QuestionService = Depends(get_question_service),
):
    """
    Part 5 문법/어휘 문제를 생성합니다.

    - **num**: 생성할 문제 수 (1-30)
    - **difficulty**: 난이도 (Easy, Medium, Hard)
    - **category**: 문법 카테고리
    - **subcategory**: 문법 서브 카테고리
    - **store_in_db**: 생성된 문제를 DB에 저장할지 여부
    - **return_questions**: 생성된 문제 데이터를 응답에 포함할지 여부
    """
    # 진행중인 작업이 있는지 확인
    task_id = f"part5_{request.category}_{request.subcategory}_{request.difficulty}_{request.num}_{int(time.time())}"

    try:
        logger.info(
            f"Generating Part 5 questions: {request.category}/{request.subcategory}, {request.difficulty}, count={request.num}"
        )

        questions = await question_service.generate_part5_questions(
            request.num, request.difficulty, request.category, request.subcategory
        )

        if not questions:
            raise HTTPException(status_code=500, detail="문제 생성에 실패했습니다.")

        # 백그라운드에서 DB 저장 작업 처리 (중복 방지)
        if store_in_db:

            async def store_questions_task():
                try:
                    async with _task_lock:
                        if task_id in _active_tasks:
                            logger.warning(
                                f"Task {task_id} is already in progress, skipping"
                            )
                            return
                        _active_tasks.add(task_id)

                    success, error_msg = await question_service.store_part5_questions(
                        questions
                    )

                    if not success:
                        logger.error(f"Failed to store questions: {error_msg}")
                finally:
                    async with _task_lock:
                        _active_tasks.discard(task_id)

            background_tasks.add_task(store_questions_task)

        return Part5GenerationResponse(
            success=True,
            count=len(questions),
            message=f"{len(questions)}개의 Part 5 문제가 생성되었습니다.",
            questions=questions if return_questions else None,
        )

    except Exception as e:
        logger.exception(f"Error in generate_part5_questions: {str(e)}")
        raise HTTPException(status_code=500, detail=f"문제 생성 중 오류 발생: {str(e)}")


@router.get("/categories")
async def get_part5_categories():
    """Part 5 문법 카테고리 및 서브카테고리 목록을 반환합니다."""
    # 향후 DB에서 카테고리 목록을 가져오거나 고정된 목록 반환
    categories = {
        "문법": [
            "시제",
            "수일치",
            "태(수동/능동)",
            "관계사",
            "비교구문",
            "가정법",
            "부정사/동명사",
        ],
        "어휘": [
            "동의어",
            "반의어",
            "관용표현",
            "Collocation",
            "Phrasal Verb",
        ],
        "전치사/접속사/접속부사": [
            "시간/장소 전치사",
            "원인/결과",
            "양보",
            "조건",
            "접속부사",
        ],
    }
    return categories


@router.get("/active-tasks", include_in_schema=False)
async def get_active_tasks():
    """현재 진행 중인 작업 목록 (디버깅용)"""
    async with _task_lock:
        return {"active_tasks": list(_active_tasks)}
