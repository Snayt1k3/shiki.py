import pytest

from shikimori.endpoints.user_rates import UserRatesEndpoint
from shikimori.types.user_rates import UserRateResponse


@pytest.fixture
def user_rate() -> UserRatesEndpoint:
    return UserRatesEndpoint("", "", "")


@pytest.fixture
def user_rate_json() -> dict:
    return {
        "id": 9,
        "user_id": 23456789,
        "target_id": 8,
        "target_type": "Anime",
        "score": 0,
        "status": "planned",
        "rewatches": 0,
        "episodes": 0,
        "volumes": 0,
        "chapters": 0,
        "text": None,
        "text_html": "",
        "created_at": "2022-11-26T17:19:28.554+03:00",
        "updated_at": "2022-11-26T17:19:28.554+03:00",
    }


@pytest.fixture
def user_rates_json():
    return [
        {
            "id": 13,
            "user_id": 23456789,
            "target_id": 12,
            "target_type": "Anime",
            "score": 0,
            "status": "completed",
            "rewatches": 0,
            "episodes": 0,
            "volumes": 0,
            "chapters": 0,
            "text": None,
            "text_html": "",
            "created_at": "2022-11-26T17:19:28.708+03:00",
            "updated_at": "2022-11-26T17:19:28.708+03:00",
        },
        {
            "id": 14,
            "user_id": 23456789,
            "target_id": 13,
            "target_type": "Anime",
            "score": 0,
            "status": "planned",
            "rewatches": 0,
            "episodes": 0,
            "volumes": 0,
            "chapters": 0,
            "text": None,
            "text_html": "",
            "created_at": "2022-11-26T17:19:28.708+03:00",
            "updated_at": "2022-11-26T17:19:28.708+03:00",
        },
    ]


@pytest.fixture
def exp_list_response():
    return [
        UserRateResponse(
            13,
            23456789,
            12,
            "Anime",
            0,
            "completed",
            0,
            0,
            0,
            0,
            None,
            "",
            "2022-11-26T17:19:28.708+03:00",
            "2022-11-26T17:19:28.708+03:00",
        ),
        UserRateResponse(
            14,
            23456789,
            13,
            "Anime",
            0,
            "planned",
            0,
            0,
            0,
            0,
            None,
            "",
            "2022-11-26T17:19:28.708+03:00",
            "2022-11-26T17:19:28.708+03:00",
        ),
    ]


@pytest.fixture
def create_user_rate_json():
    return {
        "id": 16,
        "user_id": 23456789,
        "target_id": 15,
        "target_type": "Anime",
        "score": 10,
        "status": "completed",
        "rewatches": 5,
        "episodes": 2,
        "volumes": 3,
        "chapters": 4,
        "text": "test",
        "text_html": "test",
        "created_at": "2022-11-26T17:19:28.773+03:00",
        "updated_at": "2022-11-26T17:19:28.773+03:00",
    }


@pytest.fixture
def create_user_rate_exp():
    return UserRateResponse(
        16,
        23456789,
        15,
        "Anime",
        10,
        "completed",
        5,
        2,
        3,
        4,
        "test",
        "test",
        "2022-11-26T17:19:28.773+03:00",
        "2022-11-26T17:19:28.773+03:00",
    )
