from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, User as UserSchema
from app.db.session import get_db

router = APIRouter()


@router.post("/register", response_model=UserSchema)
async def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 중복확인
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 가입된 회원입니다.")

    db_user = User(
        email=user_in.email,
        password=user_in.password,
        access_key=user_in.access_key,
        secret_key=user_in.secret_key,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{email}", response_model=UserSchema)
async def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 회원입니다.")
    return user
