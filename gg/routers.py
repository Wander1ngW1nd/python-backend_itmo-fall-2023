from fastapi import APIRouter, HTTPException
from model import GG

router = APIRouter()


@router.get("/predict/")
async def calc_gg(frequency: int, monetary_value: float) -> dict:  # pylint: disable=invalid-name
    """
    Predicts the expected average profit of one customer's purchase, given their statistics
    More about the model nomenclature: https://lifetimes.readthedocs.io/en/latest/Quickstart.html#the-shape-of-your-data
    """
    if not (frequency > 0 and monetary_value > 0):
        raise HTTPException(status_code=404, detail="All parameters should be positive")

    return {"average_profit": GG.conditional_expected_average_profit(frequency, monetary_value)}
