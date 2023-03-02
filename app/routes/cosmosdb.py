from fastapi import APIRouter
import logging
from dapr.clients import DaprClient
from python_random_strings import random_strings
import uuid


cosmosdb = APIRouter()


@cosmosdb.get("/")
async def home():
    return {"message": "home of cosmosdb"}


@cosmosdb.get("/dapr/sdk")
def dapr_sdk_cosmosdb():
    """
    create random value in cosmosdb with a sdk
    """
    with DaprClient() as daprClient:
        result = daprClient.save_state(store_name="cosmosdb", key=random_strings.random_lowercase(6), value=uuid.uuid4())

    return {"random string": f'{result}'}



