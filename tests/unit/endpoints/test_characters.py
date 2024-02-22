import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_byId_success(character_client):
    character_client._request = FakeRequest({})
    response = await character_client.byId(123)
    assert response

@pytest.mark.asyncio
async def test_byId_error(character_client):
    character_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await character_client.byId(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_search_success(character_client):
    character_client._request = FakeRequest({})
    response = await character_client.search(123)
    assert response

@pytest.mark.asyncio
async def test_search_error(character_client):
    character_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await character_client.search(123)
    assert isinstance(response, RequestError)
