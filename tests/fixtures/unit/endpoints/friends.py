import pytest

from shikimori.endpoints.friends import FriendEndpoint

@pytest.fixture
def friend_client():
    return FriendEndpoint("", "", "")