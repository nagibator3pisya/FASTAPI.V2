import uvicorn
from fastapi import FastAPI

from app.books.views.views import router_autors_and_books

app = FastAPI()

app.include_router(router_autors_and_books)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)