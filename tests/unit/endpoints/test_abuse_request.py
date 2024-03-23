import pytest

from shikimori.types.abuse_requests import AbuseRequest
from tests.fixtures.unit.api_client import FakeRequest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_as_offtopic_success(abuse_request):
    json = {"kind": "offtopic", "value": False, "affected_ids": [1]}
    abuse_request._request = FakeRequest(json)
    response = await abuse_request.AsOfftopic(123)
    assert AbuseRequest(**json) == response


@pytest.mark.asyncio
async def test_as_offtopic_error(abuse_request):
    abuse_request._request = FakeRequest(RequestError("Test Message", 404))
    response = await abuse_request.AsOfftopic(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_as_review_success(abuse_request):
    abuse_request._request = FakeRequest({})
    response = await abuse_request.AsReview(123, 123)
    assert response is None


@pytest.mark.asyncio
async def test_as_offtopic_error(abuse_request):
    abuse_request._request = FakeRequest(RequestError("Test Message", 404))
    response = await abuse_request.AsReview(123)
    assert isinstance(response, RequestError)


@pytest.mark.asyncio
async def test_create_violation_success(abuse_request):
    abuse_request._request = FakeRequest({})
    response = await abuse_request.CreateViolation()
    assert response is None


@pytest.mark.asyncio
async def test_create_violation_error(abuse_request):
    abuse_request._request = FakeRequest(RequestError("Test Message", 404))
    response = await abuse_request.CreateViolation()
    assert isinstance(response, RequestError)


@pytest.mark.asycnio
async def test_spoiler_in_content_success(abuse_request):
    abuse_request._request = FakeRequest({})
    response = await abuse_request.SpoilerInContent()
    assert response is None


async def test_spoiler_in_content_error(abuse_request):
    abuse_request._request = FakeRequest(RequestError("Test Message", 404))
    response = await abuse_request.SpoilerInContent()
    assert isinstance(response, RequestError)
