import pytest
from shikimori.endpoints.abuse_requests import AbuseRequestEndpoint


@pytest.fixture
def abuse_request():
    return AbuseRequestEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


