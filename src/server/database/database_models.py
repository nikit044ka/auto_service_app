from peewee import *
import peewee
import settings

db = peewee.SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Customer(BaseModel):
    customer_id = AutoField(default=0)
    name = CharField(default='')
    address = CharField(default='')
    phone_number = CharField(default='')

class Car(BaseModel):
    car_id = AutoField(default=0)
    customer_id = ForeignKeyField(Customer, backref='cars', default=0)
    make = CharField(default='')
    model = CharField(default='')
    year = IntegerField(default=0)
    vin = CharField(default='')

class Order(BaseModel):
    order_id = AutoField(default=0)
    customer_id = ForeignKeyField(Customer, backref='orders', default=0)
    car_id = ForeignKeyField(Car, backref='orders', default=0)
    date = DateField(default='')
    description = TextField(default='')

class Part(BaseModel):
    part_id = AutoField(default=0)
    name = CharField(default='')
    price = DecimalField(decimal_places=2, default=0.0)
    quantity = IntegerField(default=0)

class Service(BaseModel):
    service_id = AutoField(default=0)
    name = CharField(default='')
    price = DecimalField(decimal_places=2, default=0.0)

db.create_tables([User, Customer, Car, Order, Part, Service])