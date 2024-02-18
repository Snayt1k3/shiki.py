import pytest

from shikimori.exceptions import RequestError
from shikimori.types.user_ignore import UserIgnore
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_ignore_success(user_ignore):
    json = {"user_id": "23456795", "is_ignored": True}
    user_ignore._request = FakeRequest(json)
    response = await user_ignore.ignore(123)
    assert response == UserIgnore(**json)


@pytest.mark.asyncio
async def test_ignore_error(user_ignore):
    user_ignore._request = FakeRequest(RequestError("Error", 404))
    response = await user_ignore.ignore(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_unignore_success(user_ignore):
    json = {"user_id": "23456794", "is_ignored": False}
    user_ignore._request = FakeRequest(json)
    response = await user_ignore.unignore(123)
    assert response == UserIgnore(**json)


@pytest.mark.asyncio
async def test_unignore_error(user_ignore):
    user_ignore._request = FakeRequest(RequestError("Error", 404))
    response = await user_ignore.unignore(123)
    assert isinstance(response, RequestError)
