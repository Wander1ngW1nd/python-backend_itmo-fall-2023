import os

from fastapi import HTTPException
from lifetimes import GammaGammaFitter

if not os.environ.get("MODEL_PATH"):
    raise HTTPException(status_code=404, detail="Environment does not contain MODEL_PATH")

GG = GammaGammaFitter()
GG.load_model(os.environ["MODEL_PATH"])
