import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(forum_client, forum_list_json, forum_list_resp):
    forum_client._request = FakeRequest(forum_list_json)
    response = await forum_client.list()
    assert response == forum_list_resp

@pytest.mark.asyncio
async def test_list_error(forum_client):
    forum_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await forum_client.list()
    assert isinstance(response, RequestError)