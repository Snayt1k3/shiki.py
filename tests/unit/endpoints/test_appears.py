import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_read_success(appears_client):
    appears_client._request = FakeRequest({})
    response = await appears_client.read(123)
    assert response is None

@pytest.mark.asyncio
async def test_read_error(appears_client):
    appears_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await appears_client.read(123)
    assert isinstance(response, RequestError)
