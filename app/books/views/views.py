from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.books.Service.Dependency import get_session
from app.books.Service.service import create_autor, get_autor_by_id, get_autor_by_all, get_autor_by_del, \
    get_autor_by_update, get_autor_with_books
from app.books.schemas.Schemas import AutorCreate, AutorUpdate, AutorBase

router_autors_and_books = APIRouter(tags=['autors'],prefix='/autors')

@router_autors_and_books.post('/')
async def create_autors(autor:AutorCreate, session:AsyncSession = Depends(get_session)):
    autors = await create_autor(session=session,autor=autor)
    return autors


@router_autors_and_books.get('/{autors_id}')
async def autor_by_id(autor_id:int, session: AsyncSession = Depends(get_session)):
    autor_by = await get_autor_by_id(session=session,autor_id=autor_id)
    if autor_by is None:
        raise HTTPException(status_code=404,detail='Автора нет')
    return autor_by


@router_autors_and_books.get('/')
async def autor_all(session: AsyncSession = Depends(get_session)):
    authors = await get_autor_by_all(session)
    return authors

@router_autors_and_books.put('/{autor_id}/')
async def update_autor(
        autor_data:AutorUpdate,
        autor_id: int,
        session:AsyncSession = Depends(get_session)):

    update_autors = await get_autor_by_update(session=session,autor_id=autor_id,author_data=autor_data)
    if update_autors is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return update_autors

@router_autors_and_books.delete('/{autors_id}/')
async def autor_delete(autor_id:int,session:AsyncSession = Depends(get_session)):
    delet_autor = await get_autor_by_del(session=session,autor_id=autor_id)
    if delet_autor is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return delet_autor





@router_autors_and_books.get("/{author_id}/")
async def read_author(author_id: int, session: AsyncSession = Depends(get_session)):
    author = await get_autor_with_books(session=session, autor_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author



