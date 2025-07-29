from sqlalchemy.orm import Session


from fastapi import APIRouter, HTTPException, security, Depends,status

from app.deps import get_db
from app.model import User
from app.schemas import UserCreate
from app.service import filter_user_scuses
from demo.aut import get_password_hash

routers_auts = APIRouter(prefix='/demo-auth',tags=['demo-auth'])

@routers_auts.post('/register',response_class=UserCreate)
async  def register(user: UserCreate, session:Session = Depends(get_db)):
    users = await filter_user_scuses(user=user,session=session)
    if users:
        if users.email == user.email:
            raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
        if users.username == user.username:
            raise HTTPException(status_code=400, detail="Имя пользователя уже занято")
    hashed_password = get_password_hash(user.password)
    session_users = User(
        email = user.email,
        username = user.username,
        hashed_password = hashed_password
    )
    session.add(session_users)
    session.commit()
    session.refresh(session_users)
    return session_users

























