# pylint: disable=wrong-import-position
# type: ignore

import os
import sys

sys.path.append("gg/")
os.environ["MODEL_PATH"] = "gg/gg.pkl"

import pytest
from fastapi.testclient import TestClient

from gg.main import app

CLIENT = TestClient(app)


@pytest.mark.parametrize(
    "params,expected",
    [
        ({"frequency": 2, "monetary_value": 170}, 145.722),
        ({"frequency": 10, "monetary_value": 36}, 35.9651),
        ({"frequency": 5, "monetary_value": 10}, 12.0326),
    ],
)
def test_predict(params, expected):
    response = CLIENT.get("/predict/", params=params)
    assert response.status_code == 200
    assert list(response.json().keys()) == ["average_profit"]
    assert round(response.json()["average_profit"], 4) == expected


@pytest.mark.parametrize(
    "params",
    [
        {"frequency": -2, "monetary_value": 170},
        {"frequency": 10, "monetary_value": -36},
    ],
)
def test__predict__should_fail(params):
    response = CLIENT.get("/predict/", params=params)
    assert response.status_code == 404
    assert response.json() == {"detail": "All parameters should be positive"}
