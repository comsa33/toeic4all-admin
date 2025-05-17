from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.admin import part5_routes, part6_routes, part7_routes
from app.routes.api import part5_api, part6_api, part7_api

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="TOEIC Question Generator & API",
    description="TOEIC 문제 생성 및 조회 API",
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

# 관리자용 API 라우터 등록
app.include_router(
    part5_routes.router, prefix="/api/v1/admin/part5", tags=["Admin - Part 5"]
)
app.include_router(
    part6_routes.router, prefix="/api/v1/admin/part6", tags=["Admin - Part 6"]
)
app.include_router(
    part7_routes.router, prefix="/api/v1/admin/part7", tags=["Admin - Part 7"]
)

# 사용자용 API 라우터 등록
app.include_router(
    part5_api.router, prefix="/api/v1/questions/part5", tags=["Questions - Part 5"]
)
app.include_router(
    part6_api.router, prefix="/api/v1/questions/part6", tags=["Questions - Part 6"]
)
app.include_router(
    part7_api.router, prefix="/api/v1/questions/part7", tags=["Questions - Part 7"]
)


@app.get("/")
async def root():
    """API 서버 상태 확인 엔드포인트"""
    return {"status": "online", "message": "TOEIC Question Generator & API is running"}
