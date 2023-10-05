# type: ignore

import pytest
from fastapi import HTTPException
from utils import calc_delivery_price, calc_distance, calc_tariff, get_city_id


@pytest.mark.unit
@pytest.mark.parametrize("city_name, expected", [("Moscow", 0), ("Saint Petersburg", 1), ("Yekaterinburg", 3)])
def test__get_city_id__should_return_id(city_name: str, expected: int):
    assert get_city_id(city_name) == expected


@pytest.mark.unit
@pytest.mark.parametrize("city_name", ["abobus", "London", "zaratustra"])
def test__get_city_id__should_fail(city_name: str):
    with pytest.raises(HTTPException):
        get_city_id(city_name)


@pytest.mark.unit
@pytest.mark.parametrize(
    "name1, name2, expected",
    [
        ("Moscow", "Saint Petersburg", 700.23),
        ("Saint Petersburg", "Novosibirsk", 3426.16),
        ("Novosibirsk", "Yekaterinburg", 1542.09),
    ],
)
def test__calc_distance(name1: str, name2: str, expected: float):
    assert calc_distance(name1, name2) == expected


@pytest.mark.unit
@pytest.mark.parametrize("parcel_type, expected", [("envelope", 50), ("box", 250), ("tovarnyak", 100500)])
def test__calc_tariff__should_return_tariff(parcel_type: str, expected: float):
    assert calc_tariff(parcel_type) == expected


@pytest.mark.unit
@pytest.mark.parametrize("parcel_type", ["abobus", "London", "zaratustra"])
def test__calc_tariff__should_fail(parcel_type: str):
    with pytest.raises(HTTPException):
        calc_tariff(parcel_type)


@pytest.mark.integration
@pytest.mark.parametrize(
    "name1, name2, parcel_type, expected",
    [
        ("Moscow", "Saint Petersburg", "envelope", 750.23),
        ("Saint Petersburg", "Novosibirsk", "box", 3676.16),
        ("Novosibirsk", "Yekaterinburg", "tovarnyak", 102042.09),
    ],
)
def test__calc_delivery_price(name1: str, name2: str, parcel_type: str, expected: float):
    assert calc_delivery_price(name1, name2, parcel_type) == expected
