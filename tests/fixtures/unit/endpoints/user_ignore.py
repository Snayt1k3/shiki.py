from shikimori.endpoints.user_ignore import UserIgnoreEndpoint
import pytest

@pytest.fixture
def user_ignore():
    return UserIgnoreEndpoint("", "", "")
