from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Car, database_model=database_models.Car, prefix='/car', tags=['Cars']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Customer, database_model=database_models.Customer, prefix='/customer', tags=['Customers']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Order, database_model=database_models.Order, prefix='/order', tags=['Orders']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Service, database_model=database_models.Service, prefix='/service', tags=['Services']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Part, database_model=database_models.Part, prefix='/part', tags=['Parts']).fastapi_router
)
