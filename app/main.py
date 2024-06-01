import sys
import os
import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.controllers import exchange, quotation, user
from app.models.base_model import Base
from app.db.session import engine
from app.config import settings
from app.test.db_connection_test import router as test_db_router

# 현재 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 로거 가져오기
logger = logging.getLogger(__name__)

app = FastAPI(debug=settings.debug)

# 정적 파일 디렉토리 설정
static_directory = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_directory):
    os.makedirs(static_directory)
app.mount("/static", StaticFiles(directory=static_directory), name="static")

# 템플릿 디렉토리 설정
template_directory = os.path.join(os.path.dirname(__file__), "templates")
if not os.path.exists(template_directory):
    os.makedirs(template_directory)
templates = Jinja2Templates(directory=template_directory)

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(exchange.router, prefix="/api/v1/exchange", tags=["exchange"])
# app.include_router(quotation.router, prefix="/api/v1/quotation", tags=["quotation"])
app.include_router(test_db_router, prefix="/api/v1", tags=["test"])


@app.get("/")
def read_root(request: Request):
    logger.info("Root endpoint accessed")
    return templates.TemplateResponse(
        "home/index.html",
        {
            "request": request,
            "message": f"Welcome to the Coin Trading App",
        },
    )
