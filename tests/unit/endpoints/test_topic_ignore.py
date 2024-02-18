import pytest

from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest
from shikimori.types.topic_ignore import Topic


@pytest.mark.asyncio
async def test_ignore_success(topic_ignore):
    json = {"topic_id": "82468", "is_ignored": True}
    topic_ignore._request = FakeRequest(json)
    response = await topic_ignore.ignore(123)
    assert response == Topic(**json)


@pytest.mark.asyncio
async def test_ignore_error(topic_ignore):
    topic_ignore._request = FakeRequest(RequestError("Error", 404))
    response = await topic_ignore.ignore(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_unignore_success(topic_ignore):
    json = {"topic_id": "82468", "is_ignored": False}
    topic_ignore._request = FakeRequest(json)
    response = await topic_ignore.unignore(123)
    assert response == Topic(**json)


@pytest.mark.asyncio
async def test_unignore_error(topic_ignore):
    topic_ignore._request = FakeRequest(RequestError("Error", 404))
    response = await topic_ignore.unignore(123)
    assert isinstance(response, RequestError)
