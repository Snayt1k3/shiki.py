import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(publisher_list_json, publisher_list_resp, publisher_client):
    publisher_client._request = FakeRequest(publisher_list_json)
    response = await publisher_client.list()
    assert response == publisher_list_resp


@pytest.mark.asyncio
async def test_list_error(publisher_client):
    publisher_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await publisher_client.list()
    assert isinstance(response, RequestError)
