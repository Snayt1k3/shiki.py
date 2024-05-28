import pytest

from shikimori.endpoints.grapql import GraphQlEndpoint


@pytest.fixture
def graphql_client():
    return GraphQlEndpoint("", "", "")
