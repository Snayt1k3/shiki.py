import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(achievements_client, achievements_list_json, achievements_list_expected):
    achievements_client._request = FakeRequest(achievements_list_json)
    response = await achievements_client.list(123)
    assert response == achievements_list_expected

@pytest.mark.asyncio
async def test_list_error(achievements_client):
    achievements_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await achievements_client.list(123)
    assert isinstance(response, RequestError)
