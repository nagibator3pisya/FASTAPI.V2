from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class Phone(BaseModel):
    phone:  Optional[int] = None




class Address(BaseModel):
    country: str
    city : str
    # phones: Phone # 1 адрес может иметь 1 телефон

class User(BaseModel):
    name:str = Field(min_length=1)
    age: int = Field(gt=1, lt=100)
    description: Optional[str] = None # не обязательный параметр
    address: Optional[list[Address]] =  None # связь с адресом





class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None