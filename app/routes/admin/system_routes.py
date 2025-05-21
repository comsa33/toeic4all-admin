# app/routes/admin/system_routes.py 파일 생성

from fastapi import APIRouter, Depends, HTTPException

from app.db.redis_lock import RedisClient
from app.utils.logger import logger

router = APIRouter()


# Redis 의존성 함수
async def get_redis():
    return await RedisClient.get_instance()


@router.get("/locks")
async def get_all_locks(redis=Depends(get_redis)):
    """현재 활성 락 상태 조회"""
    try:
        # 락 패턴으로 키 검색
        locks = await redis.keys("lock:*")
        lock_info = {}

        for lock_key in locks:
            lock_name = lock_key.replace("lock:", "")
            lock_value = await redis.get(lock_key)
            # TTL 조회
            ttl = await redis.ttl(lock_key)

            lock_info[lock_name] = {"value": lock_value, "ttl_seconds": ttl}

        return {"active_locks_count": len(locks), "locks": lock_info}
    except Exception as e:
        logger.error(f"Error retrieving lock information: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tasks")
async def get_all_tasks(redis=Depends(get_redis)):
    """모든 작업 목록 조회"""
    try:
        # 라우터 작업
        router_tasks = await redis.smembers("active_tasks")
        router_tasks_info = []

        for task_id in router_tasks:
            task_data = await redis.get(f"task:{task_id}")
            if task_data:
                router_tasks_info.append({"id": task_id, "data": task_data})

        # 서비스 작업
        service_tasks = await redis.smembers("qs:active_tasks")
        service_tasks_info = []

        for task_id in service_tasks:
            task_data = await redis.get(f"qs:task:{task_id}")
            if task_data:
                service_tasks_info.append({"id": task_id, "data": task_data})

        return {
            "router_tasks_count": len(router_tasks_info),
            "router_tasks": router_tasks_info,
            "service_tasks_count": len(service_tasks_info),
            "service_tasks": service_tasks_info,
        }
    except Exception as e:
        logger.error(f"Error retrieving task information: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str, redis=Depends(get_redis)):
    """특정 작업 강제 삭제"""
    try:
        # 라우터 작업 확인
        router_exists = await redis.exists(f"task:{task_id}")
        if router_exists:
            await redis.delete(f"task:{task_id}")
            await redis.srem("active_tasks", task_id)
            return {"message": f"Router task {task_id} deleted"}

        # 서비스 작업 확인
        service_exists = await redis.exists(f"qs:task:{task_id}")
        if service_exists:
            await redis.delete(f"qs:task:{task_id}")
            await redis.srem("qs:active_tasks", task_id)
            return {"message": f"Service task {task_id} deleted"}

        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/locks/{lock_name}")
async def delete_lock(lock_name: str, redis=Depends(get_redis)):
    """특정 락 강제 해제"""
    try:
        lock_key = f"lock:{lock_name}"
        exists = await redis.exists(lock_key)

        if not exists:
            raise HTTPException(status_code=404, detail=f"Lock {lock_name} not found")

        await redis.delete(lock_key)
        return {"message": f"Lock {lock_name} released"}
    except Exception as e:
        logger.error(f"Error releasing lock {lock_name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-locks")
async def reset_all_locks(redis=Depends(get_redis)):
    """모든 락 초기화 (긴급 상황용)"""
    try:
        # 락 패턴으로 키 검색
        locks = await redis.keys("lock:*")

        # 모든 락 삭제
        if locks:
            await redis.delete(*locks)

        return {"message": f"Reset {len(locks)} locks", "locks_deleted": locks}
    except Exception as e:
        logger.error(f"Error resetting locks: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-tasks")
async def reset_all_tasks(redis=Depends(get_redis)):
    """모든 작업 초기화 (긴급 상황용)"""
    try:
        # 라우터 작업 목록 초기화
        router_tasks = await redis.smembers("active_tasks")
        for task_id in router_tasks:
            await redis.delete(f"task:{task_id}")
        await redis.delete("active_tasks")

        # 서비스 작업 목록 초기화
        service_tasks = await redis.smembers("qs:active_tasks")
        for task_id in service_tasks:
            await redis.delete(f"qs:task:{task_id}")
        await redis.delete("qs:active_tasks")

        return {
            "message": f"Reset {len(router_tasks)} router tasks and {len(service_tasks)} service tasks",
            "router_tasks_deleted": list(router_tasks),
            "service_tasks_deleted": list(service_tasks),
        }
    except Exception as e:
        logger.error(f"Error resetting tasks: {e}")
        raise HTTPException(status_code=500, detail=str(e))
