import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..utils.filter import filter_none_parameters


class AppearsEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def markRead(self, ids: str = None) -> None | RequestError:
        """
        Mark comments or topics as read
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/appears",
            headers={
                "User-Agent": self._user_agent,
            },
            body=filter_none_parameters({"ids": ids})
        )

        if not isinstance(response, RequestError):
            return

        logging.debug(
            f"Bad Request(mark): status - {response.status_code}: info - {str(response)}"
        )

        return response
