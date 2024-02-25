import pytest

from shikimori.endpoints.forums import ForumEndpoint
from shikimori.types.topics import Forum

@pytest.fixture
def forum_client():
    return ForumEndpoint("", "", "")


@pytest.fixture
def forum_list_json():
    return [
        {
            "id": 23,
            "position": 0,
            "name": "Скрытый",
            "permalink": "hidden",
            "url": "/forum/hidden",
        },
        {
            "id": 12,
            "position": 0,
            "name": "Рецензии",
            "permalink": "critiques",
            "url": "/forum/critiques",
        },
    ]
@pytest.fixture
def forum_list_resp(forum_list_json):
    return [Forum(**f) for f in forum_list_json]