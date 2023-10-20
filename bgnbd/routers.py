from fastapi import APIRouter, HTTPException
from model import BGNBD

router = APIRouter()


@router.get("/predict/")
async def calc_bgnbd(t: float, frequency: int, recency: int, T: float) -> dict:  # pylint: disable=invalid-name
    """
    Predicts the expected number of purchases for t periods, given customer's statistics
    More about the model nomenclature: https://lifetimes.readthedocs.io/en/latest/Quickstart.html#the-shape-of-your-data
    """
    if not (t > 0 and frequency > 0 and recency > 0 and T > 0):
        raise HTTPException(status_code=404, detail="All parameters should be positive")

    return {"number_of_purchases": BGNBD.conditional_expected_number_of_purchases_up_to_time(t, frequency, recency, T)}
