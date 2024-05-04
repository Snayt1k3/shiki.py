import logging

from shikimori.types.abuse_requests import AbuseRequest
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class AbuseRequestEndpoint(BaseEndpoint):
    async def AsOfftopic(self, comment_id: str | int) -> AbuseRequest | RequestError:
        """
        Mark comment as offtopic
        Request will be sent to moderators.

        :param comment_id: Must be a number.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/offtopic",
            headers=self.headers,
            json={"comment_id": comment_id},
        )

        if not isinstance(response, RequestError):
            return AbuseRequest.from_dict(response)

        logger.debug(
            f"Bad Request(mark_comment_as_offtopic): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def AsReview(
        self, topic_id: str | int = None, comment_id: str | int = None
    ) -> None | RequestError:
        """
        Convert comment to review.

        Request will be sent to moderators.

        :param topic_id: Must be a number.
        :param comment_id: Must be a number.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers=self.headers,
            json=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logger.debug(
            f"Bad Request(convert_comment_to_review): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def CreateViolation(
        self,
        topic_id: str | int = None,
        comment_id: str | int = None,
        reason: str = None,
    ) -> None | RequestError:
        """
        Create abuse about violation of site rules.

        Request will be sent to moderators.

        :param comment_id: Must be a number.
        :param topic_id: Must be a number.
        :param reason: Must be a string.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/abuse",
            headers=self.headers,
            json=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id, "reason": reason}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logger.debug(
            f"Bad Request(create_abuse_about_violation_of_site_rules): status - {response.status_code}: info - {str(response)}"  # NOQA
        )

        return response

    async def SpoilerInContent(
        self,
        topic_id: str | int = None,
        comment_id: str | int = None,
        reason: str = None,
    ) -> None | RequestError:
        """
        Create abuse about spoiler in content
        Request will be sent to moderators.

        :param comment_id: Must be a number.
        :param topic_id: Must be a number.
        :param reason: Must be a string.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/spoiler",
            headers=self.headers,
            json=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id, "reason": reason}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logger.debug(
            f"Bad Request(create_abuse_about_spoiler_in_content): status - {response.status_code}: info - {str(response)}"  # NOQA
        )

        return response
