import logging
from typing import List

from shikimori.types.dialog import Dialog
from shikimori.types.message import Message, MessageInfo
from shikimori.types.photo import PhotoExtended, Photo
from shikimori.types.topics import Linked
from shikimori.types.user import User
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class DialogsEndpoint(BaseEndpoint):
    async def list(self) -> List[Dialog] | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Dialog.from_dict(dialog) for dialog in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: str) -> List[MessageInfo] | RequestError:
        """
        requires oauth scope
        :param id: like user_id
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [MessageInfo.from_dict(msg) for msg in response]

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: str) -> str | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
