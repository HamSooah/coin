from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

router = APIRouter()


@router.get("/test-db-connection")
async def test_db_connection(db: Session = Depends(get_db)):
    try:
        # 단순한 쿼리 실행
        result = db.execute(text("SELECT 1"))
        return {"status": "success", "result": [row[0] for row in result]}
    except Exception as e:
        return {"status": "failure", "error": str(e)}
