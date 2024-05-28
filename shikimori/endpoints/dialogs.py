import logging
from typing import List

from shikimori.types.dialog import Dialog
from shikimori.types.message import MessageInfo
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class DialogsEndpoint(BaseEndpoint):
    async def list(self) -> List[Dialog] | RequestError:
        """
        List dialogs.

        Requires messages oauth scope.
        """
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
        Show a dialog.
        Requires messages oauth scope.

        :param id: like user_{id}.
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
        """
        Destroy a dialog.
        Requires messages oauth scope.

        :param id: like user_{id}.
        """
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
