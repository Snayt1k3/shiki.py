import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.general.dialogs import Message, Dialog, MessageInfo
from ..types.user.user import User
from ..types.general.photo import PhotoExtended


class DialogsEndpoint(BaseEndpoint):
    async def list(self) -> List[Dialog] | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs",
            headers=self._headers(),
        )

        if not isinstance(response, RequestError):
            return [
                Dialog(
                    target_user=User(**s["target_user"]),
                    message=Message(**s["message"]),
                )
                for s in response
            ]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(
        self, id: str
    ) -> List[MessageInfo] | RequestError:
        """
        requires oauth scope
        :param id: like user_id
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self._headers(),
        )

        if not isinstance(response, RequestError):
            return [
                MessageInfo(
                    **s,
                    to=User(**s["to"], image=PhotoExtended(**s["to"]["image"])),
                    sender=User(**s["from"], image=PhotoExtended(**s["from"]["image"])),
                )
                for s in response
            ]

        logging.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: str) -> str | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self._headers(),
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response

