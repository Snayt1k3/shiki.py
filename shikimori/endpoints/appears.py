import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class AppearsEndpoint(BaseEndpoint):
    async def read(self, ids: str = None) -> None | RequestError:
        """
        Mark comments or topics as read.

        :param ids: str like 'comment-7,comment-8,topic-270101'.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/appears",
            headers=self.headers,
            json=filter_none_parameters({"ids": ids}),
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(mark): status - {response.status_code}: info - {str(response)}"
        )

        return response
