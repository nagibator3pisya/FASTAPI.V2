import asyncio

from app.service import check_upcoming_deadlines
from config.config import async_session_maker


# async def reminder_worker():
#     while True:
#         print("Фоновая задача работает!")
#         async with async_session_maker() as sess:
#             await check_upcoming_deadlines(sess)
#         await asyncio.sleep(60*1)
