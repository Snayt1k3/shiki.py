import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(ban_client):
    ban_client._request = FakeRequest({})
    response = await ban_client.list(123)
    assert response

@pytest.mark.asyncio
async def test_list_error(ban_client):
    ban_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ban_client.list(123)
    assert isinstance(response, RequestError)
