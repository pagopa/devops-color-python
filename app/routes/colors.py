from fastapi import APIRouter
import requests
import logging

colors = APIRouter()


@colors.get("/")
async def home():
    return {"message": "home of colors"}


@colors.get("/dapr/http")
async def random_color():
    """
    return random color
    """
    r = requests.get('http://localhost:3500/v1.0/invoke/backend/method/color')
    logging.info(r)
    return {"random color": f'${r}'}



