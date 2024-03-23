import pytest

from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_list_success(topic_client, topic_list_json, topic_list_resp):
    topic_client._request = FakeRequest(topic_list_json)
    response = await topic_client.list()
    assert response == topic_list_resp


@pytest.mark.asyncio
async def test_list_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.list()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_updates_success(topic_client, topic_updates_json, topic_updates_resp):
    topic_client._request = FakeRequest(topic_updates_json)
    response = await topic_client.updates()
    assert response == topic_updates_resp


@pytest.mark.asyncio
async def test_updates_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.updates()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_hot_success(topic_client, topics_hot_json, topics_hot_resp):
    topic_client._request = FakeRequest(topics_hot_json)
    response = await topic_client.hot()
    assert response == topics_hot_resp


@pytest.mark.asyncio
async def test_hot_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.hot()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_byid_success(topic_client, topics_byid_json, topics_byid_resp):
    topic_client._request = FakeRequest(topics_byid_json)
    response = await topic_client.ById(123)
    assert response == topics_byid_resp


@pytest.mark.asyncio
async def test_byid_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_success(topic_client, topics_create_json, topics_create_resp):
    topic_client._request = FakeRequest(topics_create_json)
    response = await topic_client.create(123, 1, 1, 1)
    assert response == topics_create_resp


@pytest.mark.asyncio
async def test_create_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.create(123, 1, 1, 1)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(topic_client, topics_update_json, topics_update_resp):
    topic_client._request = FakeRequest(topics_update_json)
    response = await topic_client.update(123, 1, 1, 1)
    assert response == topics_update_resp


@pytest.mark.asyncio
async def test_update_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.update(123, 1, 1, 1)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(topic_client):
    topic_client._request = FakeRequest({"notice": "deleted"})
    response = await topic_client.delete(123)
    assert response == "deleted"


@pytest.mark.asyncio
async def test_delete_error(topic_client):
    topic_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await topic_client.delete(123)
    assert isinstance(response, RequestError)
