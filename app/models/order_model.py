from sqlalchemy import Column, Integer, String, Boolean
from app.models.base_model import Base


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String, nullable=False)
    acess_key = Column(String, nullable=True)
    secret_key = Column(String, nullable=True)
