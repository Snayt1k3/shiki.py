import pytest

from shikimori.endpoints.review import ReviewEndpoint
from shikimori.types.review import Review


@pytest.fixture
def review_client():
    return ReviewEndpoint("", "", "")


@pytest.fixture
def review_create_json():
    return {
        "id": 1,
        "user_id": 23456796,
        "anime_id": 28,
        "manga_id": None,
        "body": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "opinion": "positive",
        "is_written_before_release": False,
        "created_at": "2022-11-26T17:19:30.598+03:00",
        "updated_at": "2022-11-26T17:19:30.598+03:00",
        "comments_count": 0,
        "cached_votes_up": 0,
        "cached_votes_down": 0,
        "changed_at": None,
    }


@pytest.fixture
def review_create_resp(review_create_json):
    return Review(**review_create_json)
