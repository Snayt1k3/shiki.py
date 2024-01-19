import logging

from .base import BaseEndpoint
from ..types.topic_ignore import Topic
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter


class TopicIgnoreEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def ignore(
        self, topic_id: str | int, access_token: str
    ) -> Topic | RequestError:
        """
        ignore topic.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return Topic(**response)

        logging.debug(
            f"Bad Request(ignore): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def unignore(
        self, topic_id: str | int, access_token: str
    ) -> Topic | RequestError:
        """
        unignore topic.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return Topic(**response)

        logging.debug(
            f"Bad Request(unignore): status - {response.status_code}: info - {str(response)}"
        )

        return response
