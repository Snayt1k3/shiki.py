from .base import BaseEndpoint
from shikimori.types.general.episode_notification import (
    EpisodeNotification,
    EpisodeNotificationResponse,
)
from ..exceptions import RequestError
import logging


class EpisodeNotificationEndpoint(BaseEndpoint):
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
            headers=self._headers(),
        )

        if not isinstance(response, RequestError):
            return EpisodeNotificationResponse(**response)

        logging.debug(
            f"Bad Request(notify_shikimori_about_anime_episode): status - {response.status_code}: info - {str(response)}"
        )

        return response
