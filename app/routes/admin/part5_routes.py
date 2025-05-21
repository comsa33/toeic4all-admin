# app/routes/admin/part5_routes.py 수정
import json
import time

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Query

from app.db.redis_lock import RedisClient, RedisLock
from app.schemas.admin.part5_schemas import (
    Part5GenerationRequest,
    Part5GenerationResponse,
)
from app.services.question_service import QuestionService
from app.utils.logger import logger

router = APIRouter()


# Redis 의존성 함수
async def get_redis():
    return await RedisClient.get_instance()


async def get_question_service() -> QuestionService:
    """QuestionService 의존성 주입 함수"""
    return QuestionService()


# 활성 작업 관리 함수들
async def check_task_exists(task_id: str, redis):
    """작업 ID가 이미 존재하는지 확인"""
    return await redis.exists(f"task:{task_id}")


async def register_task(task_id: str, metadata: dict, redis, ttl: int = 3600):
    """작업 등록 (TTL 설정)"""
    await redis.set(f"task:{task_id}", json.dumps(metadata), ex=ttl)
    await redis.sadd("active_tasks", task_id)
    logger.info(f"Task {task_id} registered with TTL {ttl}s")


async def unregister_task(task_id: str, redis):
    """작업 등록 해제"""
    await redis.delete(f"task:{task_id}")
    await redis.srem("active_tasks", task_id)
    logger.info(f"Task {task_id} unregistered")


async def get_active_tasks(redis):
    """활성 작업 목록 조회"""
    task_ids = await redis.smembers("active_tasks")
    tasks = []
    for task_id in task_ids:
        task_data = await redis.get(f"task:{task_id}")
        if task_data:
            tasks.append({"id": task_id, "metadata": json.loads(task_data)})
    return tasks


