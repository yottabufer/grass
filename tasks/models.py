from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from .database import Base


class Task(BaseModel):
    """
    Модель для работы с задачами, а конкретно для валидации при создании в методе create_task менеджера TaskManager
    """
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, index=True)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)
