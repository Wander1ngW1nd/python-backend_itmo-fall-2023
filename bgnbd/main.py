from fastapi import FastAPI
from routers import router

app: FastAPI = FastAPI(
    title="BG-NBD model",
    description=("BG-NBD model for predicting number of purchases"),
    version="0.0.1",
)

app.include_router(router)
