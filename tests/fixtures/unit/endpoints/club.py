import pytest
from shikimori.endpoints.club import ClubEndpoint


@pytest.fixture
def club_client():
    return ClubEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


