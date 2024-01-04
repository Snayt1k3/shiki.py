import logging
from typing import Callable, Coroutine
import aiohttp
from .exceptions import RequestError


class Request:
    """class for send requests"""
    async def _get(self, url: str, query_params: dict = None, headers: dict = None):
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url, params=query_params) as response:

                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logging.debug(f"Error occurred with get request - {exc}")
            return RequestError(exc.message, exc.status)

    async def _post(self, url: str, body: dict = None, headers: dict = None):
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(url, json=body) as response:

                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logging.debug(f"Error occurred with post request - {exc}")
            return RequestError(exc.message, exc.status)

    async def _patch(self, url: str, body: dict = None, headers: dict = None):
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.patch(url, json=body) as response:

                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logging.debug(f"Error occurred with patch request - {exc}")
            return RequestError(exc.message, exc.status)

    async def _put(self, url: str, body: dict = None, headers: dict = None):
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.put(url, json=body) as response:

                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logging.debug(f"Error occurred with put request - {exc}")
            return RequestError(exc.message, exc.status)

    async def _delete(self, url: str, body: dict = None, headers: dict = None):
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.delete(url, json=body) as response:

                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientResponseError as exc:
            logging.debug(f"Error occurred with delete request - {exc}")
            return RequestError(exc.message, exc.status)

    async def make_request(self, method: str, **kwargs):
        methods: dict[str, [Callable, ..., Coroutine]] = {
            "GET": self._get,
            "POST": self._post,
            "PUT": self._put,
            "PATCH": self._patch,
            "DELETE": self._delete,
        }

        if method not in methods:
            raise ValueError(f"Method {method} is not allowed")

        request = methods.get(method)
        return await request(**kwargs)
