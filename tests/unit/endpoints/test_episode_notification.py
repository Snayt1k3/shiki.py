import pytest
from shikimori.types.episode_notification import EpisodeNotification
from shikimori.exceptions import RequestError
from tests.fixtures.unit.api_client import FakeRequest


@pytest.mark.asyncio
async def test_notify_success(episode_notification, json_episode_notification):
    episode_notification._request = FakeRequest(json_episode_notification)
    response = await episode_notification.notify("", "", "", "")
    assert EpisodeNotification(**json_episode_notification) == response


@pytest.mark.asyncio
async def test_notify_error(episode_notification):
    episode_notification._request = FakeRequest(RequestError("Error", 404))
    response = await episode_notification.notify("", "", "", "")
    assert isinstance(response, RequestError)
