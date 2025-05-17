# TOEIC Question Generator API

TOEIC Part 5, 6, 7 문제를 자동으로 생성하고 관리하는 FastAPI 기반 백엔드 서버입니다.

## 기능

- TOEIC Part 5 (문법/어휘) 문제 생성
- TOEIC Part 6 (문맥 이해) 문제 세트 생성
- TOEIC Part 7 (독해) 문제 세트 생성 (단일/이중/삼중 지문)
- 생성된 문제 데이터베이스 저장
- REST API를 통한 문제 생성 및 관리

## 시작하기

### 필수 조건
- Python 3.12 이상
- MongoDB (문제 데이터 저장용)
- Gemini API 키 (문제 생성용)
