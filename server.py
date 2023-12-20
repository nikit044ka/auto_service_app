import fastapi
import settings
import uvicorn
from src.server.advanced_import import *
from src.server.router import routers


app = fastapi.FastAPI(title='Auto Service API', version='Omega 0.1', description='The best auto service in the world')

[app.include_router(router) for router in routers]


@app.get(path='/', response_model=dict)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


def start_server() -> None:
    uvicorn.run(app='server:app', host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    start_server()