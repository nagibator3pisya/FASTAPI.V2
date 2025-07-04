import uvicorn
from fastapi import FastAPI


app = FastAPI()
"""
GET (получение данных) -> read

POST (добавление данных) - create

PUT (изменение данных) - update

DELETE (удаление данных) - delete
"""


@app.get("/")
async def root(name:str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)