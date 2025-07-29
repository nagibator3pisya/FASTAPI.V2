from enum import Enum
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr


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
    priority: TaskPriority
    owner: Optional["User"]  # ← ссылка на пользователя

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






class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active:bool
    tasks: Optional[List[Task]] = []  # ← список задач



    class Config:
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str]= None

# Чтобы избежать циклического импорта
Task.model_rebuild()
User.model_rebuild()