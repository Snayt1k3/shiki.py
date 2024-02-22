import pytest
from shikimori.endpoints.animes import AnimeEndpoint


@pytest.fixture
def anime_client():
    return AnimeEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


