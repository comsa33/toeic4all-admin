import os
import pathlib

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# 현재 파일의 디렉토리 경로 구하기
BASE_DIR = pathlib.Path(__file__).parent
# .env 파일 경로 설정
ENV_PATH = BASE_DIR / ".env"
# .env 파일 로드
load_dotenv(ENV_PATH)


class Settings(BaseSettings):
    """애플리케이션 설정을 관리하는 클래스"""

    # MongoDB 연결 설정
    mongodb_url: str = Field(
        default_factory=lambda: os.getenv("MONGODB_URL", "mongodb://localhost:27017/"),
        description="MongoDB 연결 URL",
    )
    database_name: str = Field(
        default_factory=lambda: os.getenv("DATABASE_NAME", "toeic4all"),
        description="MongoDB 데이터베이스 이름",
    )

    # Gemini API 설정
    gemini_api_key: str = Field(
        default_factory=lambda: os.getenv("GEMINI_API_KEY", ""),
        description="Gemini API 키",
    )

    # 서버 설정
    host: str = Field(
        default_factory=lambda: os.getenv("HOST", "0.0.0.0"), description="서버 호스트"
    )
    port: int = Field(
        default_factory=lambda: int(os.getenv("PORT", "8000")), description="서버 포트"
    )

    # API 설정
    api_prefix: str = Field(
        default_factory=lambda: os.getenv("API_PREFIX", "/api"),
        description="API 경로 접두사",
    )

    # 환경 변수 파일 경로 및 케이스 설정
    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


# 싱글톤 패턴으로 설정 인스턴스 생성
settings = Settings()
