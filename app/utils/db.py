from pymongo import AsyncMongoClient

from app.config import settings

# MongoDB 클라이언트 생성
client = AsyncMongoClient(settings.mongodb_url)
db = client[settings.database_name]

# 컬렉션 참조 생성
part5_collection = db["part5_questions"]
part6_collection = db["part6_sets"]
part7_collection = db["part7_sets"]


async def get_database():
    """데이터베이스 의존성 주입을 위한 함수"""
    return db
