from datetime import datetime, timedelta
from http.client import HTTPException

from fastapi.params import Depends
from sqlalchemy import select,or_
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import TaskCreate, TaskUpdate, TaskUpdateStatus, TastUpdatepriority, UserCreate
from app.model import Task, User
from demo.aut import get_current_active_user


async def check_upcoming_deadlines(session:AsyncSession):
    now = datetime.now()
    soon = now + timedelta(hours=2)


    result = await session.execute(
        select(Task).where(
            Task.deadline != None,
            Task.deadline <= soon,
            Task.status == False))
    tasks = result.scalars().all()
    print(f"Найдено задач: {len(tasks)}")

    for task in tasks:
        print(f"{task.id} | {task.title} | deadline: {task.deadline} | status: {task.status}")





async def get_task_first(session:AsyncSession,task_id:int,current_user: User = Depends(get_current_active_user)):

    # result = await session.execute(select(Task).filter(Task.id == task_id))
    # return result.scalars().first()
    stmt = select(Task).where(Task.id == task_id, Task.owner_id == current_user.id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_task_all(session:AsyncSession,current_user: User = Depends(get_current_active_user)):
    result = await session.execute(select(Task).filter(Task.owner_id == current_user.id))
    return result.scalars().all()


async  def create_task(session:AsyncSession, task:TaskCreate,current_user: User = Depends(get_current_active_user)):
    result =Task(**task.model_dump(),owner_id= current_user.id)
    session.add(result)
    await session.commit()
    await session.refresh(result)
    return result


async def update_task(task_id: int,task_data: TaskUpdate,session:AsyncSession):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task =result.scalar_one_or_none()

    if not task:
        return None

    for k,v in task_data.model_dump().items():
        setattr(task,k,v)
    await session.commit()
    await session.refresh(task)
    return task


async def delete_task(task_id: int, session: AsyncSession):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        return None

    await session.delete(task)
    await session.commit()
    return {"detail": "Задача удалена"}


async def update_task_status(task_id: int,status: TaskUpdateStatus,session:AsyncSession):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task =result.scalar_one_or_none()

    if not task:
        return None

    task.status = status
    await session.commit()
    await session.refresh(task)
    return task


async def update_task_priority(task_id: int,priority: TastUpdatepriority,session:AsyncSession):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task =result.scalar_one_or_none()

    if not task:
        return None

    task.priority = priority
    await session.commit()
    await session.refresh(task)
    return task

# User.email == user.email
async def filter_user_scuses(session:AsyncSession,user: UserCreate):
    stmt = select(User).filter(
        or_(
            User.email == user.email,
            User.username == user.username
        )
    )
    result = await session.execute(stmt)
    return  result.scalars().first()

# поиска пользователя по username
async def get_user_by_username(session: AsyncSession, username: str):
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    return result.scalars().first()
