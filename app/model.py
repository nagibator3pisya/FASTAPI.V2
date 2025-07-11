from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped,mapped_column

from config.DataBase import Base




class Task(Base):
    __tablename__ = 'task'

    title:Mapped[str] = mapped_column(String(20))
    description:Mapped[str] = mapped_column(String(500))
    status:Mapped[str] = mapped_column(Boolean, default=False)
