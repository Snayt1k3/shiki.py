import pytest
import asyncio
from shikimori.exceptions import RequestError


@pytest.mark.asyncio
async def test_animes_list(client):
    resp = await client.Anime.list()
    assert not isinstance(resp, RequestError)


@pytest.mark.asyncio
async def test_animes_byid(client):
    resp = await client.Anime.byId(19)
    assert not isinstance(resp, RequestError)
