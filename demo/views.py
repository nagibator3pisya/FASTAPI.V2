import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])


httpbasic = HTTPBasic()

# Аутентификация — это процесс проверки подлинности пользователя
@routers_auts.get('/basic-auth/')
def demo_auth(
        credentials: Annotated[HTTPBasicCredentials, Depends(httpbasic)]
):
   return {
       'message': 'hi',
       'user_name':credentials.username,
       'password': credentials.password
   }


user = {
    'admin': 'admin',
    'join': ' password'
}

@routers_auts.get('/basic-auth/')
def get_auth_user(
        credentials: Annotated[HTTPBasicCredentials, Depends(httpbasic)]
):
  unated = HTTPException(
      status_code =status.HTTP_401_UNAUTHORIZED,
      detail='Invalid username or password',
      headers = {'WWW-Authenticate':'Basic'}
  )
  correst_password = user.get(credentials)
  # if credentials.username not in user:
  #     raise unated
  # if not secrets.compare_digest(
  #         credentials.password.encode('utf-8')
  # ):
  #     raise unated





# проверка юзера
@routers_auts.get('/some-http-header-auth/')
def demo_auth_username(
        username: str = Depends()
):
   return {
       'message': F'hi {username}',
       'user_name':username,
   }


















