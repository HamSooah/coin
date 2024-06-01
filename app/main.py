import sys
import os
import logging
from fastapi import FastAPI

# 현재 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.controllers import exchange, quotation, user
from app.models.base_model import Base
from app.db.session import engine
from app.config import settings
from app.test.db_connection_test import router as test_db_router
from fastapi.staticfiles import StaticFiles
from app.common.logger import setup_logging

# 로깅 설정 초기화
setup_logging()

# 로거 가져오기
logger = logging.getLogger(__name__)

app = FastAPI(debug=settings.debug)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(exchange.router, prefix="/api/v1/exchange", tags=["exchange"])
# app.include_router(quotation.router, prefix="/api/v1/quotation", tags=["quotation"])
app.include_router(test_db_router, prefix="/api/v1", tags=["test"])


@app.get("/")
def read_root():
    return {"message": f"Welcome to the Coin Trading App"}
