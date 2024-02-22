import pytest
from shikimori.endpoints.calendar import CalendarEndpoint


@pytest.fixture
def calendar_client():
    return CalendarEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


