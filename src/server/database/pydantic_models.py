from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 0

class LoginData(BaseModel):
    password: str
    login: str

class ChangePassword(BaseModel):
    password: str

class User(ModifyBaseModel):
    position: str = ''
    login: str = ''
    password: str = ''
    power_level: int = 0

class Customer(ModifyBaseModel):
    name: str = ''
    address: str = ''
    phone_number: str = ''

class Car(ModifyBaseModel):
    customer_id: int = 0
    make: str = ''
    model: str = ''
    year: int = 0
    vin: str = ''

class Order(ModifyBaseModel):
    customer_id: int = 0
    car_id: int = 0
    date: str = ''
    description: str = ''

class Part(ModifyBaseModel):
    name: str = ''
    price: float = 0.0
    quantity: int = 0

class Service(ModifyBaseModel):
    name: str = ''
    price: float = 0.0