@router.post("/generate", response_model=Part5GenerationResponse)
async def generate_part5_questions(
    request: Part5GenerationRequest,
    background_tasks: BackgroundTasks,
    store_in_db: bool = Query(True, description="결과를 데이터베이스에 저장할지 여부"),
    return_questions: bool = Query(
        False, description="생성된 문제 데이터를 응답에 포함할지 여부"
    ),
    question_service: QuestionService = Depends(get_question_service),
    redis=Depends(get_redis),
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
    # 작업 ID 생성
    task_id = f"part5_{request.category}_{request.subcategory}_{request.difficulty}_{request.num}_{int(time.time())}"

    # Redis 락 사용
    task_lock = RedisLock(
        redis, f"task_lock:{task_id}", expire_seconds=300
    )  # 5분 타임아웃

    # 작업 중복 체크
    if await check_task_exists(task_id, redis):
        return Part5GenerationResponse(
            success=False,
            count=0,
            message="동일한 요청의 작업이 이미 진행 중입니다. 잠시 후 다시 시도해주세요.",
        )

    try:
        logger.info(
            f"Generating Part 5 questions: {request.category}/{request.subcategory}, {request.difficulty}, count={request.num}"
        )

        # 락 획득 시도 (5초 타임아웃)
        if not await task_lock.acquire(timeout=5.0):
            logger.warning(f"Failed to acquire lock for task {task_id}")
            raise HTTPException(
                status_code=503,
                detail="서비스가 현재 사용량이 많습니다. 잠시 후 다시 시도해주세요.",
            )

        # 작업 등록
        await register_task(
            task_id,
            {
                "type": "part5_generation",
                "category": request.category,
                "subcategory": request.subcategory,
                "difficulty": request.difficulty,
                "num": request.num,
                "started_at": time.time(),
                "status": "in_progress",
            },
            redis,
            ttl=3600,  # 1시간 TTL
        )

        # 질문 생성
        questions = await question_service.generate_part5_questions(
            request.num, request.difficulty, request.category, request.subcategory
        )

        if not questions:
            await unregister_task(task_id, redis)
            raise HTTPException(status_code=500, detail="문제 생성에 실패했습니다.")

        # 백그라운드 DB 저장 작업 처리 (개선된 방식)
        if store_in_db:

            async def store_questions_task():
                db_task_id = f"{task_id}_db_store"
                db_lock = RedisLock(
                    redis, f"task_lock:{db_task_id}", expire_seconds=600
                )  # 10분 타임아웃

                lock_acquired = False
                try:
                    # 락 획득 (10초 타임아웃)
                    lock_acquired = await db_lock.acquire(timeout=10.0)
                    if not lock_acquired:
                        logger.error(
                            f"Failed to acquire lock for DB storing task {db_task_id}"
                        )
                        return

                    # 중복 체크 (이미 DB 저장 작업이 진행 중인지)
                    if await check_task_exists(db_task_id, redis):
                        logger.info(
                            f"DB store task {db_task_id} is already in progress, skipping"
                        )
                        return

                    # DB 저장 작업 등록
                    await register_task(
                        db_task_id,
                        {
                            "type": "part5_db_store",
                            "parent_task_id": task_id,
                            "started_at": time.time(),
                            "status": "in_progress",
                            "question_count": len(questions),
                        },
                        redis,
                        ttl=1800,  # 30분 TTL
                    )

                    # DB 저장 작업 실행
                    success, error_msg = await question_service.store_part5_questions(
                        questions
                    )

                    # 작업 상태 업데이트
                    if not success:
                        logger.error(f"Failed to store questions: {error_msg}")
                        await register_task(
                            db_task_id,
                            {
                                "type": "part5_db_store",
                                "parent_task_id": task_id,
                                "started_at": time.time(),
                                "status": "failed",
                                "error": error_msg,
                            },
                            redis,
                            ttl=7200,  # 2시간 TTL (실패 기록 유지)
                        )
                    else:
                        await register_task(
                            db_task_id,
                            {
                                "type": "part5_db_store",
                                "parent_task_id": task_id,
                                "started_at": time.time(),
                                "completed_at": time.time(),
                                "status": "completed",
                                "question_count": len(questions),
                            },
                            redis,
                            ttl=3600,  # 1시간 TTL
                        )

                except Exception as e:
                    logger.exception(f"Error in store_questions_task: {str(e)}")
                    if await check_task_exists(db_task_id, redis):
                        await register_task(
                            db_task_id,
                            {
                                "type": "part5_db_store",
                                "parent_task_id": task_id,
                                "status": "error",
                                "error": str(e),
                            },
                            redis,
                            ttl=7200,  # 2시간 TTL (오류 기록 유지)
                        )
                finally:
                    # 락 해제 보장
                    if lock_acquired:
                        await db_lock.release()

            # 백그라운드 작업 추가
            background_tasks.add_task(store_questions_task)

        # 문제 생성 작업 완료로 상태 업데이트
        await register_task(
            task_id,
            {
                "type": "part5_generation",
                "category": request.category,
                "subcategory": request.subcategory,
                "difficulty": request.difficulty,
                "num": request.num,
                "started_at": time.time(),
                "completed_at": time.time(),
                "status": "completed",
                "question_count": len(questions),
            },
            redis,
            ttl=3600,  # 1시간 TTL
        )

        return Part5GenerationResponse(
            success=True,
            count=len(questions),
            message=f"{len(questions)}개의 Part 5 문제가 생성되었습니다.",
            questions=questions if return_questions else None,
        )

    except Exception as e:
        logger.exception(f"Error in generate_part5_questions: {str(e)}")
        # 오류 상태 업데이트
        try:
            await register_task(
                task_id,
                {
                    "type": "part5_generation",
                    "category": request.category,
                    "subcategory": request.subcategory,
                    "difficulty": request.difficulty,
                    "num": request.num,
                    "started_at": time.time(),
                    "status": "error",
                    "error": str(e),
                },
                redis,
                ttl=7200,  # 2시간 TTL (오류 기록 유지)
            )
        except Exception as reg_err:
            logger.error(f"Failed to register error state: {reg_err}")

        raise HTTPException(status_code=500, detail=f"문제 생성 중 오류 발생: {str(e)}")
    finally:
        # 락 해제 보장
        await task_lock.release()


@router.get("/categories")
async def get_part5_categories(redis=Depends(get_redis)):
    """Part 5 문법 카테고리 및 서브카테고리 목록을 반환합니다."""

    # 캐시 키 정의
    cache_key = "part5:categories_cache"

    # 캐시 확인
    cached_data = await redis.get(cache_key)
    if cached_data:
        return json.loads(cached_data)

    # 캐시가 없으면 새로 데이터 구성
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

    # 캐시 저장 (1시간 TTL)
    await redis.set(cache_key, json.dumps(categories), ex=3600)

    return categories


@router.get("/active-tasks")
async def get_active_tasks_endpoint(redis=Depends(get_redis)):
    """현재 진행 중인 작업 목록 조회"""
    return {"active_tasks": await get_active_tasks(redis)}
