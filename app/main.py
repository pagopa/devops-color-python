from fastapi import FastAPI
from app.routes.colors import colors
from app.routes.status import status_route


def include_router(app):
    app.include_router(colors, prefix='/colors')
    app.include_router(status_route, prefix='/status')


def configure_application(app):
    include_router(app)
    return app


app = FastAPI()


@app.get("/")
async def home_root():
    return {"home_root": "ok"}


configure_application(app)

