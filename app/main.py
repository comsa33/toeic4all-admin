from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import part5_routes, part6_routes, part7_routes

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="TOEIC Question Generator API",
    description="FastAPI backend for generating TOEIC test questions",
    version="1.0.0",
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 실제 프론트엔드 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(part5_routes.router, prefix="/api/v1/part5", tags=["Part 5"])
app.include_router(part6_routes.router, prefix="/api/v1/part6", tags=["Part 6"])
app.include_router(part7_routes.router, prefix="/api/v1/part7", tags=["Part 7"])


@app.get("/")
async def root():
    """API 서버 상태 확인 엔드포인트"""
    return {"status": "online", "message": "TOEIC Question Generator API is running"}
