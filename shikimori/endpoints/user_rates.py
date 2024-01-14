import logging

from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..types.user_rates import UserRateResponse, UserRateCreate, UserRateUpdate
from ..utils.filter import filter_none_parameters


class UserRatesEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def get(self, id: int) -> UserRateResponse | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/v2/user_rates/{id}",
            headers={"User-Agent": self._user_agent},
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
            headers={"User-Agent": self._user_agent},
        )

        if not isinstance(response, RequestError):
            return [UserRateResponse(**obj) for obj in response]

        logging.debug(
            f"Bad Request(get_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self, user_rate: UserRateCreate, access_token: str
    ) -> UserRateResponse | RequestError:
        """
        Requires user_rates oauth scope
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}api/v2/user_rates",
            body={"user_rate": filter_none_parameters(user_rate.to_dict())},
            headers={
                "Authorization": f"Bearer {access_token}",
                "User-Agent": self._user_agent,
            },
        )

        if not isinstance(response, RequestError):
            return UserRateResponse(**response)

        logging.debug(
            f"Bad Request(create_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, user_rate_id: int, user_rate: UserRateUpdate, access_token: str
    ) -> UserRateResponse | RequestError:
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}",
            body=filter_none_parameters(user_rate.to_dict()),
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return UserRateResponse(**response)

        logging.debug(
            f"Bad Request(update_user_rate): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def increment(
        self, user_rate_id: int, access_token: str
    ) -> UserRateResponse | RequestError:
        """Increment episodes/chapters by 1"""
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}/increment",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )

        if not isinstance(response, RequestError):
            return UserRateResponse(**response)

        logging.debug(
            f"Bad Request(increment): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(
        self, user_rate_id: int, access_token: str
    ) -> None | RequestError:
        """
        Destroy a user rate
        :param user_rate_id: must be a number.
        :param access_token: auth token.
        :return: None - Success, RequestError - Error.
        """

        return await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/v2/user_rates/{user_rate_id}",
            headers={
                "User-Agent": self._user_agent,
                "Authorization": f"Bearer {access_token}",
            },
        )
