# pylint: disable=wrong-import-position
# type: ignore

import os
import sys

sys.path.append("clv/")
os.environ["BGNBD_SERVICE_URL"] = "http://bgnbd:8000/predict/"
os.environ["GG_SERVICE_URL"] = "http://gg:8000/predict/"

import pytest
from fastapi.testclient import TestClient
from httpx import URL

from clv.main import app

CLIENT = TestClient(app)


@pytest.fixture
def non_mocked_hosts() -> list:
    return ["testserver"]


@pytest.mark.parametrize(
    "httpxmock, params, bgnbd_response, gg_response, expected_clv",
    [
        (
            "httpx_mock",
            (
                ("t", 1.0),
                ("frequency", 2),
                ("recency", 3),
                ("T", 4.0),
                ("monetary_value", 170.0),
            ),
            (("number_of_purchases", 0.1828),),
            (("average_profit", 145.722),),
            26.638,
        ),
        (
            "httpx_mock",
            (
                ("t", 10.0),
                ("frequency", 10),
                ("recency", 10),
                ("T", 10.0),
                ("monetary_value", 36.0),
            ),
            (("number_of_purchases", 4.9667),),
            (("average_profit", 35.9651),),
            178.6279,
        ),
        (
            "httpx_mock",
            (
                ("t", 3.0),
                ("frequency", 5),
                ("recency", 7),
                ("T", 11.0),
                ("monetary_value", 10.0),
            ),
            (("number_of_purchases", 4.9667),),
            (("average_profit", 0.576),),
            2.8608,
        ),
    ],
)
def test_calc_clv(
    httpxmock, params, bgnbd_response, gg_response, expected_clv, request
):  # pylint: disable=too-many-arguments
    httpx_mock = request.getfixturevalue(httpxmock)
    params = dict(params)
    bgnbd_response = dict(bgnbd_response)
    gg_response = dict(gg_response)

    httpx_mock.add_response(
        url=URL(
            "http://bgnbd:8000/predict/",
            params={
                "t": params["t"],
                "frequency": params["frequency"],
                "recency": params["recency"],
                "T": params["T"],
            },
        ),
        json=bgnbd_response,
    )
    httpx_mock.add_response(
        url=URL(
            "http://gg:8000/predict/",
            params={"frequency": params["frequency"], "monetary_value": params["monetary_value"]},
        ),
        json=gg_response,
    )

    response = CLIENT.get("/clv/", params=params)
    assert response.status_code == 200
    assert list(response.json().keys()) == ["clv"]
    assert round(response.json()["clv"], 4) == expected_clv
