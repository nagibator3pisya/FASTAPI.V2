import asyncio

from contextlib import asynccontextmanager
from typing import Union
import uvicorn
from fastapi import FastAPI
from app.background_tasks import reminder_worker
from app.crud import user_router
from demo.views import routers_auts


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(reminder_worker())
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(routers_auts)





"""
GET (получение данных) -> read

POST (добавление данных) - create

PUT (изменение данных) - update

DELETE (удаление данных) - delete
"""




if __name__ == '__main__':
    uvicorn.run("app.main:app", reload=True)
