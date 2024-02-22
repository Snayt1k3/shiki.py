import pytest
from shikimori.endpoints.bans import BanEndpoint


@pytest.fixture
def ban_client():
    return BanEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


