import logging
from typing import List

from shikimori.types.videos import Video
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class VideosEndpoint(BaseEndpoint):
    async def list(self, id: int) -> List[Video] | RequestError:
        """
        List videos.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/animes/{id}/videos",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Video.from_dict(v) for v in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self, id: int, kind: str, url: str, name: str
    ) -> Video | RequestError:
        """
        Create a video.

        Requires content oauth scope.

        :param id: must be a number
        :param kind: Must be one of: pv, character_trailer, cm, op, ed, op_ed_clip, clip, other, episode_preview.
        :param url: Supported hostings: YouTube,vk,ok,coub,rutube,vimeo,sibnet,yandex,streamable,smotret_anime,myvi,youmite,viuly,stormo,mediafile
        :param name: must be a string.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/animes/{id}/videos",
            json={"video": {"url": url, "kind": kind, "name": name}},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Video.from_dict(response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, anime_id: int, id: int) -> None | RequestError:
        """
        Destroy a video.

        Requires content oauth scope.

        :param anime_id: must be a number
        :param id: must be a number
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/animes/{anime_id}/videos/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
