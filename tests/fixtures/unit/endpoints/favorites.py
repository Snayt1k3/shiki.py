import pytest

from shikimori.endpoints.favorites import FavoritesEndpoint


@pytest.fixture
def favorites_client():
    return FavoritesEndpoint("", "", "")