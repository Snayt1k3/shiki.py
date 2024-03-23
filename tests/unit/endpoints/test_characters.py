import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_byId_success(character_client, character_list_json, character_list_resp):
    character_client._request = FakeRequest(character_list_json)
    response = await character_client.ById(123)
    assert response == character_list_resp


@pytest.mark.asyncio
async def test_byId_error(character_client):
    character_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await character_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_search_success(
    character_client, character_search_json, character_search_resp
):
    character_client._request = FakeRequest(character_search_json)
    response = await character_client.search(123)
    assert response == character_search_resp


@pytest.mark.asyncio
async def test_search_error(character_client):
    character_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await character_client.search(123)
    assert isinstance(response, RequestError)
