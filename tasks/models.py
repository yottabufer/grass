from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey


class Task(BaseModel):
    """
    Модель для работы с задачами, а конкретно для валидации при создании в методе create_task менеджера TaskManager
    """
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime
