import pytest
from shikimori.endpoints.appears import AppearsEndpoint


@pytest.fixture
def appears_client():
    return AppearsEndpoint("", "", "")


@pytest.fixture
def response_json():
    return {}
