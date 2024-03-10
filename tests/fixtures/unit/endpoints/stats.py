import pytest

from shikimori.endpoints.stats import StatsEndpoint


@pytest.fixture
def stats_client():
    return StatsEndpoint("", "", "")

