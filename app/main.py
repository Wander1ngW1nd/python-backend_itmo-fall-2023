import uvicorn
from fastapi import FastAPI
from routers import router

app: FastAPI = FastAPI(
    title="Delivery price calculator",
    description=("Simple delivery price calculator"),
    version="0.0.1",
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
