from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from app import service
from app.deps import get_db
from app.model import User
from app.schemas import TaskCreate, TaskUpdate, TaskUpdateStatus, TastUpdatepriority, Task
from demo.aut import get_current_active_user

user_router = APIRouter(tags=['task'],prefix='/task')





@user_router.post('/')
async def creat_task(task_id: TaskCreate,session:AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    return await service.create_task(session=session,task=task_id,current_user=current_user)


@user_router.get('/{task_id}/')
async def read_task_first(task_id: int, session: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    result = await service.get_task_first(session=session, task_id=task_id,current_user=current_user)
    if result is None:
        raise HTTPException(status_code=404, detail='Такой задачи нет')
    return result


@user_router.get('/all')
async def read_tasks_all(session:AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    result = await service.get_task_all(session=session,current_user=current_user)
    if result is None:
        raise HTTPException(status_code=404, detail='Нет задач')
    return result


@user_router.put('/update/{task_id}/')
async def read_task_update(task_id: int,task_data: TaskUpdate,session:AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    update = await service.update_task(task_id=task_id,task_data=task_data,session=session,current_user=current_user)
    if update is None:
        raise HTTPException(status_code=404, detail='Нет задач')
    return update


@user_router.delete("/delete/{task_id}/")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user)):
    result = await service.delete_task(task_id=task_id, session=session,current_user=current_user)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result




@user_router.patch('/{task_id}/status_update')
async def update(task_id: int, task_data_status :TaskUpdateStatus ,session: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    result =await service.update_task_status(task_id=task_id,status=task_data_status.status,session=session,current_user=current_user)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result


@user_router.patch('/{task_id}/priority')
async def update_priority(task_id: int, task_data_priority :TastUpdatepriority ,session: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_active_user) ):
    result =await service.update_task_priority(task_id=task_id,priority=task_data_priority.priority,session=session,current_user=current_user)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result