from enum import Enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class TaskPriority(str,Enum):
    high = "high"
    medium = "medium"
    low = "low"




class TaskBase(BaseModel):
    title:str
    description:str | None
    status:bool | None
    deadline:datetime



    class Config:
        from_attributes = True


# Cхема для создания задачи
class TaskCreate(TaskBase):
    title: str
    description: str | None
    status: bool = False
    deadline: datetime
    priority: TaskPriority

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


class TastUpdatepriority(BaseModel):
    priority: TaskPriority

class UserLoginSchema(BaseModel):
    name: str
    password: str
