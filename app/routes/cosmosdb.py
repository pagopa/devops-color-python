from fastapi import APIRouter
import logging
from dapr.clients import DaprClient

cosmosdb = APIRouter()


@cosmosdb.get("/")
async def home():
    return {"message": "home of cosmosdb"}


@cosmosdb.post("/dapr/sdk")
def dapr_sdk_cosmosdb():
    """
    return random cosmosdb with a sdk request to dapr
    """
    with DaprClient() as daprClient:
        result = daprClient.save_state("cosmosdb", [
            {
                "key": "order_1",
                "value": 1
            },
            {
                "key": "order_2",
                "value": 2
            }
        ])

    cosmosdb = result.data.decode("utf-8")

    logging.info(str(cosmosdb))
    return {"random cosmosdb": f'{str(cosmosdb)}'}



