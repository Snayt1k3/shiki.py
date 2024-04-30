import pytest

from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_list_success(user_client, users_list_json, users_list_resp):
    user_client._request = FakeRequest(users_list_json)
    response = await user_client.list()
    assert response == users_list_resp


@pytest.mark.asyncio
async def test_list_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.list()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_byid_success(user_client, users_byid_resp, users_byid_json):
    user_client._request = FakeRequest(users_byid_json)
    response = await user_client.ById(123)
    assert response == users_byid_resp


@pytest.mark.asyncio
async def test_byid_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_info_success(user_client, users_info_json, users_info_resp):
    user_client._request = FakeRequest(users_info_json)
    response = await user_client.info(123)
    assert response == users_info_resp


@pytest.mark.asyncio
async def test_info_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.info(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_info_success(user_client, users_info_json, users_info_resp):
    user_client._request = FakeRequest(users_info_json)
    response = await user_client.info(123)
    assert response == users_info_resp


@pytest.mark.asyncio
async def test_info_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.info(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_whoami_success(user_client, users_whoami_json, users_whoami_resp):
    user_client._request = FakeRequest(users_whoami_json)
    response = await user_client.whoami()
    assert response == users_whoami_resp


@pytest.mark.asyncio
async def test_info_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.whoami()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_signout_success(user_client, users_signout_json):
    user_client._request = FakeRequest(users_signout_json)
    response = await user_client.signOut()
    assert response is None


@pytest.mark.asyncio
async def test_info_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.signOut()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_friends_success(user_client, users_friends_json, users_friends_resp):
    user_client._request = FakeRequest(users_friends_json)
    response = await user_client.friends()
    assert response == users_friends_resp


@pytest.mark.asyncio
async def test_friends_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.friends()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_clubs_success(user_client, users_clubs_json, users_clubs_resp):
    user_client._request = FakeRequest(users_clubs_json)
    response = await user_client.clubs(123)
    assert response == users_clubs_resp


@pytest.mark.asyncio
async def test_clubs_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.clubs(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_clubs_success(user_client, users_clubs_json, users_clubs_resp):
    user_client._request = FakeRequest(users_clubs_json)
    response = await user_client.clubs(123)
    assert response == users_clubs_resp


@pytest.mark.asyncio
async def test_clubs_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.clubs(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_clubs_success(user_client, users_clubs_json, users_clubs_resp):
    user_client._request = FakeRequest(users_clubs_json)
    response = await user_client.clubs(123)
    assert response == users_clubs_resp


@pytest.mark.asyncio
async def test_clubs_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.clubs(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_animesrates_success(
    user_client, users_animerates_json, users_animerates_resp
):
    user_client._request = FakeRequest(users_animerates_json)
    response = await user_client.animeRates(123)
    assert response == users_animerates_resp


@pytest.mark.asyncio
async def test_animesrates_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.animeRates(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_mangarates_success(
    user_client, users_mangarates_json, users_mangarates_resp
):
    user_client._request = FakeRequest(users_mangarates_json)
    response = await user_client.mangaRates(123)
    assert response == users_mangarates_resp


@pytest.mark.asyncio
async def test_mangarates_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.mangaRates(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_mangarates_success(
    user_client, users_mangarates_json, users_mangarates_resp
):
    user_client._request = FakeRequest(users_mangarates_json)
    response = await user_client.mangaRates(123)
    assert response == users_mangarates_resp


@pytest.mark.asyncio
async def test_mangarates_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.mangaRates(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_favourites_success(
    user_client, users_favourites_json, users_favourites_resp
):
    user_client._request = FakeRequest(users_favourites_json)
    response = await user_client.favourites(123)
    assert response == users_favourites_resp


@pytest.mark.asyncio
async def test_favourites_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.favourites(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_messages_success(user_client, users_messages_json, users_messages_resp):
    user_client._request = FakeRequest(users_messages_json)
    response = await user_client.messages(123)
    assert response == users_messages_resp


@pytest.mark.asyncio
async def test_messages_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.messages(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_unreadMessages_success(
    user_client, users_unread_json, users_unread_resp
):
    user_client._request = FakeRequest(users_unread_json)
    response = await user_client.unread(123)
    assert response == users_unread_resp


@pytest.mark.asyncio
async def test_unreadMessages_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.unread(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_history_success(user_client, users_history_resp, users_history_json):
    user_client._request = FakeRequest(users_history_json)
    response = await user_client.history(123)
    assert response == users_history_resp


@pytest.mark.asyncio
async def test_history_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.history(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_bans_success(user_client, users_bans_json, users_bans_resp):
    user_client._request = FakeRequest(users_bans_json)
    response = await user_client.bans(123)
    assert response == users_bans_resp


@pytest.mark.asyncio
async def test_bans_error(user_client):
    user_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await user_client.bans(123)
    assert isinstance(response, RequestError)
