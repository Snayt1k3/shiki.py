import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(anime_client, animes_list_json, animes_list_resp):
    anime_client._request = FakeRequest(animes_list_json)
    response = await anime_client.list(123)
    assert response == animes_list_resp

@pytest.mark.asyncio
async def test_list_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.list(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_by_id_success(anime_client, animes_byId_json, animes_byId_resp):
    anime_client._request = FakeRequest(animes_byId_json)
    response = await anime_client.ById(123)
    assert response == animes_byId_resp

@pytest.mark.asyncio
async def test_by_id_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.ById(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_roles_success(anime_client, animes_roles_json, animes_roles_resp):
    anime_client._request = FakeRequest(animes_roles_json)
    response = await anime_client.roles(123)
    assert response == animes_roles_resp

@pytest.mark.asyncio
async def test_roles_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.roles(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_similar_success(anime_client, animes_list_json, animes_list_resp):
    anime_client._request = FakeRequest(animes_list_json)
    response = await anime_client.similar(123)
    assert response == animes_list_resp

@pytest.mark.asyncio
async def test_similar_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.similar(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_related_success(anime_client, animes_related_json, animes_related_resp):
    anime_client._request = FakeRequest(animes_related_json)
    response = await anime_client.related(123)
    assert response == animes_related_resp

@pytest.mark.asyncio
async def test_related_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.related(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_screenshots_success(anime_client, animes_screenshots_json, animes_screenshots_resp):
    anime_client._request = FakeRequest(animes_screenshots_json)
    response = await anime_client.screenshots(123)
    assert response == animes_screenshots_resp

@pytest.mark.asyncio
async def test_screenshots_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.screenshots(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_franchise_success(anime_client, animes_franchise_json, animes_franchise_resp):
    anime_client._request = FakeRequest(animes_franchise_json)
    response = await anime_client.franchise(123)
    assert response == animes_franchise_resp

@pytest.mark.asyncio
async def test_franchise_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.franchise(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_externalLinks_success(anime_client, animes_external_json, animes_external_resp):
    anime_client._request = FakeRequest(animes_external_json)
    response = await anime_client.externalLinks(123)
    assert response == animes_external_resp

@pytest.mark.asyncio
async def test_externalLinks_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.externalLinks(123)
    assert isinstance(response, RequestError)

@pytest.mark.asyncio
async def test_topics_success(anime_client, animes_topics_resp, animes_topics_json):
    anime_client._request = FakeRequest(animes_topics_json)
    response = await anime_client.topics(123)
    assert response == animes_topics_resp

@pytest.mark.asyncio
async def test_topics_error(anime_client):
    anime_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await anime_client.topics(123)
    assert isinstance(response, RequestError)
