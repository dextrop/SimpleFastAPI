import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, Table

Base = declarative_base()

class BaseModel(Base):
    """
    ElevateBase is extended version of Base Model with extra column and functions
    """

    __abstract__ = True
    __table__: Table

    id = Column(Integer, unique=True, autoincrement=True, nullable=False, index=True, primary_key=True)

    # Do we need to enable timezone for below two fields
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

