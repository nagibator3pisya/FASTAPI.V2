from pydantic import BaseModel


class TaskBase(BaseModel):
    title:str
    description:str | None
    completed:bool | None

# Cхема для создания задачи
class TaskCreate(TaskBase):
    pass

# Схема для отображения задачи
class Task(TaskBase):
    id: int

    class Config:
        from_orm = True