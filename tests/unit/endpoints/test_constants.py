import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_animes_success(const_client, const_animes_json, const_animes_resp):
    const_client._request = FakeRequest(const_animes_json)
    response = await const_client.animes()
    assert response == const_animes_resp


@pytest.mark.asyncio
async def test_animes_error(const_client):
    const_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await const_client.animes()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_mangas_success(const_client, const_mangas_json, const_mangas_resp):
    const_client._request = FakeRequest(const_mangas_json)
    response = await const_client.mangas()
    assert response == const_mangas_resp


@pytest.mark.asyncio
async def test_mangas_error(const_client):
    const_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await const_client.mangas()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_UserRates_success(
    const_client, const_user_rate_json, const_user_rate_resp
):
    const_client._request = FakeRequest(const_user_rate_json)
    response = await const_client.UserRates()
    assert response == const_user_rate_resp


@pytest.mark.asyncio
async def test_UserRates_error(const_client):
    const_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await const_client.UserRates()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_clubs_success(const_client, const_club_json, const_club_resp):
    const_client._request = FakeRequest(const_club_json)
    response = await const_client.clubs()
    assert response == const_club_resp


@pytest.mark.asyncio
async def test_clubs_error(const_client):
    const_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await const_client.clubs()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_smile_success(const_client, const_smile_json, const_smile_resp):
    const_client._request = FakeRequest(const_smile_json)
    response = await const_client.smileys()
    assert response == const_smile_resp


@pytest.mark.asyncio
async def test_smile_error(const_client):
    const_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await const_client.smileys()
    assert isinstance(response, RequestError)
