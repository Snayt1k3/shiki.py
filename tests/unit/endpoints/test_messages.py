import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_byid_success(message_client, messages_byid_resp, messages_byid_json):
    message_client._request = FakeRequest(messages_byid_json)
    response = await message_client.ById(12)
    assert response == messages_byid_resp


@pytest.mark.asyncio
async def test_byid_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.ById(12)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_success(
    message_client, messages_create_json, messages_create_resp
):
    message_client._request = FakeRequest(messages_create_json)
    response = await message_client.create(12, 12, 12)
    assert response == messages_create_resp


@pytest.mark.asyncio
async def test_create_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.create(12, 12, 12)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(
    message_client, messages_update_json, messages_update_resp
):
    message_client._request = FakeRequest(messages_update_json)
    response = await message_client.update(12, 12)
    assert response == messages_update_resp


@pytest.mark.asyncio
async def test_update_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.update(12, 12)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(message_client):
    message_client._request = FakeRequest({})
    response = await message_client.delete(12)
    assert response is None


@pytest.mark.asyncio
async def test_delete_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.delete(12)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_markRead_success(message_client):
    message_client._request = FakeRequest({})
    response = await message_client.markRead(12, True)
    assert response is None


@pytest.mark.asyncio
async def test_markRead_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.markRead(12, True)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_readAll_success(message_client):
    message_client._request = FakeRequest({})
    response = await message_client.readAll(12)
    assert response is None


@pytest.mark.asyncio
async def test_readAll_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.readAll(12)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_deleteAll_success(message_client):
    message_client._request = FakeRequest({})
    response = await message_client.deleteAll(12)
    assert response is None


@pytest.mark.asyncio
async def test_deleteAll_error(message_client):
    message_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await message_client.deleteAll(12)
    assert isinstance(response, RequestError)