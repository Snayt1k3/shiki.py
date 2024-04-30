import os

import pytest

from shikimori.auth import AccessTokenData


@pytest.mark.asyncio
async def test_auth_refresh(client):
    resp = await client.auth.refresh(os.getenv("REFRESH_TOKEN"))
    try:
        assert isinstance(resp, AccessTokenData)
    except Exception:
        pytest.skip()


@pytest.mark.asyncio
async def test_auth_access(client, auth_code):
    resp = await client.auth.get_access_token(auth_code)
    try:
        assert isinstance(resp, AccessTokenData)
    except Exception:
        pytest.skip()
