import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(ranobe_client, ranobe_list_json, ranobe_list_resp):
    ranobe_client._request = FakeRequest(ranobe_list_json)
    response = await ranobe_client.list()
    assert response == ranobe_list_resp


@pytest.mark.asyncio
async def test_list_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.list()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ById_success(ranobe_client, ranobe_byid_json, ranobe_byid_resp):
    ranobe_client._request = FakeRequest(ranobe_byid_json)
    response = await ranobe_client.ById(123)
    assert response == ranobe_byid_resp


@pytest.mark.asyncio
async def test_ById_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_roles_success(ranobe_client, ranobes_roles_json, ranobes_roles_resp):
    ranobe_client._request = FakeRequest(ranobes_roles_json)
    response = await ranobe_client.roles(123)
    assert response == ranobes_roles_resp


@pytest.mark.asyncio
async def test_roles_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.roles(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_similar_success(
    ranobe_client, ranobes_similar_json, ranobes_similar_resp
):
    ranobe_client._request = FakeRequest(ranobes_similar_json)
    response = await ranobe_client.similar(123)
    assert response == ranobes_similar_resp


@pytest.mark.asyncio
async def test_similar_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.similar(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_related_success(
    ranobe_client, ranobes_related_json, ranobes_related_resp
):
    ranobe_client._request = FakeRequest(ranobes_related_json)
    response = await ranobe_client.related(123)
    assert response == ranobes_related_resp


@pytest.mark.asyncio
async def test_related_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.related(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_franchise_success(
    ranobe_client, ranobes_franchise_json, ranobes_franchise_resp
):
    ranobe_client._request = FakeRequest(ranobes_franchise_json)
    response = await ranobe_client.franchise(123)
    assert response == ranobes_franchise_resp


@pytest.mark.asyncio
async def test_franchise_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.franchise(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ExternalLinks_success(
    ranobe_client, ranobes_external_resp, ranobes_external_json
):
    ranobe_client._request = FakeRequest(ranobes_external_json)
    response = await ranobe_client.ExternalLinks(123)
    assert response == ranobes_external_resp


@pytest.mark.asyncio
async def test_ExternalLinks_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.ExternalLinks(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_topics_success(ranobe_client, ranobes_topics_json, ranobes_topics_resp):
    ranobe_client._request = FakeRequest(ranobes_topics_json)
    response = await ranobe_client.topics(123)
    assert response == ranobes_topics_resp


@pytest.mark.asyncio
async def test_topics_error(ranobe_client):
    ranobe_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await ranobe_client.topics(123)
    assert isinstance(response, RequestError)
