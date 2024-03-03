import pytest

from shikimori.endpoints.genres import GenreEndpoint
from shikimori.types.genres import Genre


@pytest.fixture
def genre_client():
    return GenreEndpoint("", "", "")


@pytest.fixture
def genres_list_json():
    return [{"id": 1, "name": "genre_1", "russian": None, "kind": "anime"}]

@pytest.fixture
def genres_list_resp(genres_list_json):
    return [Genre(**a) for a in genres_list_json]

