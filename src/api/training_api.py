from fastapi import APIRouter, Response, status
from loguru import logger
from pydantic import BaseModel

from ..client import *


router = APIRouter()


class TrainingModelRequest(BaseModel):
    vector_db_host: str
    sql: str | None = None
    question: str | None = None
    ddl: str | None = None
    doc: str | None = None


class TrainingModelMessage(BaseModel):
    consumer_host: str
    package: TrainingModelRequest


@router.post("/train_model")
def train_model(request: TrainingModelMessage) -> Response:
    logger.info(f"Training model with request: {request}")

    try:
        client.send_message(QueueUrl=train_task_queue_url, MessageBody=request.model_dump_json())

        return Response(status_code=status.HTTP_200_OK)

    except Exception as e:
        logger.critical(e)
        raise e
