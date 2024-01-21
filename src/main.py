from fastapi import FastAPI

from api import training_api


app = FastAPI()

app.include_router(training_api.router)
