import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(club_client, club_list_resp, club_list_json):
    club_client._request = FakeRequest(club_list_json)
    response = await club_client.list(123)
    assert response == club_list_resp


@pytest.mark.asyncio
async def test_list_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.list(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ById_success(club_client, club_byId_json, club_byId_resp):
    club_client._request = FakeRequest(club_byId_json)
    response = await club_client.ById(123)
    assert response == club_byId_resp


@pytest.mark.asyncio
async def test_ById_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(club_client, club_byId_resp, club_byId_json):
    club_client._request = FakeRequest(club_byId_json)
    response = await club_client.update(123)
    assert response == club_byId_resp


@pytest.mark.asyncio
async def test_update_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.update(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_animes_success(club_client, club_animes_json, club_animes_resp):
    club_client._request = FakeRequest(club_animes_json)
    response = await club_client.animes(123)
    assert response == club_animes_resp


@pytest.mark.asyncio
async def test_animes_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.animes(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_mangas_success(club_client, club_mangas_json, club_mangas_resp):
    club_client._request = FakeRequest(club_mangas_json)
    response = await club_client.mangas(123)
    assert response == club_mangas_resp


@pytest.mark.asyncio
async def test_mangas_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.mangas(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ranobes_success(club_client, club_mangas_json, club_ranobes_resp):
    club_client._request = FakeRequest(club_mangas_json)
    response = await club_client.ranobes(123)
    assert response == club_ranobes_resp


@pytest.mark.asyncio
async def test_ranobes_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.ranobes(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_characters_success(
    club_client, club_characters_resp, club_characters_json
):
    club_client._request = FakeRequest(club_characters_json)
    response = await club_client.characters(123)
    assert response


@pytest.mark.asyncio
async def test_characters_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.characters(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_collections_success(
    club_client, club_collection_json, club_collection_resp
):
    club_client._request = FakeRequest(club_collection_json)
    response = await club_client.collections(123)
    assert response == club_collection_resp


@pytest.mark.asyncio
async def test_collections_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.collections(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_clubs_success(club_client, club_clubs_json, club_clubs_resp):
    club_client._request = FakeRequest(club_clubs_json)
    response = await club_client.clubs(123)
    assert response == club_clubs_resp


@pytest.mark.asyncio
async def test_clubs_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.clubs(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_members_success(club_client, club_members_json, club_members_resp):
    club_client._request = FakeRequest(club_members_json)
    response = await club_client.members(123)
    assert response == club_members_resp


@pytest.mark.asyncio
async def test_members_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.members(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_images_success(club_client, club_images_json, club_images_resp):
    club_client._request = FakeRequest(club_images_json)
    response = await club_client.images(123)
    assert response == club_images_resp


@pytest.mark.asyncio
async def test_images_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.images(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_join_success(club_client):
    club_client._request = FakeRequest({})
    response = await club_client.join(123)
    assert response is None


@pytest.mark.asyncio
async def test_join_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.join(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_leave_success(club_client):
    club_client._request = FakeRequest({})
    response = await club_client.leave(123)
    assert response is None


@pytest.mark.asyncio
async def test_leave_error(club_client):
    club_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await club_client.leave(123)
    assert isinstance(response, RequestError)
