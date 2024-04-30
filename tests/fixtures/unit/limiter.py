import pytest

from shikimori.requestLimiter import RequestLimiter
from shikimori.constants import MAX_REQUESTS_PER_MINUTE, MAX_REQUESTS_PER_SECOND


@pytest.fixture
def limiter_client(fake_request_client):
    return RequestLimiter(
        MAX_REQUESTS_PER_SECOND, MAX_REQUESTS_PER_MINUTE, fake_request_client
    )
