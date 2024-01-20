import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..types.general.dialogs import Message, Dialog, MessageInfo
from ..types.user.user import User
from ..types.general.photo import PhotoExtended


class DialogsEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def list(self, access_token: str) -> List[Dialog] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs",
            headers=self.auth_headers(access_token),
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
        self, id: str, access_token: str
    ) -> List[MessageInfo] | RequestError:
        """

        :param id: like user_id
        :param access_token: auth token
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self.auth_headers(access_token),
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

    async def delete(self, id: str, access_token: str) -> str | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/dialogs/{id}",
            headers=self.auth_headers(access_token),
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
