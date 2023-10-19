FROM python:3.10.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install fastapi==0.103.1 lifetimes==0.11.3 uvicorn==0.23.2 \
    && rm -rf /root/.cache/pip

COPY . /app/
