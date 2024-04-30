import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(genre_client, genres_list_json, genres_list_resp):
    genre_client._request = FakeRequest(genres_list_json)
    response = await genre_client.list()
    assert response == genres_list_resp


@pytest.mark.asyncio
async def test_list_error(genre_client):
    genre_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await genre_client.list()
    assert isinstance(response, RequestError)
