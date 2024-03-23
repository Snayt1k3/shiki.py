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
            return [
                Dialog(
                    target_user=User(
                        id=s["target_user"]["id"],
                        nickname=s["target_user"]["nickname"],
                        avatar=s["target_user"]["avatar"],
                        last_online_at=s["target_user"]["last_online_at"],
                        url=s["target_user"]["url"],
                        image=PhotoExtended(**s["target_user"]["image"]),
                    ),
                    message=Message(
                        id=s["message"]["id"],
                        body=s["message"]["body"],
                        html_body=s["message"]["html_body"],
                        created_at=s["message"]["created_at"],
                        read=s["message"]["read"],
                        kind=s["message"]["kind"],
                        linked_id=s["message"]["linked_id"],
                        linked_type=s["message"]["linked_type"],
                        linked=(
                            Linked(
                                name=s["message"]["linked"]["name"],
                                id=s["message"]["linked"]["id"],
                                russian=s["message"]["linked"]["russian"],
                                url=s["message"]["linked"]["url"],
                                kind=s["message"]["linked"]["kind"],
                                score=s["message"]["linked"]["score"],
                                status=s["message"]["linked"]["status"],
                                episodes=s["message"]["linked"]["episodes"],
                                episodes_aired=s["message"]["linked"]["episodes_aired"],
                                aired_on=s["message"]["linked"]["aired_on"],
                                released_on=s["message"]["linked"]["released_on"],
                                image=Photo(**s["message"]["linked"]["image"]),
                            )
                            if s["message"]["linked"]
                            else None
                        ),
                    ),
                )
                for s in response
            ]

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
            return [
                MessageInfo(
                    id=s["id"],
                    kind=s["kind"],
                    body=s["body"],
                    html_body=s["html_body"],
                    created_at=s["created_at"],
                    linked_id=s["linked_id"],
                    linked_type=s["linked_type"],
                    read=s["read"],
                    linked=(
                        Linked(
                            name=s["linked"]["name"],
                            id=s["linked"]["id"],
                            russian=s["linked"]["russian"],
                            url=s["linked"]["url"],
                            kind=s["linked"]["kind"],
                            score=s["linked"]["score"],
                            status=s["linked"]["status"],
                            episodes=s["linked"]["episodes"],
                            episodes_aired=s["linked"]["episodes_aired"],
                            aired_on=s["linked"]["aired_on"],
                            released_on=s["linked"]["released_on"],
                            image=Photo(**s["linked"]["image"]),
                        )
                        if s["linked"]
                        else None
                    ),
                    to=User(
                        id=s["to"]["id"],
                        avatar=s["to"]["avatar"],
                        image=PhotoExtended(**s["to"]["image"]),
                        last_online_at=s["to"]["last_online_at"],
                        nickname=s["to"]["nickname"],
                        url=s["to"]["url"],
                    ),
                    sender=User(
                        id=s["from"]["id"],
                        avatar=s["from"]["avatar"],
                        image=PhotoExtended(**s["from"]["image"]),
                        last_online_at=s["from"]["last_online_at"],
                        nickname=s["from"]["nickname"],
                        url=s["from"]["url"],
                    ),
                )
                for s in response
            ]

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
