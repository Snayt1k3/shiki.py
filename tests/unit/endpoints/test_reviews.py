import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_create_success(review_client, review_create_resp, review_create_json):
    review_client._request = FakeRequest(review_create_json)
    response = await review_client.create("", "", "")
    assert response == review_create_resp


@pytest.mark.asyncio
async def test_create_error(review_client):
    review_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await review_client.create("", "", "")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_update_success(review_client, review_create_resp, review_create_json):
    review_client._request = FakeRequest(review_create_json)
    response = await review_client.update("", "", "")
    assert response == review_create_resp


@pytest.mark.asyncio
async def test_update_error(review_client):
    review_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await review_client.update("", "", "")
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(review_client):
    review_client._request = FakeRequest({"notice": "DELETED"})
    response = await review_client.delete("")
    assert response == "DELETED"


@pytest.mark.asyncio
async def test_update_error(review_client):
    review_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await review_client.delete("")
    assert isinstance(response, RequestError)
