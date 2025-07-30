from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from fastapi import APIRouter, HTTPException, security, Depends,status

from app.deps import get_db
from app.model import User
from app.schemas import UserCreate, User as UserSchema, Token
from app.service import filter_user_scuses, get_user_by_username
from demo.aut import get_password_hash, verify_token, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    get_current_active_user, verify_password

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])



@routers_auts.post('/register/',response_model=UserSchema)
async  def register(user: UserCreate, session:Session = Depends(get_db)):
    db_users = await filter_user_scuses(user=user,session=session)
    if db_users:
        if db_users.email == user.email:
            raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
        if db_users.username == user.username:
            raise HTTPException(status_code=400, detail="Имя пользователя уже занято")
    hashed_password = get_password_hash(user.password)
    session_users = User(
        email = user.email,
        username = user.username,
        hashed_password = hashed_password
    )
    session.add(session_users)
    await session.commit()
    await session.refresh(session_users)
    return session_users



@routers_auts.post('/token/', response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
):
    '''
    эндпоинт для получения JWT токена. Использует стандартную форму OAuth2 для получения логина и пароля. Процесс аутентификации
    :param form_data:
    :param session:
    :return:
    '''
#аутентификация пользователя
    users = await  get_user_by_username(session,form_data.username)
    if not users or not verify_password(form_data.password,users.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # создание токена доступа
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub':users.username},expires_delta=access_token_expires
    )
    return {'access_token':access_token,"token_type":'bearer'}





@routers_auts.get('/users/me',response_model=UserSchema)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
     эндпоинт для получения информации о текущем пользователе. Защищён зависимостью get_current_active_user, которая:

        Извлекает токен из заголовка Authorization
        Проверяет валидность токена
        Находит пользователя в базе данных
        Проверяет активность пользователя
        Возвращает информацию о пользователе
    :param current_user:
    :return:
    """
    return current_user



@routers_auts.get('/protected')
async def protected(current_user: User = Depends(get_current_active_user)):
    return {"message":f'Привет {current_user.username}, это защищённый маршрут'}



















