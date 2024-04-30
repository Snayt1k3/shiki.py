import pytest

from shikimori.endpoints.achievements import AchievementsEndpoint
from shikimori.types.achievements import Achievement


@pytest.fixture
def achievements_client():
    return AchievementsEndpoint("", "", "")


@pytest.fixture
def achievements_list_json():
    return [
        {
            "id": 811883697,
            "neko_id": "aa_megami_sama",
            "level": 0,
            "progress": 31,
            "user_id": 1,
            "created_at": "2021-03-29T10:00:37.080+03:00",
            "updated_at": "2023-04-07T19:21:46.136+03:00",
        },
        {
            "id": 1014790857,
            "neko_id": "akiyuki_shinbou",
            "level": 0,
            "progress": 76,
            "user_id": 1,
            "created_at": "2021-12-12T17:43:25.210+03:00",
            "updated_at": "2023-04-07T19:21:46.136+03:00",
        },
    ]


@pytest.fixture
def achievements_list_expected(achievements_list_json):
    return [Achievement(**a) for a in achievements_list_json]
