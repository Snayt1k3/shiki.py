from shikimori.types.user_rates import UserRate
from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest

import pytest


@pytest.mark.asyncio
async def test_by_id_success(user_rate, user_rate_json):
    user_rate._request = FakeRequest(user_rate_json)
    response = await user_rate.ById(9)
    assert UserRate(**user_rate_json) == response


@pytest.mark.asyncio
async def test_by_id_error(user_rate):
    user_rate._request = FakeRequest(RequestError("Message", 404))
    response = await user_rate.ById(9)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_list_success(user_rate, user_rates_json, exp_list_response):
    user_rate._request = FakeRequest(user_rates_json)
    response = await user_rate.list(0, 0, "", "", 0, 0)
    assert exp_list_response == response


@pytest.mark.asyncio
async def test_list_error(user_rate):
    user_rate._request = FakeRequest(RequestError("message", 404))
    response = await user_rate.list(0, 0, "", "", 0, 0)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_success(user_rate, create_user_rate_json, create_user_rate_exp):
    user_rate._request = FakeRequest(create_user_rate_json)
    response = await user_rate.create(23456789, 15, "Anime")
    assert create_user_rate_exp == response


@pytest.mark.asyncio
async def test_create_error(user_rate):
    user_rate._request = FakeRequest(RequestError("message"))
    response = await user_rate.create(23456789, 15, "Anime")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(user_rate, user_rate_json):
    user_rate._request = FakeRequest(user_rate_json)
    response = await user_rate.update(14)
    assert UserRate(**user_rate_json) == response


@pytest.mark.asyncio
async def test_update_error(user_rate):
    user_rate._request = FakeRequest(RequestError("message"))
    response = await user_rate.update(14)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_increment_success(user_rate_json, user_rate):
    user_rate._request = FakeRequest(user_rate_json)
    response = await user_rate.increment(14)
    assert UserRate(**user_rate_json) == response


@pytest.mark.asyncio
async def test_increment_error(user_rate):
    user_rate._request = FakeRequest(RequestError("message"))
    response = await user_rate.increment(14)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(user_rate, user_rate_json):
    user_rate._request = FakeRequest(user_rate_json)
    response = await user_rate.delete(14)
    assert response is None


@pytest.mark.asyncio
async def test_delete_error(user_rate):
    user_rate._request = FakeRequest(RequestError("Message"))
    response = await user_rate.delete(14)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_cleanup_success(user_rate):
    user_rate._request = FakeRequest({"notice": "message"})
    response = await user_rate.cleanup(14)
    assert isinstance(response, dict)


@pytest.mark.asyncio
async def test_cleanup_error(user_rate):
    user_rate._request = FakeRequest(RequestError("Message"))
    response = await user_rate.cleanup(14)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_reset_success(user_rate):
    user_rate._request = FakeRequest({"notice": "message"})
    response = await user_rate.reset(14)
    assert isinstance(response, dict)


@pytest.mark.asyncio
async def test_reset_error(user_rate):
    user_rate._request = FakeRequest(RequestError("Message"))
    response = await user_rate.reset(14)
    assert isinstance(response, RequestError)
