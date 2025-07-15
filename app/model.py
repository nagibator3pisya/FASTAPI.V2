import datetime
import enum

from sqlalchemy import String, Boolean, DateTime, Enum
from sqlalchemy.orm import Mapped,mapped_column

from config.DataBase import Base

class TaskPriority(enum.Enum):
    high = "высокая важность"
    medium = "средняя"
    low = "низкая"


class Task(Base):
    __tablename__ = 'task'

    title:Mapped[str] = mapped_column(String(20))
    description:Mapped[str] = mapped_column(String(500))
    status:Mapped[str] = mapped_column(Boolean, default=False)
    deadline: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), nullable=False, default=TaskPriority.medium)
