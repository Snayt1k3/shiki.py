import asyncio
import random

import pytest
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_manga_list(client):
    await asyncio.sleep(random.uniform(1, 3))
    resp = await client.Manga.list()
    assert not isinstance(resp, RequestError)


@pytest.mark.asyncio
async def test_manga_byid(client):
    await asyncio.sleep(random.uniform(1, 3))
    resp = await client.Manga.ById(19)
    assert not isinstance(resp, RequestError)
