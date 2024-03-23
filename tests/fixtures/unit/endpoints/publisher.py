import pytest

from shikimori.endpoints.publisher import PublisherEndpoint
from shikimori.types.publisher import Publisher


@pytest.fixture
def publisher_client():
    return PublisherEndpoint("", "", "")


@pytest.fixture
def publisher_list_json():
    return [{"id": 3, "name": "publisher_3"}]


@pytest.fixture
def publisher_list_resp(publisher_list_json):
    return [Publisher(**a) for a in publisher_list_json]
