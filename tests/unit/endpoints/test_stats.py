import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(stats_client,):
    stats_client._request = FakeRequest([123, 123])
    response = await stats_client.list()
    assert response == [123, 123]


@pytest.mark.asyncio
async def test_list_error(stats_client):
    stats_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await stats_client.list()
    assert isinstance(response, RequestError)