from fastapi import APIRouter

colors = APIRouter()


@colors.get("/")
async def home():
    return {"message": "home of colors"}


@colors.get("/random")
async def random_color():
    """
    return random color
    """
    return {"random color": "ok"}
