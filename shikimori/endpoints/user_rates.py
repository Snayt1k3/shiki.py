import logging

from shikimori.types.user_rates import UserRate
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class UserRatesEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> UserRate | RequestError:
        """
        Show a user rate.

        :param id: must be a number
        """

        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/v2/user_rates/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRate.from_dict(response)

        logger.debug(
            f"Bad Request(get_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def list(
        self,
        user_id: int = None,
        target_id: int = None,
        target_type: str = None,
        status: str = None,
        page: int = None,
        limit: int = None,
    ) -> list[UserRate] | RequestError:
        """
        List user rates.

        :param user_id: must be a number
        :param target_id: must be a number
        :param target_type: Must be one of: Anime, Manga
        :param status: must be one of: planned, watching, rewatching, completed, on_hold, dropped
        :param page: must be a number
        :param limit: must be a number (Maximum - 1000)
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/v2/user_rates",
            params=filter_none_parameters(
                {
                    "user_id": user_id,
                    "target_id": target_id,
                    "target_type": target_type,
                    "status": status,
                    "page": page,
                    "limit": limit,
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [UserRate.from_dict(user_rate) for user_rate in response]

        logger.debug(
            f"Bad Request(get_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self,
        user_id: int,
        target_id: int,
        target_type: str,
        status: str | None = None,
        score: int | None = None,
        chapters: int | None = None,
        episodes: int | None = None,
        volumes: int | None = None,
        rewatches: int | None = None,
        text: str | None = None,
    ) -> UserRate | RequestError:
        """
        Create a user rate.

        Requires user_rates oauth scope.

        :param text: Must be a String
        :param rewatches: Must be a number.
        :param volumes: Must be a number.
        :param episodes: Must be a number.
        :param chapters: Must be a number.
        :param score: Must be a number.
        :param status: Must be one of: planned, watching, rewatching, completed, on_hold, dropped
        :param target_type:  Must be one of: Anime, Manga.
        :param target_id: Must be a number.
        :param user_id: Must be a number.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/user_rates",
            json={
                "user_rate": filter_none_parameters(
                    {
                        "user_id": user_id,
                        "target_id": target_id,
                        "target_type": target_type,
                        "status": status,
                        "chapters": chapters,
                        "volumes": volumes,
                        "rewatches": rewatches,
                        "text": text,
                        "score": score,
                        "episodes": episodes,
                    }
                )
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRate.from_dict(response)

        logger.debug(
            f"Bad Request(create_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self,
        user_rate_id: int,
        status: str | None = None,
        score: int | None = None,
        chapters: int | None = None,
        episodes: int | None = None,
        volumes: int | None = None,
        rewatches: int | None = None,
        text: str | None = None,
    ) -> UserRate | RequestError:
        """
        Update a user rate.

        Requires user_rates oauth scope.

        :param user_rate_id: Must be a number.
        :param status: Must be a number.
        :param score: Must be a number.
        :param chapters: Must be a number.
        :param episodes: Must be a number.
        :param volumes: Must be a number.
        :param rewatches: Must be a number.
        :param text: Must be a String
        """
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}",
            body={
                "user_rate": filter_none_parameters(
                    {
                        "status": status,
                        "score": score,
                        "chapters": chapters,
                        "episodes": episodes,
                        "volumes": volumes,
                        "rewatches": rewatches,
                        "text": text,
                    }
                )
            },
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRate.from_dict(response)

        logger.debug(
            f"Bad Request(update_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def increment(self, id: int) -> UserRate | RequestError:
        """
        requires user_rates oauth scope.

        Increment episodes/chapters by 1.

        :param id:  Must be a number.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/user_rates/{id}/increment",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRate.from_dict(response)

        logger.debug(
            f"Bad Request(increment): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> None | RequestError:
        """
        Destroy a user rate.

        requires user_rates oauth scope.

        :param id: must be a number.
        """

        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/user_rates/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def cleanup(self, type: str) -> dict | RequestError:
        """
        Be careful to use.

        :param type: Must be one of: anime, manga.
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/user_rates/{type}/cleanup",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(cleanup): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def reset(self, type: str) -> dict | RequestError:
        """
        Be careful to use.

        Reset all user scores to 0.

        :param type: Must be one of: anime, manga.
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/user_rates/{type}/reset",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response

        logger.debug(
            f"Bad Request(reset): status - {response.status_code}: info - {str(response)}"
        )

        return response
