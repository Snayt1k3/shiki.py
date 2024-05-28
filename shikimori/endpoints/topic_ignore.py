import logging

from shikimori.types.topic_ignore import Topic
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class TopicIgnoreEndpoint(BaseEndpoint):
    async def ignore(self, topic_id: str | int) -> Topic | RequestError:
        """
        ignore topic.

        Requires topics oauth scope.

        :param topic_id: Must be a number
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Topic.from_dict(response)

        logger.debug(
            f"Bad Request(ignore): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def unignore(
        self,
        topic_id: str | int,
    ) -> Topic | RequestError:
        """
        unignore topic.

        Requires topics oauth scope.

        :param topic_id: must be a number
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Topic.from_dict(response)

        logger.debug(
            f"Bad Request(unignore): status - {response.status_code}: info - {str(response)}"
        )

        return response
