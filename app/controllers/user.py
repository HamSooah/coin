from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserSignIn, User as UserSchema
from app.db.session import get_db
from app.core.security import verify_password, get_password_hash

router = APIRouter()


# 회원가입
@router.post("/signup", response_model=UserSchema)
async def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    # 중복확인
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 가입된 회원입니다.")

    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        password=hashed_password,
        access_key=user_in.access_key,
        secret_key=user_in.secret_key,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 로그인
@router.post("/login", response_model=UserSchema)
async def login(user_in: UserSignIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()
    if user is None or not verify_password(user_in.password, user.password):
        raise HTTPException(
            status_code=4044, detail="이메일 또는 비밀번호가 옳바르지 않습니다"
        )
    return user


@router.get("/{email}", response_model=UserSchema)
async def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="존재하지 않는 회원입니다.")
    return user
