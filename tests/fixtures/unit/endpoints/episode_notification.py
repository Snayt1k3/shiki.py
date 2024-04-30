import pytest

from shikimori.endpoints.episode_notifications import EpisodeNotificationEndpoint


@pytest.fixture
def episode_notification():
    return EpisodeNotificationEndpoint("", "", "")


@pytest.fixture
def json_episode_notification():
    return {
        "id": 1,
        "anime_id": 35,
        "episode": 3,
        "is_raw": False,
        "is_subtitles": False,
        "is_fandub": True,
        "is_anime365": True,
        "topic_id": 123,
    }
