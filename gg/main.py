from fastapi import FastAPI
from routers import router

app: FastAPI = FastAPI(
    title="Gamma-Gamma model",
    description=("Gamma-Gamma model for predicting average profit of purchase"),
    version="0.0.1",
)

app.include_router(router)
