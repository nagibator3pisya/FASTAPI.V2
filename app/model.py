import datetime
import enum

from sqlalchemy import String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.DataBase import Base


class User(Base):
    __tablename__ = 'user'
    email :Mapped[str] = mapped_column(String(20), unique=True, index=True)
    username:Mapped[str] = mapped_column(String(20), unique=True, index=True)
    #  хэшированный пароль пользователя. Важно: мы никогда не храним пароли в открытом виде!
    #  Пароли всегда хэшируются перед сохранением в базу данных.
    hashed_password:Mapped[str] =  mapped_column(String(128))
    is_active:Mapped[bool]= mapped_column(Boolean, default=True)

    task = relationship('Task',back_populates='owner',lazy='select')



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
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    owner = relationship("User", back_populates="task")










