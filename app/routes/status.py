from fastapi import APIRouter

status_route = APIRouter()


@status_route.get("/")
async def status():
    return {"status": "ok"}
