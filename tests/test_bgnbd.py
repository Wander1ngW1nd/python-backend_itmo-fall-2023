# pylint: disable=wrong-import-position
# type: ignore

import os

os.environ["MODEL_PATH"] = "bgnbd/bgnbd.pkl"

import pytest
from fastapi.testclient import TestClient

from bgnbd.main import app

CLIENT = TestClient(app)


@pytest.mark.parametrize(
    "params,expected",
    [
        ({"t": 1, "frequency": 2, "recency": 3, "T": 4}, 0.1828),
        ({"t": 10, "frequency": 10, "recency": 10, "T": 10}, 4.9667),
        ({"t": 3, "frequency": 5, "recency": 7, "T": 11}, 0.576),
    ],
)
def test_predict(params, expected):
    response = CLIENT.get("/predict/", params=params)
    assert response.status_code == 200
    assert list(response.json().keys()) == ["number_of_purchases"]
    assert round(response.json()["number_of_purchases"], 4) == expected


@pytest.mark.parametrize(
    "params",
    [
        {"t": -1, "frequency": 2, "recency": 3, "T": 4},
        {"t": 10, "frequency": -10, "recency": 10, "T": 10},
        {"t": 3, "frequency": 5, "recency": -7, "T": 11},
    ],
)
def test__predict__should_fail(params):
    response = CLIENT.get("/predict/", params=params)
    assert response.status_code == 404
    assert response.json() == {"detail": "All parameters should be positive"}
