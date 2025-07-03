from sqlalchemy.ext.asyncio import AsyncSession

from app.config.config import async_session_maker


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session