import pytest

from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_list_success(studio_client, studios_list_json, studios_list_resp):
    studio_client._request = FakeRequest(studios_list_json)
    response = await studio_client.list()
    assert response == studios_list_resp


@pytest.mark.asyncio
async def test_list_error(studio_client):
    studio_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await studio_client.list()
    assert isinstance(response, RequestError)
