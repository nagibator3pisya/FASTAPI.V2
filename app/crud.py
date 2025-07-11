from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import service
from app.deps import get_db
from app.schemas import TaskCreate, TaskUpdate

user_router = APIRouter(tags=['task'],prefix='/task')

@user_router.post('/')
async def creat_task(task_id: TaskCreate,session:AsyncSession = Depends(get_db)):
    return await service.create_task(session=session,task=task_id)


@user_router.get('/{task_id}/')
async def read_task_first(task_id:int,session:AsyncSession = Depends(get_db)):
    result = await service.get_task_first(session=session,task_id=task_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Такой задачи нет')
    return result


@user_router.get('/all')
async def read_tasks_all(session:AsyncSession = Depends(get_db)):
    result = await service.get_task_all(session=session)
    if result is None:
        raise HTTPException(status_code=404, detail='Нет задач')
    return result


@user_router.put('/update/{task_id}/')
async def read_task_update(task_id: int,task_data: TaskUpdate,session:AsyncSession = Depends(get_db)):
    update = await service.update_task(task_id=task_id,task_data=task_data,session=session)
    if update is None:
        raise HTTPException(status_code=404, detail='Нет задач')
    return update


@user_router.delete("/delete/{task_id}/")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_db)):
    result = await service.delete_task(task_id=task_id, session=session)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result

