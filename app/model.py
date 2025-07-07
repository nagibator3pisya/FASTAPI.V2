from typing import Optional

from pydantic import BaseModel



class Phone(BaseModel):
    phone: int




class Address(BaseModel):
    country: str
    city : str
    phones: Phone # 1 адрес может иметь 1 телефон

class User(BaseModel):
    name:str
    age: int
    description: Optional[str] = None # не обязательный параметр
    address: Optional[list[Address]] =  None # связь с адресом


address = Address(country='Россия',city='Москва')
user = User(name='Саша',age=22,address=[address])

print(user.model_dump())

