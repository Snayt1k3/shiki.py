import pytest
from unittest import mock
from tests.fixtures.unit.api_client import client

@pytest.mark.asyncio
async def test_get_request(client):
    with mock.patch("aiohttp.ClientSession.get", return_value={"some_key": "some_value"}):
        response = await client.make_request("GET", url="https://url", query_params={"some": 123})

    assert response == {"some_key": "some_value"}
