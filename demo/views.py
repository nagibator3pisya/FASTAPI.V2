from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic,HTTPBasicCredentials
routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])


httpbasic = HTTPBasic()

# Аутентификация — это процесс проверки подлинности пользователя
@routers_auts.get('/basuc-auth/')
def demo_auth(
        credentials: Annotated[HTTPBasicCredentials, Depends(httpbasic)]
):
   return {
       'message': 'hi',
       'user_name':credentials.username,
       'password': credentials.password
   }