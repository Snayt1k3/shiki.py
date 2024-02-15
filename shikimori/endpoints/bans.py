import logging
from typing import List

from shikimori.types.bans import Comment, Ban
from .base import BaseEndpoint
from ..exceptions import RequestError
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
                    **b,
                    comment=Comment(**b.get("comment")),
                    user=User(**b.get("user")),
                    moderator=User(**b.get("moderator")),
                )
                for b in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response
