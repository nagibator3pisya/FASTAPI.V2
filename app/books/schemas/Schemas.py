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

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

