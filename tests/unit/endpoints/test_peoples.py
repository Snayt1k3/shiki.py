import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_byid_success(people_client, people_byid_json, people_byid_resp):
    people_client._request = FakeRequest(people_byid_json)
    response = await people_client.ById(12)
    assert response == people_byid_resp


@pytest.mark.asyncio
async def test_byid_error(people_client):
    people_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await people_client.ById(12)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_search_success(people_client, people_search_json, people_search_resp):
    people_client._request = FakeRequest(people_search_json)
    response = await people_client.search(12)
    assert response == people_search_resp


@pytest.mark.asyncio
async def test_search_error(people_client):
    people_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await people_client.search(12)
    assert isinstance(response, RequestError)
