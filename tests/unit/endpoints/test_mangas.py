import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(manga_client, mangas_list_json, mangas_list_resp):
    manga_client._request = FakeRequest(mangas_list_json)
    response = await manga_client.list()
    assert response == mangas_list_resp


@pytest.mark.asyncio
async def test_list_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.list()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ById_success(manga_client, mangas_ById_json, mangas_ById_resp):
    manga_client._request = FakeRequest(mangas_ById_json)
    response = await manga_client.ById(123)
    assert response == mangas_ById_resp


@pytest.mark.asyncio
async def test_ById_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_roles_success(manga_client, mangas_roles_json, mangas_roles_resp):
    manga_client._request = FakeRequest(mangas_roles_json)
    response = await manga_client.roles(123)
    assert response == mangas_roles_resp


@pytest.mark.asyncio
async def test_roles_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.roles(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_similar_success(manga_client, mangas_similar_resp, mangas_similar_json):
    manga_client._request = FakeRequest(mangas_similar_json)
    response = await manga_client.similar(123)
    assert response == mangas_similar_resp


@pytest.mark.asyncio
async def test_similar_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.similar(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_related_success(manga_client, mangas_related_json, mangas_related_resp):
    manga_client._request = FakeRequest(mangas_related_json)
    response = await manga_client.related(123)
    assert response == mangas_related_resp


@pytest.mark.asyncio
async def test_related_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.related(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_franchise_success(
    manga_client, mangas_franchise_json, mangas_franchise_resp
):
    manga_client._request = FakeRequest(mangas_franchise_json)
    response = await manga_client.franchise(123)
    assert response == mangas_franchise_resp


@pytest.mark.asyncio
async def test_franchise_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.franchise(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ExternalLinks_success(
    manga_client, mangas_ExternalLinks_json, mangas_ExternalLinks_resp
):
    manga_client._request = FakeRequest(mangas_ExternalLinks_json)
    response = await manga_client.ExternalLinks(123)
    assert response == mangas_ExternalLinks_resp


@pytest.mark.asyncio
async def test_ExternalLinks_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.ExternalLinks(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_topics_success(manga_client, mangas_topics_json, mangas_topics_resp):
    manga_client._request = FakeRequest(mangas_topics_json)
    response = await manga_client.topics(123)
    assert response == mangas_topics_resp


@pytest.mark.asyncio
async def test_topics_error(manga_client):
    manga_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await manga_client.topics(123)
    assert isinstance(response, RequestError)
