import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(comment_client, comments_list_json, comments_list_resp):
    comment_client._request = FakeRequest(comments_list_json)
    response = await comment_client.list()
    assert response == comments_list_resp


@pytest.mark.asyncio
async def test_list_error(comment_client):
    comment_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await comment_client.list(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_byId_success(comment_client, comments_byId_json, comments_byId_resp):
    comment_client._request = FakeRequest(comments_byId_json)
    response = await comment_client.ById(123)
    assert response == comments_byId_resp


@pytest.mark.asyncio
async def test_byId_error(comment_client):
    comment_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await comment_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_success(comment_client, comments_byId_json, comments_byId_resp):
    comment_client._request = FakeRequest(comments_byId_json)
    response = await comment_client.create(123)
    assert response == comments_byId_resp


@pytest.mark.asyncio
async def test_create_error(comment_client):
    comment_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await comment_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(comment_client, comments_byId_json, comments_byId_resp):
    comment_client._request = FakeRequest(comments_byId_json)
    response = await comment_client.update(123, {})
    assert response == comments_byId_resp


@pytest.mark.asyncio
async def test_update_error(comment_client):
    comment_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await comment_client.update(123, {})
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(comment_client):
    comment_client._request = FakeRequest({"notice": "deleted"})
    response = await comment_client.delete(123)
    assert response == "deleted"


@pytest.mark.asyncio
async def test_delete_error(comment_client):
    comment_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await comment_client.delete(123)
    assert isinstance(response, RequestError)
