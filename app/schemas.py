from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskBase(BaseModel):
    title:str
    description:str | None
    status:bool | None
    deadline:Optional[datetime] = None

# Cхема для создания задачи
class TaskCreate(TaskBase):
    title: str
    description: str | None
    status: bool = False


# Схема для отображения задачи
class Task(TaskBase):
    id: int

    class Config:
        from_orm = True


class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


# для обновления только статуса
class TaskUpdateStatus(BaseModel):
    status : bool


