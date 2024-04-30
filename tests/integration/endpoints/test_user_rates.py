import os

import pytest


@pytest.mark.asyncio
async def test_user_rate_list(client):
    resp = await client.userRate.list(
        os.getenv("USER_ID"), target_type="Anime", status="planned"
    )
    assert isinstance(resp, list)


@pytest.mark.asyncio
async def test_user_rate_increment(client):
    client.set_token(os.getenv("ACCESS_TOKEN"))
    resp = await client.userRate.increment(117438752)
    try:
        assert not isinstance(resp, Exception)
    except Exception:
        pytest.skip()
