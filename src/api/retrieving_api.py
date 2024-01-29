import requests
from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

from ..client import *


router = APIRouter()


class RetrievingQueryRequest(BaseModel):
    vector_db_host: str
    llm_api_key: str
    question: str


class RetrievingQueryMessage(BaseModel):
    consumer_host: str
    package: RetrievingQueryRequest


class RetrievingQueryResponse(BaseModel):
    sql: str


@router.post("/retreive_query", response_model=RetrievingQueryResponse)
def get_results(request: RetrievingQueryMessage) -> RetrievingQueryResponse:
    logger.info(f"Retrieving query with request: {request}")

    try:
        response = requests.post(f"{request.consumer_host}/retreive_query", data=request.package.model_dump_json())
        response.raise_for_status()

        return RetrievingQueryResponse(sql=response.json()["sql"])

    except Exception as e:
        logger.critical(e)
        raise e
