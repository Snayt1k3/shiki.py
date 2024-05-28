import logging

from shikimori.types.photo import UserImage
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class UserImageEndpoint(BaseEndpoint):
    async def upload(
        self, image: str, linked_type: str = None
    ) -> UserImage | RequestError:
        """
        Create a user image.

        Requires comments oauth scope.

        :param image: Must be a String
        :param linked_type: Must be a String
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/user_images",
            headers=self.headers,
            json=filter_none_parameters({"image": image, "linked_type": linked_type}),
        )

        if not isinstance(response, RequestError):
            return UserImage.from_dict(response)

        logger.debug(
            f"Bad Request(upload): status - {response.status_code}: info - {str(response)}"
        )

        return response
