from unittest import mock

import pytest

from tests.fixtures.unit.api_client import FakeResponse


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ["method", "kwargs"],
    [
        ("GET", {"query_params": {"some": 123}}),
        ("POST", {"body": {}}),
        ("PATCH", {"body": {}}),
        ("DELETE", {"body": {}}),
        ("PUT", {"body": {}}),
    ],
)
async def test_request(request_client, method, kwargs):
    resp = FakeResponse({"some_key": "some_value"})

    with mock.patch(f"aiohttp.ClientSession.{method.lower()}", return_value=resp):
        response = await request_client.make_request(method, url="https://url", **kwargs)

    assert response == {"some_key": "some_value"}
