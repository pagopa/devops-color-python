from fastapi import APIRouter
import requests
import logging

color = APIRouter()


@color.get("/")
async def home():
    return {"message": "home of color"}


@color.get("/dapr/http")
async def random_color():
    """
    return random color with a raw http request to dapr
    """
    r = requests.get('http://localhost:3500/v1.0/invoke/backend/method/color')
    color = r.text
    logging.info(r)
    return {"random color": f'${color}'}



