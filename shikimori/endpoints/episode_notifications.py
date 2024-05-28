import logging

from shikimori.types.episode_notification import EpisodeNotification
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class EpisodeNotificationEndpoint(BaseEndpoint):
    async def notify(
        self,
        token: str,
        anime_id: int,
        episode: int,
        aired_at: str,
        is_fandub: bool = None,
        is_raw: bool = None,
        is_subtitles: bool = None,
        is_anime365: bool = None,
    ) -> EpisodeNotification | RequestError:
        """
        Notify shikimori about anime episode release.

        :param token: Private token required to access this api
        :param anime_id: Must be a number.
        :param episode: Must be a number.
        :param aired_at: Must be a date in iso8601 YYYY-MM-DDThh:mm:ss±hh format
        :param is_fandub: Must be one of: true, false, 1, 0.
        :param is_raw: Must be one of: true, false, 1, 0.
        :param is_subtitles: Must be one of: true, false, 1, 0.
        :param is_anime365: Must be one of: true, false, 1, 0.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/episode_notifications",
            json={
                "episode_notification": filter_none_parameters(
                    {
                        "anime_id": anime_id,
                        "episode": episode,
                        "aired_at": aired_at,
                        "is_fandub": is_fandub,
                        "is_raw": is_raw,
                        "is_subtitles": is_subtitles,
                        "is_anime365": is_anime365,
                    }
                ),
                "token": token,
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return EpisodeNotification.from_dict(response)

        logger.debug(
            f"Bad Request(notify): status - {response.status_code}: info - {str(response)}"
        )

        return response
