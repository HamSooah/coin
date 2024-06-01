from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


class User(UserInDBBase):
    access_key: Optional[str] = None
    secret_key: Optional[str] = None


class UserInDB(UserInDBBase):
    password: str


class UserSignIn(UserBase):
    password: str
