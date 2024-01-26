import requests
from fastapi import APIRouter, Response, status
from loguru import logger
from pydantic import BaseModel

from ..client import *


router = APIRouter()


class RetrievingQueryRequest(BaseModel):
    host: str
    key: str
    question: str


class RetrievingQueryMessage(BaseModel):
    host: str
    package: RetrievingQueryRequest


class RetrievingQueryResponse(BaseModel):
    sql: str


@router.post("/retreive_query", response_model=RetrievingQueryResponse)
def get_results(request: RetrievingQueryMessage) -> RetrievingQueryResponse:
    logger.info(f"Retrieving query with request: {request}")

    try:
        response = requests.post(f"{request.host}/retreive_query", data=request.package.model_dump_json())
        response.raise_for_status()

        return RetrievingQueryResponse(sql=response.json()["sql"])

    except Exception as e:
        logger.critical(e)
        raise e
