import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.photo import PhotoExtended
from ..types.user import User
from shikimori.types.message import MessageInfo

logger = logging.getLogger(__name__)


class MessageEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> MessageInfo | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/messages/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MessageInfo(
                **response,
                to=User(
                    **response["to"], image=PhotoExtended(**response["to"]["image"])
                ),
                sender=User(
                    **response["from"], image=PhotoExtended(**response["from"]["image"])
                ),
            )

        logger.debug(
            f"Bad Request(byId): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self, from_id: int, to_id: int, body: str, kind: str = "Private"
    ) -> MessageInfo | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/messages/",
            body={
                "message": {
                    "from_id": from_id,
                    "to_id": to_id,
                    "body": body,
                    "kind": kind,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MessageInfo(
                **response,
                to=User(
                    **response["to"], image=PhotoExtended(**response["to"]["image"])
                ),
                sender=User(
                    **response["from"],
                    image=PhotoExtended(**response["from"]["image"]),
                ),
            )

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(self, id: int, body: str) -> MessageInfo | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/messages/{id}",
            body={
                "message": {
                    "body": body,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MessageInfo(
                **response,
                to=User(
                    **response["to"], image=PhotoExtended(**response["to"]["image"])
                ),
                sender=User(
                    **response["from"],
                    image=PhotoExtended(**response["from"]["image"]),
                ),
            )

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> None | RequestError:
        """requires oauth scope"""
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/messages/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def markRead(self, ids: str, is_read: bool) -> None | RequestError:
        """
        mark as read or unread.
        requires oauth scope
        :param ids: string like '123, 34455, 283761846'
        :param is_read: True - read, False - Unread
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/messages/mark_read",
            body={"ids": ids, "is_read": "1" if is_read else "0"},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(mark_read): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def readAll(self, type: str) -> None | RequestError:
        """
        requires oauth scope
        :param type: Must be one of: news, notifications.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/messages/read_all",
            body={"type": type},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(readAll): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def deleteAll(self, type: str) -> None | RequestError:
        """
        requires oauth scope
        :param type: Must be one of: news, notifications.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/messages/delete_all",
            body={"type": type},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(deleteAll): status - {response.status_code}: info - {str(response)}"
        )

        return response
