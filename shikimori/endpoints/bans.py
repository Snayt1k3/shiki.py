from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from typing import List
from ..types.user import User
from ..types.bans import Comment, Ban


class BanEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def list(self) -> List[Ban] | RequestError:
        response = await self._request.make_request("GET", url=f"{self._base_url}/api/bans",
                                                    headers={"User-Agent": self._user_agent})

        if not isinstance(response, RequestError):
            return [
                Ban(**b, comment=Comment(**b.get("comment")), user=User ** b.get("user"),
                    moderator=User(**b.get("moderator"))) for b in response
            ]
        return response
