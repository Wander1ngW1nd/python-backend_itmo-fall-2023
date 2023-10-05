from contracts import DeliveryOrder
from fastapi import APIRouter
from utils import calc_delivery_price

router = APIRouter()


@router.post("/calculate_delivery_price")
async def calculate_delivery_price(order: DeliveryOrder) -> dict:
    return {"delivery_price": calc_delivery_price(order.city_from, order.city_to, order.parcel_type)}
