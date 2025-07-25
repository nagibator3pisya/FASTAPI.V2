import secrets

from typing import Annotated, Any

from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.schemas import UserLoginSchema
from authx import AuthXConfig, AuthX
from fastapi import APIRouter, HTTPException, security, Depends

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])

# базовая
security = HTTPBasic()


@routers_auts.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}

















