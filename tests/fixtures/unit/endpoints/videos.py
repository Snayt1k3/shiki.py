import pytest

from shikimori.endpoints.videos import VideosEndpoint
from shikimori.types.videos import Video


@pytest.fixture
def video_client():
    return VideosEndpoint("", "", "")


@pytest.fixture
def videos_list_json():
    return [
        {
            "id": 2,
            "url": "https://youtube.com/watch?v=VdwKZ6JDENc",
            "image_url": "http://img.youtube.com/vi/VdwKZ6JDENc/hqdefault.jpg",
            "player_url": "http://youtube.com/embed/VdwKZ6JDENc",
            "name": None,
            "kind": "op",
            "hosting": "youtube",
        }
    ]


@pytest.fixture
def videos_list_resp(videos_list_json):
    return [Video(**v) for v in videos_list_json]


@pytest.fixture
def videos_create_json():
    return {
        "id": 3,
        "url": "https://youtube.com/watch?v=l1YX30AmYsA",
        "image_url": "http://img.youtube.com/vi/l1YX30AmYsA/hqdefault.jpg",
        "player_url": "http://youtube.com/embed/l1YX30AmYsA",
        "name": "test",
        "kind": "pv",
        "hosting": "youtube",
    }


@pytest.fixture
def videos_create_resp(videos_create_json):
    return Video(**videos_create_json)
