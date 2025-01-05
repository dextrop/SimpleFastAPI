import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, text

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    title = Column(String(200),nullable=False)
    author_name = Column(String(200),nullable=False)
    description = Column(String(500), nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
