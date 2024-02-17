import asyncio
import time

import pytest
from shikimori.exceptions import TooManyRequests, RequestError


@pytest.mark.asyncio
async def test_limiter_success(limiter_client):
    try:
        tasks = [
            asyncio.create_task(limiter_client.make_request("GET", url=""))
            for _ in range(5)
        ]
        await asyncio.gather(*tasks)
    except TooManyRequests as e:
        pytest.fail("TooManyRequests occurred", e)


@pytest.mark.asyncio
async def test_limiter_error(limiter_client):
    try:
        tasks = [
            asyncio.create_task(limiter_client.make_request("GET", url=""))
            for _ in range(8)
        ]
        await asyncio.gather(*tasks)
        pytest.fail("Limiter is not working")
    except TooManyRequests:
        pass
