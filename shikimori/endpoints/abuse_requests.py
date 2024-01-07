import logging

from .base import BaseEndpoint
from ..types.abuse_requests import AbuseRequest
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..utils.filter import filter_none_parameters


class AbuseRequestEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

    async def mark_comment_as_offtopic(
        self, comment_id: str | int
    ) -> AbuseRequest | RequestError:
        """
        Mark comment as offtopic
        Request will be sent to moderators.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/offtopic",
            headers={
                "User-Agent": self._user_agent,
            },
            body={"comment_id": comment_id},
        )

        if not isinstance(response, RequestError):
            return AbuseRequest(**response)

        logging.debug(
            f"Bad Request(mark_comment_as_offtopic): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def convert_comment_to_review(
        self, topic_id: str | int = None, comment_id: str | int = None
    ) -> None | RequestError:
        """
        Convert comment to review
        Request will be sent to moderators.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/topics/{topic_id}/ignore",
            headers={
                "User-Agent": self._user_agent,
            },
            body=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logging.debug(
            f"Bad Request(convert_comment_to_review): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def create_abuse_about_violation_of_site_rules(
        self,
        topic_id: str | int = None,
        comment_id: str | int = None,
        reason: str = None,
    ) -> None | RequestError:
        """
        Create abuse about violation of site rules
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/abuse",
            headers={
                "User-Agent": self._user_agent,
            },
            body=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id, "reason": reason}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logging.debug(
            f"Bad Request(create_abuse_about_violation_of_site_rules): status - {response.status_code}: info - {str(response)}"  # NOQA
        )

        return response

    async def create_abuse_about_spoiler_in_content(
        self,
        topic_id: str | int = None,
        comment_id: str | int = None,
        reason: str = None,
    ) -> None | RequestError:
        """
        Create abuse about violation of site rules
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/v2/abuse_requests/spoiler",
            headers={
                "User-Agent": self._user_agent,
            },
            body=filter_none_parameters(
                {"topic_id": topic_id, "comment_id": comment_id, "reason": reason}
            ),
        )

        if not isinstance(response, RequestError):
            return None

        logging.debug(
            f"Bad Request(create_abuse_about_spoiler_in_content): status - {response.status_code}: info - {str(response)}"  # NOQA
        )

        return response