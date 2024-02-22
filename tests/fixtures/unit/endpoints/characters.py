import pytest
from shikimori.endpoints.characters import CharacterEndpoint


@pytest.fixture
def character_client():
    return CharacterEndpoint("", "", "")

@pytest.fixture
def response_json():
    return {}


