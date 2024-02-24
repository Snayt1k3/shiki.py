import logging
from typing import List

from shikimori.types.bans import Comment, Ban
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..types.photo import PhotoExtended
from ..types.user import User

logger = logging.getLogger(__name__)


class BanEndpoint(BaseEndpoint):
    async def list(self) -> List[Ban] | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/bans",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [
                Ban(
                    id=b["id"],
                    created_at=b["created_at"],
                    duration_minutes=b["duration_minutes"],
                    moderator_id=b["moderator_id"],
                    reason=b["reason"],
                    user_id=b["user_id"],
                    comment=Comment(**b["comment"]),
                    user=User(
                        id=b["user"]["id"],
                        avatar=b["user"]["avatar"],
                        image=PhotoExtended(**b["user"]["image"]),
                        last_online_at=b["user"]["last_online_at"],
                        nickname=b["user"]["nickname"],
                        url=b["user"]["url"],
                    ),
                    moderator=User(
                        id=b["moderator"]["id"],
                        avatar=b["moderator"]["avatar"],
                        image=PhotoExtended(**b["moderator"]["image"]),
                        last_online_at=b["moderator"]["last_online_at"],
                        nickname=b["moderator"]["nickname"],
                        url=b["moderator"]["url"],
                    ),
                )
                for b in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
