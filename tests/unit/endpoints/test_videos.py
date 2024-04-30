import pytest

from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_list_success(video_client, videos_list_json, videos_list_resp):
    video_client._request = FakeRequest(videos_list_json)
    response = await video_client.list(123)
    assert response == videos_list_resp


@pytest.mark.asyncio
async def test_list_error(video_client):
    video_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await video_client.list(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_success(video_client, videos_create_json, videos_create_resp):
    video_client._request = FakeRequest(videos_create_json)
    response = await video_client.create(123, 123, 123, 31)
    assert response == videos_create_resp


@pytest.mark.asyncio
async def test_create_error(video_client):
    video_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await video_client.create(123, 123, 123, 132)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(video_client):
    video_client._request = FakeRequest({})
    response = await video_client.delete(123, 123)
    assert response is None


@pytest.mark.asyncio
async def test_delete_error(video_client):
    video_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await video_client.delete(123, 123)
    assert isinstance(response, RequestError)
