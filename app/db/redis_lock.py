import asyncio
import time
import uuid
from typing import Optional

from fastapi import HTTPException
from redis.asyncio import Redis

from app.utils.logger import logger


class RedisLock:
    """Redis 기반 분산 락 관리 클래스"""

    def __init__(
        self,
        redis_client: Redis,
        lock_name: str,
        expire_seconds: int = 60,
        retry_delay: float = 0.1,
        retry_times: int = 50,
    ):
        self.redis = redis_client
        self.lock_name = lock_name
        self.expire_seconds = expire_seconds
        self.retry_delay = retry_delay
        self.retry_times = retry_times
        self.lock_value = None

    async def acquire(self, timeout: float = 10.0) -> bool:
        """락 획득을 시도합니다. 타임아웃 내에 획득하지 못하면 False 반환"""
        start_time = time.time()
        self.lock_value = str(uuid.uuid4())

        while time.time() - start_time < timeout:
            # SET NX (Not eXists) 옵션으로 락 획득 시도
            acquired = await self.redis.set(
                f"lock:{self.lock_name}",
                self.lock_value,
                ex=self.expire_seconds,  # 자동 만료 시간 설정
                nx=True,
            )

            if acquired:
                logger.debug(
                    f"Lock '{self.lock_name}' acquired with value '{self.lock_value}'"
                )
                return True

            # 짧은 대기 후 재시도
            await asyncio.sleep(self.retry_delay)

        logger.warning(
            f"Failed to acquire lock '{self.lock_name}' after {timeout} seconds"
        )
        return False

    async def release(self) -> bool:
        """락을 해제합니다. 자신이 소유한 락만 해제 가능"""
        if not self.lock_value:
            logger.warning("Attempting to release an unacquired lock")
            return False

        # Lua 스크립트로 원자적으로 자신의 락만 해제
        script = """
        if redis.call('get', KEYS[1]) == ARGV[1] then
            return redis.call('del', KEYS[1])
        else
            return 0
        end
        """

        result = await self.redis.eval(
            script, keys=[f"lock:{self.lock_name}"], args=[self.lock_value]
        )

        if result:
            logger.debug(f"Lock '{self.lock_name}' released")
            return True
        else:
            logger.warning(
                f"Failed to release lock '{self.lock_name}': not owner or expired"
            )
            return False

    async def __aenter__(self):
        """비동기 컨텍스트 매니저 진입"""
        success = await self.acquire()
        if not success:
            raise HTTPException(
                status_code=503, detail="서비스 일시적으로 사용 불가: 락 획득 실패"
            )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """비동기 컨텍스트 매니저 종료"""
        if exc_type:
            logger.error(
                f"Error in context block with lock '{self.lock_name}': {exc_val}"
            )
        await self.release()


# Redis 클라이언트 싱글톤
class RedisClient:
    """Redis 클라이언트 싱글톤"""

    _instance = None
    _redis: Optional[Redis] = None

    @classmethod
    async def get_instance(cls) -> Redis:
        if cls._redis is None:
            # 환경 변수에서 Redis URL 로드
            from app.config import settings

            redis_url = getattr(settings, "redis_url", "redis://localhost:6379/0")
            cls._redis = Redis.from_url(redis_url, decode_responses=True)
            logger.info(f"Redis connection established to {redis_url}")
        return cls._redis

    @classmethod
    async def close(cls):
        if cls._redis is not None:
            await cls._redis.close()
            cls._redis = None
            logger.info("Redis connection closed")
