import pytest

from shikimori.request import Request


class FakeRequest:
    def __init__(self, response) -> None:
        self.response = response

    async def _post(self, *args, **kwargs):
        return self.response

    async def _get(self, *args, **kwargs):
        return self.response

    async def _patch(self, *args, **kwargs):
        return self.response

    async def _put(self, *args, **kwargs):
        return self.response

    async def make_request(self, *args, **kwargs):
        return self.response


class FakeResponse:
    def __init__(self, response):
        self.response = response

    async def __aenter__(self):
        return self

    def raise_for_status(self):
        return

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self

    async def json(self):
        return self.response


@pytest.fixture
def request_client():
    return Request()

@pytest.fixture
def fake_request_client():
    return FakeRequest({})
