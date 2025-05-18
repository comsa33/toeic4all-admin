import asyncio
import random
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

from pymongo.errors import (
    BulkWriteError,
    ConnectionFailure,
    NetworkTimeout,
    OperationFailure,
    ServerSelectionTimeoutError,
)

from app.utils.db import get_collection
from app.utils.logger import logger
from app.utils.models.part5_question import Part5Question
from app.utils.models.part6_question import Part6Set
from app.utils.models.part7_question import Part7Set

# 컬렉션 매핑
COLLECTION_MAPPING = {
    "part5_questions": "part5_questions",
    "part6_sets": "part6_sets",
    "part7_sets": "part7_sets",
}

# 타입 변수 정의
T = TypeVar("T")  # 함수 반환 타입용
ModelType = Union[Part5Question, Part6Set, Part7Set]
ModelList = Union[List[Part5Question], List[Part6Set], List[Part7Set]]

# 동시 DB 작업 제한을 위한 세마포어
_db_semaphore = asyncio.Semaphore(50)  # 최대 50개 동시 연결 허용


def with_retry(
    max_retries: int = 3,
    retry_exceptions: tuple = (
        ConnectionFailure,
        OperationFailure,
        ServerSelectionTimeoutError,
        NetworkTimeout,
    ),
    base_delay: float = 0.5,
):
    """
    비동기 함수에 지수 백오프 재시도 로직을 추가하는 데코레이터

    Args:
        max_retries: 최대 재시도 횟수
        retry_exceptions: 재시도할 예외 종류
        base_delay: 초기 지연 시간 (초)
    """

    def decorator(async_func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(async_func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            last_exception = None

            while retries <= max_retries:
                try:
                    return await async_func(*args, **kwargs)
                except retry_exceptions as e:
                    last_exception = e
                    retries += 1

                    if retries > max_retries:
                        break

                    delay = base_delay * (2 ** (retries - 1))  # 지수 백오프
                    jitter = random.uniform(0, 0.1 * delay)  # 지터 추가
                    wait_time = delay + jitter

                    logger.warning(
                        f"Operation failed: {str(e)}. Retrying in {wait_time:.2f}s... "
                        f"(attempt {retries}/{max_retries})"
                    )
                    await asyncio.sleep(wait_time)

            logger.error(
                f"Operation failed after {max_retries} retries. Last error: {last_exception}"
            )
            raise last_exception

        return wrapper

    return decorator


class DocumentSession:
    """문서 작업을 위한 세션 관리 클래스"""

    def __init__(self, collection_name: str, operation_timeout: Optional[int] = None):
        self.collection_name = COLLECTION_MAPPING.get(collection_name, collection_name)
        self.operation_timeout = operation_timeout
        self._start_time = None

    async def __aenter__(self):
        self._start_time = time.time()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"Error in session for {self.collection_name}: {exc_val}")

        if self._start_time:
            duration = time.time() - self._start_time
            if duration > 1.0:  # 1초 이상 걸린 작업만 로그
                logger.info(
                    f"DB operation on {self.collection_name} took {duration:.2f}s"
                )

    @with_retry()
    async def insert_many(self, documents: List[Dict]) -> List[str]:
        """여러 문서 삽입"""
        async with _db_semaphore:  # 동시 작업 제한
            async with get_collection(self.collection_name) as collection:
                # 타임아웃 설정
                options = {}
                if self.operation_timeout:
                    options["timeoutMS"] = self.operation_timeout

                result = await collection.insert_many(
                    documents, ordered=False, **options  # 실패해도 계속 삽입 시도
                )
                return [str(id) for id in result.inserted_ids]

    @with_retry()
    async def update_many(self, filter_dict: Dict, update_dict: Dict) -> int:
        """필터에 맞는 여러 문서 업데이트"""
        async with _db_semaphore:
            async with get_collection(self.collection_name) as collection:
                result = await collection.update_many(filter_dict, update_dict)
                return result.modified_count

    @with_retry()
    async def find_one(self, filter_dict: Dict) -> Optional[Dict]:
        """단일 문서 조회"""
        async with get_collection(self.collection_name) as collection:
            return await collection.find_one(filter_dict)

    @with_retry()
    async def find_many(
        self,
        filter_dict: Dict,
        limit: int = 0,
        skip: int = 0,
        sort: Optional[List[tuple]] = None,
    ) -> List[Dict]:
        """여러 문서 조회"""
        async with get_collection(self.collection_name) as collection:
            cursor = collection.find(filter_dict)

            if skip:
                cursor = cursor.skip(skip)
            if limit:
                cursor = cursor.limit(limit)
            if sort:
                cursor = cursor.sort(sort)

            return await cursor.to_list(length=limit or None)


async def insert_questions(
    sets: ModelList,
    collection_name: str,
) -> Optional[List[str]]:
    """
    Insert a list of TOEIC questions into the corresponding MongoDB collection.

    Args:
        sets: 모델 객체 리스트 (Part5Question, Part6Set, Part7Set)
        collection_name: 컬렉션 이름

    Returns:
        Optional[List[str]]: 삽입된 문서의 ID 리스트, 실패 시 None
    """
    try:
        # 문서 변환
        docs = [s.model_dump(mode="json") for s in sets]

        # 세션 사용
        async with DocumentSession(collection_name) as session:
            result = await session.insert_many(docs)

            logger.info(
                f"Inserted {len(result)} documents into the {collection_name} collection."
            )
            return result
    except BulkWriteError as e:
        # 일부 문서만 삽입된 경우
        write_errors = e.details.get("writeErrors", [])
        n_inserted = e.details.get("nInserted", 0)

        logger.warning(
            f"Partial insert: {n_inserted} documents inserted with {len(write_errors)} errors. "
            f"First error: {write_errors[0] if write_errors else 'unknown'}"
        )
        return None
    except Exception as e:
        logger.error(f"An error occurred during database insertion: {e}")
        return None


# 벌크 작업용 유틸리티 함수들
async def bulk_update_questions(collection_name: str, operations: List[Dict]) -> bool:
    """벌크 업데이트 작업 수행"""
    try:
        async with DocumentSession(collection_name) as _:
            async with get_collection(collection_name) as collection:
                result = await collection.bulk_write(operations)
                logger.info(
                    f"Bulk update: matched={result.matched_count}, modified={result.modified_count}"
                )
                return True
    except Exception as e:
        logger.error(f"Error in bulk update: {e}")
        return False


async def bulk_delete_questions(collection_name: str, filter_dict: Dict) -> int:
    """벌크 삭제 작업 수행"""
    try:
        async with DocumentSession(collection_name) as _:
            async with get_collection(collection_name) as collection:
                result = await collection.delete_many(filter_dict)
                logger.info(
                    f"Deleted {result.deleted_count} documents from {collection_name}"
                )
                return result.deleted_count
    except Exception as e:
        logger.error(f"Error in bulk delete: {e}")
        return 0
