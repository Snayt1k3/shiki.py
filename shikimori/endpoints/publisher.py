import logging
from typing import List
from .base import BaseEndpoint
from shikimori.types.general.publisher import Publisher
from shikimori.types.titles.manga import Manga
from shikimori.types.general.photo import Photo, PhotoExtended
from shikimori.types.titles.studios import Studio
from shikimori.types.titles.screenshots import ScreenShot
from shikimori.types.titles.videos import Video
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters
from shikimori.types.titles.roles import Role, Character
from shikimori.types.titles.franchise import Franchise, Node, Link
from shikimori.types.general.topics import Topic, Forum, Linked
from ..types.user import User

logger = logging.getLogger(__name__)


class PublisherEndpoint(BaseEndpoint):
    async def list(self) -> List[Publisher] | RequestError:
        response = await self._request.make_request(
            "GET", url=f"{self._base_url}/api/publishers", headers=self.headers
        )

        if not isinstance(response, RequestError):
            return [Publisher(**v) for v in response]

        logger.debug(
            f"Bad Request(anime_list): status - {response.status_code}: info - {str(response)}"
        )

        return response
