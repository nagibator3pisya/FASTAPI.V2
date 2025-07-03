from typing import List

from pydantic import BaseModel

class AutorBase(BaseModel):
    first_name: str
    last_name: str

class AutorCreate(AutorBase):
    pass





class AutorUpdate(AutorBase):
    pass









class BookBase(BaseModel):
    id: int
    autor: AutorBase
    name: str
    title: str
    body: str
    autor_id: int

class Autor_Boks(AutorBase):
    id: int
    books: List[BookBase] = []

    class Config:
        from_attributes = True



class BookCreate(BookBase):
    author_id: int

class Book_Autor(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True

class BookUpdate(BookBase):
    pass

