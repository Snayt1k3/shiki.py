import logging
from typing import List

from shikimori.types.comment import Comment
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class CommentEndpoint(BaseEndpoint):
    async def list(
        self,
        commentable_id: int = None,
        commentable_type: str = None,
        page: int = None,
        limit: int = None,
        desc: int = None,
    ) -> List[Comment] | RequestError:
        """
        List comments.

        :param commentable_id: must be a number.
        :param commentable_type: Must be one of: Topic, User.
        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum.
        :param desc: Must be one of: 1, 0.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/comments",
            params=filter_none_parameters(
                {
                    "commentable_id": commentable_id,
                    "commentable_type": commentable_type,
                    "page": page,
                    "limit": limit,
                    "desc": desc,
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return [Comment.from_dict(com) for com in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> Comment | RequestError:
        """
        Show a comment.

        :param id: must be a number.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/comments/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Comment.from_dict(response)

        logger.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self,
        broadcast: bool = None,
        body: str = None,
        commentable_id: int = None,
        commentable_type: str = None,
        is_offtopic: bool = None,
        frontend: bool = None,
    ):
        """
        Create a comment.

        Requires comments oauth scope.

        :param broadcast: Must be one of: true, false.
        :param body: Must be a String.
        :param commentable_id: Must be a number.
        :param commentable_type: Must be one of: Topic, User, Anime, Manga, Character, Person, Article, Club, ClubPage, Collection, Critique, Review.  # NOQA
        :param is_offtopic: Must be one of: true, false.
        :param frontend: Must be one of: true, false.
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/comments",
            json=filter_none_parameters(
                {
                    "broadcast": broadcast,
                    "comment": filter_none_parameters(
                        {
                            "body": body,
                            "commentable_id": commentable_id,
                            "commentable_type": commentable_type,
                            "is_offtopic": is_offtopic,
                        }
                    ),
                    "frontend": frontend,
                }
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Comment.from_dict(response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, id: int, body: str, frontend: bool = None
    ) -> Comment | RequestError:
        """
        Update a comment. Requires comments oauth scope.

        Use abuse_requests to change is_offtopic field.

        :param body: string.
        :param frontend: string.
        """

        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/comments/{id}",
            json=filter_none_parameters(
                {"comment": {"body": body}, "frontend": frontend}
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Comment.from_dict(response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> str | RequestError:
        """
        Destroy a comment.
        Requires comments oauth scope.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/comments/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response
