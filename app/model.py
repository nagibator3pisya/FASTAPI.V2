from typing import Optional

from pydantic import BaseModel,Field



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


address = Address(country='Россия',city='Москва')
user = User(name='Саша',age=3,address=[address])

print(user.model_dump())

