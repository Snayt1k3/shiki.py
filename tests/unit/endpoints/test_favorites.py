import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_create_success(favorites_client):
    favorites_client._request = FakeRequest({"notice": "message"})
    response = await favorites_client.add(123, {})
    assert response == "message"

@pytest.mark.asyncio
async def test_create_error(favorites_client):
    favorites_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await favorites_client.add(123, {})
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_create_success(favorites_client):
    favorites_client._request = FakeRequest({"notice": "message"})
    response = await favorites_client.delete(123, {})
    assert response == "message"

@pytest.mark.asyncio
async def test_create_error(favorites_client):
    favorites_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await favorites_client.delete(123, {})
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_delete_success(favorites_client):
    favorites_client._request = FakeRequest({"notice": "message"})
    response = await favorites_client.delete(123, {})
    assert response == "message"

@pytest.mark.asyncio
async def test_delete_error(favorites_client):
    favorites_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await favorites_client.delete(123, {})
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_reorder_success(favorites_client):
    favorites_client._request = FakeRequest({"notice": "message"})
    response = await favorites_client.reorder(123, {})
    assert response is None

@pytest.mark.asyncio
async def test_reorder_error(favorites_client):
    favorites_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await favorites_client.reorder(123, {})
    assert isinstance(response, RequestError)