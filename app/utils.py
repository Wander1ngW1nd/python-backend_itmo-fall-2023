from database.cities_db import CITIES_DB_URL, CitiesDB
from fastapi import HTTPException
from geopy.distance import geodesic
from parcels import Box, Envelope, Tovarnyak
from sqlalchemy.engine import Engine, create_engine


def get_city_id(city_name: str) -> int:
    engine: Engine = create_engine(CITIES_DB_URL)
    with CitiesDB(engine) as cities_db:  # type: ignore
        city_id = cities_db.get_ids_by_name(city_name)

    # check that such city exists, and it is unique
    if len(city_id) == 0:
        raise HTTPException(status_code=404, detail=f"City {city_name} not found")
    if len(city_id) > 1:
        raise HTTPException(status_code=404, detail=f"Multiple cities called {city_name} found")
    return city_id[0]


def calc_distance(name1: str, name2: str) -> float:
    """Calculate distance between cities"""

    # get city ids from database
    id1 = get_city_id(name1)
    id2 = get_city_id(name2)

    # get cities coordinates by their ids
    engine: Engine = create_engine(CITIES_DB_URL)
    with CitiesDB(engine) as cities_db:  # type: ignore
        city1_coords: dict[str, float] = cities_db.get_coordinates_by_id(id1)
        city2_coords: dict[str, float] = cities_db.get_coordinates_by_id(id2)

    # calculate distance in kilometers
    distance: float = geodesic(city1_coords.values(), city2_coords.values()).km

    # return distance in kilometers, adjusted for roads length
    return round(distance * 1.1, 2)


def calc_tariff(parcel_type: str) -> float:
    """Returns delivery tariff for provided parcel type"""
    parcel_types = {"envelope": Envelope, "box": Box, "tovarnyak": Tovarnyak}
    if parcel_type in parcel_types:
        return parcel_types[parcel_type]().calc_tariff()  # type: ignore
    raise HTTPException(status_code=404, detail="Unknown parcel type")


def calc_delivery_price(city_from: str, city_to: str, parcel_type: str) -> float:
    """Calculates delivery price based on distance and parcel type"""
    distance_component = calc_distance(city_from, city_to)
    parcel_component = calc_tariff(parcel_type)
    return round(distance_component + parcel_component, 2)
