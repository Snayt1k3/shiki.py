import logging

from .base import BaseEndpoint
from shikimori.types.general.topic_ignore import Topic
from ..exceptions import RequestError


class TopicIgnoreEndpoint(BaseEndpoint):
    async def ignore(self, topic_id: str | int) -> Topic | RequestError:
        """
        ignore topic.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Topic(**response)

        logging.debug(
            f"Bad Request(ignore): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def unignore(
        self,
        topic_id: str | int,
    ) -> Topic | RequestError:
        """
        unignore topic.

        Requires oauth scope
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Topic(**response)

        logging.debug(
            f"Bad Request(unignore): status - {response.status_code}: info - {str(response)}"
        )

        return response
