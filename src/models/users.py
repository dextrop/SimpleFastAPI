import datetime
from src.models.base import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean
class Users(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    salt = Column(String(200), nullable=False)
    bio = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
