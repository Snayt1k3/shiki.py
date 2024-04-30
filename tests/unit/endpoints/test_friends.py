import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_add_success(friend_client):
    friend_client._request = FakeRequest({"notice": "added"})
    response = await friend_client.add(123)
    assert response == "added"


@pytest.mark.asyncio
async def test_add_error(friend_client):
    friend_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await friend_client.add(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(friend_client):
    friend_client._request = FakeRequest({"notice": "deleted"})
    response = await friend_client.delete(123)
    assert response == "deleted"


@pytest.mark.asyncio
async def test_delete_error(friend_client):
    friend_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await friend_client.delete(123)
    assert isinstance(response, RequestError)
