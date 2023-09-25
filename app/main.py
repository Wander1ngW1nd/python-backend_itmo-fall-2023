from fastapi import FastAPI
from routers import router

app: FastAPI = FastAPI(
    title="HelloWorldApp",
    description=("HelloWorldApp to get started with FastAPI"),
    version="0.0.1",
)

app.include_router(router)
