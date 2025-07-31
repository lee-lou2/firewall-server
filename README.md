# 방화벽 관리 시스템

Django와 Django REST Framework를 기반으로 구축된 방화벽 관리 시스템

## 주요 기능

*   **장비 관리:** 방화벽 대상 디바이스 관리
*   **도메인 관리:** 허용 도메인 관리
*   **감사 로그:** 감사 로그 기록
*   **예약 작업:** 비동기 스케쥴러

## 기술 스택

*   **백엔드:** Django, Django REST Framework
*   **스케줄러:** django-apscheduler
*   **WSGI 서버:** gunicorn
*   **정적 파일:** whitenoise

## 사전 요구 사항

*   Python 3.x
*   Pip (Python 패키지 설치 프로그램)

## 설치 방법

1.  **저장소 복제:**
    ```bash
    git clone <저장소-URL>
    cd firewall-server
    ```

2.  **가상 환경 생성 및 활성화:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **의존성 설치:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **데이터베이스 마이그레이션 실행:**
    ```bash
    python manage.py migrate
    ```
    
## 애플리케이션 실행

### 환경 변수 설정

```bash
# .env
SECRET_KEY=
ALLOWED_HOSTS=
CSRF_TRUSTED_ORIGINS=
DEBUG=False
SLACK_WEBHOOK_URL=
HASH_SALT=
```

### 개발 서버

개발 서버를 실행하려면:

```bash
python manage.py runserver
```

### 프로덕션 서버 (Gunicorn 사용)

Gunicorn으로 애플리케이션을 실행하려면:

```bash
gunicorn conf.wsgi:application --bind 0.0.0.0:8000
```
