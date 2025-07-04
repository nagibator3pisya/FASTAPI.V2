import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
"""
GET (получение данных) -> read

POST (добавление данных) - create

PUT (изменение данных) - update

DELETE (удаление данных) - delete
"""

# Query-параметры http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/")
async def root(name:str,age:int):
    return {"message": f"Hello {name},age {age}"}


# отличие между auery параметрами и body параметрами
@app.post("/")
async def root(name:str,age:int):
    return {"message": f"Hello {name},age {age}"}


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)