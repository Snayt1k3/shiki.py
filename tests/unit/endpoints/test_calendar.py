import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(calendar_client, calendar_list_json, calendar_list_resp):
    calendar_client._request = FakeRequest(calendar_list_json)
    response = await calendar_client.list(123)
    assert response == calendar_list_resp


@pytest.mark.asyncio
async def test_list_error(calendar_client):
    calendar_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await calendar_client.list(123)
    assert isinstance(response, RequestError)
