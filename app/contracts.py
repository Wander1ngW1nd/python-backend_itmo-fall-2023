from pydantic import BaseModel


class DeliveryOrder(BaseModel):
    """Defines simple model of delivery order"""

    city_from: str
    city_to: str
    parcel_type: str
