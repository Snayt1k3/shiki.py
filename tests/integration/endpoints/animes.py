import asyncio
import random

import pytest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_animes_list(client):
    await asyncio.sleep(random.uniform(1, 3))
    resp = await client.Anime.list()
    assert not isinstance(resp, RequestError)


@pytest.mark.asyncio
async def test_animes_byid(client):
    await asyncio.sleep(random.uniform(1, 3))
    resp = await client.Anime.byId(19)
    assert not isinstance(resp, RequestError)
