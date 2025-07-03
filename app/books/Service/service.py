from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.books.schemas.Schemas import AutorCreate, Book, BookCreate, AutorUpdate

from app.books.model.models import Autor,Books

async def create_autor(session:AsyncSession,autor: AutorCreate):
    db_autor = Autor(**autor.model_dump())
    session.add(db_autor)
    await session.commit()
    await session.refresh(db_autor)
    return db_autor

async def get_autor_by_id(session:AsyncSession,autor_id:int):
    # взять по id
    result = await session.execute(select(Autor).filter(Autor.id == autor_id))
    return result.scalars().first()


async def get_autor_by_all(session:AsyncSession):
    # извлекает список авторов из базы данных с поддержкой пагинации
    result = await session.execute(select(Autor))
    return result.scalars().all()


async def get_autor_by_del(autor_id:int,session:AsyncSession):
    result = await session.execute(select(Autor).filter(Autor.id == autor_id))
    delet = result.scalars().first()
    if delet:
        await session.delete(delet)
        await session.commit()
    return delet



async def get_autor_by_update(autor_id:int,session:AsyncSession,author_data:AutorUpdate)->Autor:
    result = await session.execute(select(Autor).filter(Autor.id == autor_id))
    update_autor = result.scalars().first()
    if update_autor:
        for k,v in author_data.model_dump().items():
            setattr(update_autor,k,v)

        await session.commit()
        await session.refresh(update_autor)

    return update_autor





# книгии
async def create_book(db: AsyncSession, book: BookCreate):
    db_book = Books(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Books).filter(Book.id == book_id))
    return result.scalars().first()

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Books).offset(skip).limit(limit))
    return result.scalars().all()