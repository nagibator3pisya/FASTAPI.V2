import secrets
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import HTTPBasic,HTTPBasicCredentials

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])




static_auth_token_to_username= {
    'f438578fd7b885f11acdafdb411cdb3c7644f38442bf26aca71d26a92fe37aec': 'admin',
    'e448cbf29162c6941d6a251bb13c2d4d330a7e981a4e42c41a4e37b2385f58c5': ' jon'
}


def get_user_by_static_auth_token(
        statik_token: str = Header(alias='x-auth-token'),
):
    if username := static_auth_token_to_username.get(statik_token):
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='token invalid'
    )




# проверка юзера если не верное то не попадаем
@routers_auts.get('/some-http-header-auth/')
def demo_auth_some_http_header(
        username: str = Depends(get_user_by_static_auth_token)
):
   return {
       'message': F'hi {username}',
       'user_name':username,
   }


















