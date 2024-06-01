from sqlalchemy import Column, Integer, String, Boolean
from app.models.base_model import Base


class User(Base):
    __tablename__ = "User"

    email = Column(
        String(255), primary_key=True, unique=True, nullable=False, index=True
    )
    password = Column(String(255), nullable=False)
    access_key = Column(String(255), nullable=True)
    secret_key = Column(String(255), nullable=True)
