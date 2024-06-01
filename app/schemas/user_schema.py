from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str
    access_key: str | None = None
    secret_key: str | None = None


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True


class User(UserInDBBase):
    access_key: str | None = None
    secret_key: str | None = None


class UserInDB(UserInDBBase):
    password: str
