from .base import BaseEndpoint
from ..types.episode_notification import (
    EpisodeNotification,
    EpisodeNotificationResponse,
)
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
import logging


class EpisodeNotificationEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def notify(
        self, episode: EpisodeNotification, token: str
    ) -> EpisodeNotificationResponse | RequestError:
        """
        :param episode: EpisodeNotifications obj
        :param token: Private token required to access this api
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/episode_notifications",
            body={"episode_notification": episode.to_dict(), "token": token},
            headers={"User-Agent": self._user_agent},
        )

        if not isinstance(response, RequestError):
            return EpisodeNotificationResponse(**response)

        logging.debug(
            f"Bad Request(notify_shikimori_about_anime_episode): status - {response.status_code}: info - {str(response)}"
        )

        return response
