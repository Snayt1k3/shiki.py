import pytest
from shikimori.endpoints.achievements import AchievementsEndpoint


@pytest.fixture
def achievements_client():
    return AchievementsEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


