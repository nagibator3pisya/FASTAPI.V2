import secrets

from typing import Annotated, Any

import jwt
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from jose import JWTError

from app.schemas import UserLoginSchema

from fastapi import APIRouter, HTTPException, security, Depends,status

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])





















