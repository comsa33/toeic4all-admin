from pymongo import AsyncMongoClient

from app.config import settings

mongo_options = {
    "maxPoolSize": 30,  # 최대 연결 풀 크기 증가
    "minPoolSize": 5,  # 최소 연결 풀 유지
    "maxIdleTimeMS": 30000,  # 유휴 연결 유지 시간
    "socketTimeoutMS": 240000,  # 소켓 타임아웃 증가
    "connectTimeoutMS": 120000,  # 연결 타임아웃 증가
    "serverSelectionTimeoutMS": 40000,  # 서버 선택 타임아웃
    "retryWrites": True,  # 쓰기 작업 재시도
    "waitQueueTimeoutMS": 25000,  # 대기 큐 타임아웃
}

# MongoDB 클라이언트 생성
client = AsyncMongoClient(settings.mongodb_url, **mongo_options)
db = client[settings.database_name]

# 컬렉션 참조 생성
part5_collection = db["part5_questions"]
part6_collection = db["part6_sets"]
part7_collection = db["part7_sets"]


async def get_database():
    """데이터베이스 의존성 주입을 위한 함수"""
    return db
