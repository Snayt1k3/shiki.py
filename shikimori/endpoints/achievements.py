import logging

from shikimori.types.achievements import Achievement
from .base import BaseEndpoint
from ..exceptions import RequestError

logger = logging.getLogger(__name__)


class AchievementsEndpoint(BaseEndpoint):
    async def list(self, user_id: int) -> list[Achievement] | RequestError:
        """
        List user achievements.

        :param user_id: Must be a number.
        """
        response = await self._request.make_request(
            "GET",
            params={"user_id": user_id},
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Achievement.from_dict(obj) for obj in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )
        return response
