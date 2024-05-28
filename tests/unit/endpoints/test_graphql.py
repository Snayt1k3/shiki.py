import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_animes_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.animes("123")
    assert response == {}


@pytest.mark.asyncio
async def test_animes_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.animes("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_characters_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.characters("123")
    assert response == {}


@pytest.mark.asyncio
async def test_characters_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.characters("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_contests_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.contests("123")
    assert response == {}


@pytest.mark.asyncio
async def test_contests_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.contests("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_currentUser_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.currentUser("123")
    assert response == {}


@pytest.mark.asyncio
async def test_currentUser_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.currentUser("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_genres_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.genres("123", "1231")
    assert response == {}


@pytest.mark.asyncio
async def test_genres_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.genres("123", "1234")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_mangas_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.mangas("123")
    assert response == {}


@pytest.mark.asyncio
async def test_mangas_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.mangas("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_people_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.people("123")
    assert response == {}


@pytest.mark.asyncio
async def test_people_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.people("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_userRates_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.userRates("123")
    assert response == {}


@pytest.mark.asyncio
async def test_userRates_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.userRates("123")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_users_success(graphql_client):
    graphql_client._request = FakeRequest({})
    response = await graphql_client.users("123")
    assert response == {}


@pytest.mark.asyncio
async def test_users_error(graphql_client):
    graphql_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await graphql_client.users("123")
    assert isinstance(response, RequestError)
