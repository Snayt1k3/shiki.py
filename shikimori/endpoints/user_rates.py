import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.user.user_rates import UserRateResponse
from ..utils.filter import filter_none_parameters


class UserRatesEndpoint(BaseEndpoint):
    async def ById(self, id: int) -> UserRateResponse | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/v2/user_rates/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRateResponse(**response)

        logging.debug(
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
    ) -> list[UserRateResponse] | RequestError:
        """
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
            query_params=filter_none_parameters(
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
            return [UserRateResponse(**obj) for obj in response]

        logging.debug(
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
    ) -> UserRateResponse | RequestError:
        """
        Requires oauth scope
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}api/v2/user_rates",
            body={
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
            return UserRateResponse(**response)

        logging.debug(
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
    ) -> UserRateResponse | RequestError:
        """
        requires oauth scope
        :param user_rate_id:
        :param status:
        :param score:
        :param chapters:
        :param episodes:
        :param volumes:
        :param rewatches:
        :param text:
        :return:
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
            return UserRateResponse(**response)

        logging.debug(
            f"Bad Request(update_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def increment(self, user_rate_id: int) -> UserRateResponse | RequestError:
        """
        requires oauth scope.
        Increment episodes/chapters by 1
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}/increment",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return UserRateResponse(**response)

        logging.debug(
            f"Bad Request(increment): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, user_rate_id: int) -> None | RequestError:
        """
        Destroy a user rate.
        requires oauth scope
        :param user_rate_id: must be a number.
        :return: None - Success, RequestError - Error.
        """

        return await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}",
            headers=self.headers,
        )
