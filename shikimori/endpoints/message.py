import logging

from shikimori.types.message import MessageInfo
from shikimori.types.photo import PhotoExtended, Photo
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.topics import Linked
from ..types.user import User

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
                id=response["id"],
                body=response["body"],
                created_at=response["created_at"],
                html_body=response["html_body"],
                kind=response["kind"],
                linked=(
                    Linked(
                        name=response["linked"]["name"],
                        id=response["linked"]["id"],
                        russian=response["linked"]["russian"],
                        url=response["linked"]["url"],
                        kind=response["linked"]["kind"],
                        score=response["linked"]["score"],
                        status=response["linked"]["status"],
                        episodes=response["linked"].get("episodes"),
                        episodes_aired=response["linked"].get("episodes_aired"),
                        volumes=response["linked"].get("volumes"),
                        chapters=response["linked"].get("chapters"),
                        aired_on=response["linked"]["aired_on"],
                        released_on=response["linked"]["released_on"],
                        image=Photo(**response["linked"]["image"]),
                    )
                    if response["linked"]
                    else None
                ),
                linked_id=response["linked_id"],
                linked_type=response["linked_id"],
                read=response["read"],
                to=User(
                    id=response["to"]["id"],
                    nickname=response["to"]["nickname"],
                    avatar=response["to"]["avatar"],
                    last_online_at=response["to"]["last_online_at"],
                    url=response["to"]["url"],
                    image=PhotoExtended(**response["to"]["image"]),
                ),
                sender=User(
                    id=response["from"]["id"],
                    nickname=response["from"]["nickname"],
                    avatar=response["from"]["avatar"],
                    last_online_at=response["from"]["last_online_at"],
                    url=response["from"]["url"],
                    image=PhotoExtended(**response["from"]["image"]),
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
            json={
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
                id=response["id"],
                body=response["body"],
                created_at=response["created_at"],
                html_body=response["html_body"],
                kind=response["kind"],
                linked=(
                    Linked(
                        name=response["linked"]["name"],
                        id=response["linked"]["id"],
                        russian=response["linked"]["russian"],
                        url=response["linked"]["url"],
                        kind=response["linked"]["kind"],
                        score=response["linked"]["score"],
                        status=response["linked"]["status"],
                        episodes=response["linked"].get("episodes"),
                        episodes_aired=response["linked"].get("episodes_aired"),
                        volumes=response["linked"].get("volumes"),
                        chapters=response["linked"].get("chapters"),
                        aired_on=response["linked"]["aired_on"],
                        released_on=response["linked"]["released_on"],
                        image=Photo(**response["linked"]["image"]),
                    )
                    if response["linked"]
                    else None
                ),
                linked_id=response["linked_id"],
                linked_type=response["linked_id"],
                read=response["read"],
                to=User(
                    id=response["to"]["id"],
                    nickname=response["to"]["nickname"],
                    avatar=response["to"]["avatar"],
                    last_online_at=response["to"]["last_online_at"],
                    url=response["to"]["url"],
                    image=PhotoExtended(**response["to"]["image"]),
                ),
                sender=User(
                    id=response["from"]["id"],
                    nickname=response["from"]["nickname"],
                    avatar=response["from"]["avatar"],
                    last_online_at=response["from"]["last_online_at"],
                    url=response["from"]["url"],
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
            json={
                "message": {
                    "body": body,
                }
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return MessageInfo(
                id=response["id"],
                body=response["body"],
                created_at=response["created_at"],
                html_body=response["html_body"],
                kind=response["kind"],
                linked=(
                    Linked(
                        name=response["linked"]["name"],
                        id=response["linked"]["id"],
                        russian=response["linked"]["russian"],
                        url=response["linked"]["url"],
                        kind=response["linked"]["kind"],
                        score=response["linked"]["score"],
                        status=response["linked"]["status"],
                        episodes=response["linked"].get("episodes"),
                        episodes_aired=response["linked"].get("episodes_aired"),
                        volumes=response["linked"].get("volumes"),
                        chapters=response["linked"].get("chapters"),
                        aired_on=response["linked"]["aired_on"],
                        released_on=response["linked"]["released_on"],
                        image=Photo(**response["linked"]["image"]),
                    )
                    if response["linked"]
                    else None
                ),
                linked_id=response["linked_id"],
                linked_type=response["linked_id"],
                read=response["read"],
                to=User(
                    id=response["to"]["id"],
                    nickname=response["to"]["nickname"],
                    avatar=response["to"]["avatar"],
                    last_online_at=response["to"]["last_online_at"],
                    url=response["to"]["url"],
                    image=PhotoExtended(**response["to"]["image"]),
                ),
                sender=User(
                    id=response["from"]["id"],
                    nickname=response["from"]["nickname"],
                    avatar=response["from"]["avatar"],
                    last_online_at=response["from"]["last_online_at"],
                    url=response["from"]["url"],
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
            json={"ids": ids, "is_read": "1" if is_read else "0"},
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
            json={"type": type},
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
            json={"type": type},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(deleteAll): status - {response.status_code}: info - {str(response)}"
        )

        return response
