from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from app.config import Base

class Autor(Base):
    __tablename__ = 'autors'

    first_name : Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(20))
    books: Mapped[list['Books']] = relationship(back_populates='autor')


class Books(Base):
    __tablename__ = 'books'

    name: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    body: Mapped[str] = mapped_column(String(50))

    autor: Mapped["Autor"] = relationship(back_populates="books")
    autor_id : Mapped[int] = mapped_column(ForeignKey("autors.id"))








