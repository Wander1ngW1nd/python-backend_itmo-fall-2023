# type: ignore
from fastapi import FastAPI
from routers import router

app: FastAPI = FastAPI(
    title="CLV model",
    description=("Customer Lifetime Value simple calculator"),
    version="0.0.1",
)

app.include_router(router)
