from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.schemas import TaskCreate
from model import Task

async def get_task_first(session:AsyncSession,task_id:int):
    result = await session.execute(select(Task).filter_by(Task.id == task_id))
    return result.scalars().first()

async def get_task_all(session:AsyncSession,task_id:int):
    result = await session.execute(select(Task).filter_by(Task.id == task_id))
    return result.scalars().all()

async  def create_task(session:AsyncSession, task:TaskCreate):
    result =Task(**task.model_dump())
    session.add(result)
    await session.commit()
    return result


