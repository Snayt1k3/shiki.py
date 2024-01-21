import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.user.achievements import Achievement


class AchievementsEndpoint(BaseEndpoint):
    async def list(self, user_id: int) -> list[Achievement] | RequestError:
        response = await self._request.make_request(
            "GET",
            query_params={"user_id": user_id},
            headers={"User-Agent": self._user_agent},
        )

        if not isinstance(response, RequestError):
            return [Achievement(**obj) for obj in response]

        logging.debug(
            f"Bad Request(get_achievements): status - {response.status_code}: info - {str(response)}"
        )
        return response
