from fastapi import APIRouter, Response, status
from loguru import logger

from client import *
from interface import TrainingMessagePackage


router = APIRouter()


@router.post("/train_model")
def train_model(request: TrainingMessagePackage) -> Response:
    logger.info(f"Training model with request: {request}")

    try:
        client.send_message(QueueUrl=train_task_queue_url, MessageBody=request.model_dump_json())

        return Response(status_code=status.HTTP_200_OK)

    except Exception as e:
        logger.critical(e)
        raise e
