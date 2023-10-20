import os

from fastapi import HTTPException
from lifetimes import ModifiedBetaGeoFitter

if not os.environ.get("MODEL_PATH"):
    raise HTTPException(status_code=404, detail="Environment does not contain MODEL_PATH")

BGNBD = ModifiedBetaGeoFitter()
BGNBD.load_model(os.environ["MODEL_PATH"])
