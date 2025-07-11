from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.schemas import TaskCreate, TaskUpdate, TaskUpdateStatus
from model import Task

async def get_task_first(session:AsyncSession,task_id:int):
    result = await session.execute(select(Task).filter(Task.id == task_id))
    return result.scalars().first()

async def get_task_all(session:AsyncSession):
    result = await session.execute(select(Task).filter(Task.id))
    return result.scalars().all()


async  def create_task(session:AsyncSession, task:TaskCreate):
    result =Task(**task.model_dump())
    session.add(result)
    await session.commit()
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