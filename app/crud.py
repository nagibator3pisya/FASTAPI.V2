from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import service
from app.deps import get_db
from app.schemas import TaskCreate

user_router = APIRouter()

@user_router.post('/task/')
async def creat_task(task_id: TaskCreate,session:AsyncSession = Depends(get_db)):
    return await service.create_task(session=session,task=task_id)