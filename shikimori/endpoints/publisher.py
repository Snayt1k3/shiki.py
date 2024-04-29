import logging
from typing import List

from shikimori.types.publisher import Publisher
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class PublisherEndpoint(BaseEndpoint):
    async def list(self) -> List[Publisher] | RequestError:
        """List publishers"""
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/publishers", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Publisher.from_dict(publisher) for publisher in response]

        logger.debug(
            f"Bad Request(anime_list): status - {response.status_code}: info - {str(response)}"
        )

        return response
