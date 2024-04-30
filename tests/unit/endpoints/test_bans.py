import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(ban_client, bans_list_json, bans_list_resp):
    ban_client._request = FakeRequest(bans_list_json)
    response = await ban_client.list()
    assert response == bans_list_resp


@pytest.mark.asyncio
async def test_list_error(ban_client):
    ban_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ban_client.list()
    assert isinstance(response, RequestError)
