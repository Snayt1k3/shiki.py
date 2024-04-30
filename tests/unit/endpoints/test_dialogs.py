import pytest

from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_list_success(dialog_client, dialogs_list_json, dialogs_list_resp):
    dialog_client._request = FakeRequest(dialogs_list_json)
    response = await dialog_client.list()
    assert response == dialogs_list_resp


@pytest.mark.asyncio
async def test_list_error(dialog_client):
    dialog_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await dialog_client.list()
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_ById_success(dialog_client, dialogs_ById_json, dialogs_ById_resp):
    dialog_client._request = FakeRequest(dialogs_ById_json)
    response = await dialog_client.ById(123)
    assert response == dialogs_ById_resp


@pytest.mark.asyncio
async def test_ById_error(dialog_client):
    dialog_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await dialog_client.ById(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_delete_success(dialog_client):
    dialog_client._request = FakeRequest({"notice": "deleted"})
    response = await dialog_client.delete(123)
    assert response == "deleted"


@pytest.mark.asyncio
async def test_delete_error(dialog_client):
    dialog_client._request = FakeRequest(RequestError("Test Message", 404))
    response = await dialog_client.delete(123)
    assert isinstance(response, RequestError)
