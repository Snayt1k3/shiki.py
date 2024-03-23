import pytest
from shikimori.endpoints.topic_ignore import TopicIgnoreEndpoint


@pytest.fixture
def topic_ignore():
    return TopicIgnoreEndpoint("", "", "")
