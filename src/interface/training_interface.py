from typing import Optional
from pydantic import BaseModel


class TrainingRequest(BaseModel):
    host: str
    sql: Optional[str] = None
    question: Optional[str] = None
    ddl: Optional[str] = None
    doc: Optional[str] = None


class TrainingMessagePackage(BaseModel):
    host: str
    package: TrainingRequest
