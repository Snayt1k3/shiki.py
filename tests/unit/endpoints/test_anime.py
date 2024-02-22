import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.list(123)
    assert response

@pytest.mark.asyncio
async def test_list_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.list(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_by_id_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.byId(123)
    assert response

@pytest.mark.asyncio
async def test_by_id_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.byId(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_roles_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.roles(123)
    assert response

@pytest.mark.asyncio
async def test_roles_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.roles(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_similar_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.similar(123)
    assert response

@pytest.mark.asyncio
async def test_similar_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.similar(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_related_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.related(123)
    assert response

@pytest.mark.asyncio
async def test_related_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.related(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_screenshots_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.screenshots(123)
    assert response

@pytest.mark.asyncio
async def test_screenshots_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.screenshots(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_franchise_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.franchise(123)
    assert response

@pytest.mark.asyncio
async def test_franchise_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.franchise(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_externalLinks_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.externalLinks(123)
    assert response

@pytest.mark.asyncio
async def test_externalLinks_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.externalLinks(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_topics_success(anime_client):
    anime_client._request = FakeRequest({})
    response = await anime_client.topics(123)
    assert response

@pytest.mark.asyncio
async def test_topics_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.topics(123)
    assert isinstance(response, RequestError)
