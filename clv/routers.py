import os

import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/clv/")
async def calculate_clv(
    t: float, frequency: int, recency: int, T: float, monetary_value: float  # pylint: disable=invalid-name
) -> dict:
    if not os.environ.get("BGNBD_SERVICE_URL"):
        raise HTTPException(status_code=404, detail="Environment does not contain BGNBD_SERVICE_URL")
    if not os.environ.get("GG_SERVICE_URL"):
        raise HTTPException(status_code=404, detail="Environment does not contain GG_SERVICE_URL")

    if not (t > 0 and frequency > 0 and recency > 0 and T > 0 and monetary_value > 0):
        raise HTTPException(status_code=404, detail="All parameters should be positive")

    number_of_purchases: float = httpx.get(
        os.environ["BGNBD_SERVICE_URL"], params={"t": t, "frequency": frequency, "recency": recency, "T": T}
    ).json()["number_of_purchases"]

    average_profit: float = httpx.get(
        os.environ["GG_SERVICE_URL"], params={"frequency": frequency, "monetary_value": monetary_value}
    ).json()["average_profit"]

    return {"clv": number_of_purchases * average_profit}
