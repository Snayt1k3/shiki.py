import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(calendar_client):
    calendar_client._request = FakeRequest({})
    response = await calendar_client.list(123)
    assert response

@pytest.mark.asyncio
async def test_list_error(calendar_client):
    calendar_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await calendar_client.list(123)
    assert isinstance(response, RequestError)
