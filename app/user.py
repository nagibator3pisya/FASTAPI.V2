from fastapi import APIRouter

from app.model import User, UserOut, UserIn

user_router = APIRouter(prefix='/users',tags=['users'])

"""
GET (получение данных) -> read

POST (добавление данных) - create

PUT (изменение данных) - update

DELETE (удаление данных) - delete
"""

@user_router.post('/user/',response_model=UserOut)
async def create(user: UserIn):
    return user










# Получение данных
@user_router.get('/{user_id}')
async def get_user(user_id: int) -> dict:
    return {"message": f"Получил данные {user_id}"}


# Добавление данных
@user_router.post('/')
async def create_user(user: User) -> dict:
    return {"message": f"Добавил данные {user.name}"}


# Удаление данных
@user_router.delete('/{user_id}')
async def delete_user(user_id: int) -> dict:
    return {"message": f"Удален {user_id}"}


# Изменение данных
@user_router.put('/{user_id}')
async def update_user(user_id: int, user: User) -> dict:
    return {"message": f"Изменено {user_id}, новое имя: {user.name}"}
