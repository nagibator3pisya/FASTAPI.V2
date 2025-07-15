from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse
from fastapi import Request
from app import service
from app.Jinja.utils import templates
from app.deps import get_db

from app.schemas import TaskCreate, TaskUpdate, TaskUpdateStatus, TastUpdatepriority

user_router = APIRouter(tags=['task'],prefix='/task')

@user_router.post('/')
async def creat_task(task_id: TaskCreate,session:AsyncSession = Depends(get_db)):
    return await service.create_task(session=session,task=task_id)


@user_router.get('/html/{task_id}/',response_class=HTMLResponse)
async def read_task_first(task_id:int,request: Request,session:AsyncSession = Depends(get_db)):
    result = await service.get_task_first(session=session,task_id=task_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Такой задачи нет')
    return templates.TemplateResponse('index.html',{'request':request,'result':result})


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




@user_router.patch('/{task_id}/status_update')
async def update(task_id: int, task_data_status :TaskUpdateStatus ,session: AsyncSession = Depends(get_db) ):
    result =await service.update_task_status(task_id=task_id,status=task_data_status.status,session=session)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result


@user_router.patch('/{task_id}/priority')
async def update_priority(task_id: int, task_data_priority :TastUpdatepriority ,session: AsyncSession = Depends(get_db) ):
    result =await service.update_task_status(task_id=task_id,status=task_data_priority.priority,session=session)
    if not result:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return result