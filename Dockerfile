# 단일 스테이지 Dockerfile
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 파이썬 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# uv 설치
RUN pip install uv

# requirements.txt 복사 및 의존성 설치
COPY requirements.txt .
RUN uv pip install --system --no-cache-dir -r requirements.txt gunicorn

# 애플리케이션 코드 복사
COPY . .

# non-root 사용자 생성 및 권한 설정
# 보안을 위해 non-root 사용자로 실행하는 것을 권장합니다.
RUN addgroup --system nonroot && adduser --system --ingroup nonroot nonroot
RUN chown -R nonroot:nonroot /app
USER nonroot

# Gunicorn 실행
CMD ["gunicorn", "conf.wsgi:application", "--bind", "0.0.0.0:8000"]
