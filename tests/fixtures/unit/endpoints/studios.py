import pytest

from shikimori.endpoints.studios import StudiosEndpoint
from shikimori.types.studios import Studio


@pytest.fixture
def studio_client():
    return StudiosEndpoint("", "", "")


@pytest.fixture
def studios_list_json():
    return [
        {
            "id": 1,
            "name": "studio_1",
            "filtered_name": "studio_1",
            "real": False,
            "image": None,
        }
    ]


@pytest.fixture
def studios_list_resp(studios_list_json):
    return [Studio(**a) for a in studios_list_json]
