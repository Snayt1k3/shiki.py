import logging

from shikimori.types.review import Review
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class ReviewEndpoint(BaseEndpoint):
    async def create(
        self, anime_id: int, body: str, opinion: str
    ) -> Review | RequestError:
        """
        Create a review.

        :param anime_id: Must be a number.
        :param body: Must be a String
        :param opinion: Must be one of: positive, neutral, negative
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/reviews",
            json={
                "review": filter_none_parameters(
                    {"anime_id": anime_id, "body": body, "opinion": opinion}
                )
            },
        )

        if not isinstance(response, RequestError):
            return Review.from_dict(response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(self, id: int, body: str, opinion: str) -> Review | RequestError:
        """
        Update a review.

        :param id: Must be a number.
        :param body: Must be a String
        :param opinion: Must be one of: positive, neutral, negative
        """
        response = await self._request.make_request(
            "PATCH",
            headers=self.headers,
            url=f"{self._base_url}/api/reviews/{id}",
            json={"review": filter_none_parameters({"body": body, "opinion": opinion})},
        )

        if not isinstance(response, RequestError):
            return Review.from_dict(response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> Review | RequestError:
        """
        Destroy a review.

        :param id: Must be a number.
        """
        response = await self._request.make_request(
            "DELETE",
            headers=self.headers,
            url=f"{self._base_url}/api/reviews/{id}",
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
