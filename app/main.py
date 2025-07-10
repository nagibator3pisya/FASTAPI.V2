from typing import Union

import uvicorn
from fastapi import FastAPI

from app.crud import user_router

app = FastAPI()

app.include_router(user_router)




"""
GET (получение данных) -> read

POST (добавление данных) - create

PUT (изменение данных) - update

DELETE (удаление данных) - delete
"""




if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)