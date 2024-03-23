import logging
from typing import List

from shikimori.types.comment import Comment
from shikimori.types.photo import PhotoExtended
from shikimori.types.user import User
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
        :param commentable_id: number
        :param commentable_type: Must be one of: Topic, User.
        :param page: Must be a number between 1 and 100000
        :param limit: 30 maximum
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
            return [
                Comment(
                    id=s["id"],
                    body=s["body"],
                    commentable_id=s["commentable_id"],
                    commentable_type=s["commentable_type"],
                    created_at=s["created_at"],
                    can_be_edited=s["can_be_edited"],
                    is_offtopic=s["is_offtopic"],
                    html_body=s["html_body"],
                    user_id=s["user_id"],
                    is_summary=s["is_summary"],
                    updated_at=s["updated_at"],
                    user=User(
                        id=s["user"]["id"],
                        avatar=s["user"]["avatar"],
                        url=s["user"]["url"],
                        last_online_at=s["user"]["last_online_at"],
                        nickname=s["user"]["nickname"],
                        image=PhotoExtended(**s["user"]["image"]),
                    ),
                )
                for s in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> Comment | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/comments/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Comment(
                    id=response["id"],
                    body=response["body"],
                    commentable_id=response["commentable_id"],
                    commentable_type=response["commentable_type"],
                    created_at=response["created_at"],
                    can_be_edited=response["can_be_edited"],
                    is_offtopic=response["is_offtopic"],
                    html_body=response["html_body"],
                    user_id=response["user_id"],
                    is_summary=response["is_summary"],
                    updated_at=response["updated_at"],
                    user=User(
                        id=response["user"]["id"],
                        avatar=response["user"]["avatar"],
                        url=response["user"]["url"],
                        last_online_at=response["user"]["last_online_at"],
                        nickname=response["user"]["nickname"],
                        image=PhotoExtended(**response["user"]["image"]),
                    ),
                )

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
        requires oauth scope
        :param broadcast: Must be one of: true, false
        :param body: Must be a String
        :param commentable_id: Must be a number.
        :param commentable_type: Must be one of: Topic, User, Anime, Manga, Character, Person, Article, Club, ClubPage, Collection, Critique, Review
        :param is_offtopic: Must be one of: true, false
        :param frontend: Must be one of: true, false
        """

        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/comments",
            body=filter_none_parameters(
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
            return Comment(
                    id=response["id"],
                    body=response["body"],
                    commentable_id=response["commentable_id"],
                    commentable_type=response["commentable_type"],
                    created_at=response["created_at"],
                    can_be_edited=response["can_be_edited"],
                    is_offtopic=response["is_offtopic"],
                    html_body=response["html_body"],
                    user_id=response["user_id"],
                    is_summary=response["is_summary"],
                    updated_at=response["updated_at"],
                    user=User(
                        id=response["user"]["id"],
                        avatar=response["user"]["avatar"],
                        url=response["user"]["url"],
                        last_online_at=response["user"]["last_online_at"],
                        nickname=response["user"]["nickname"],
                        image=PhotoExtended(**response["user"]["image"]),
                    ),
                )

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, id: int, body: str, frontend: bool = None
    ) -> Comment | RequestError:
        """
        Update a comment. requires oauth scope
        Use abuse_requests to change is_offtopic field.
        :param body: string.
        :param frontend: string.
        """

        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}api/comments/{id}",
            body=filter_none_parameters(
                {"comment": {"body": body}, "frontend": frontend}
            ),
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Comment(
                    id=response["id"],
                    body=response["body"],
                    commentable_id=response["commentable_id"],
                    commentable_type=response["commentable_type"],
                    created_at=response["created_at"],
                    can_be_edited=response["can_be_edited"],
                    is_offtopic=response["is_offtopic"],
                    html_body=response["html_body"],
                    user_id=response["user_id"],
                    is_summary=response["is_summary"],
                    updated_at=response["updated_at"],
                    user=User(
                        id=response["user"]["id"],
                        avatar=response["user"]["avatar"],
                        url=response["user"]["url"],
                        last_online_at=response["user"]["last_online_at"],
                        nickname=response["user"]["nickname"],
                        image=PhotoExtended(**response["user"]["image"]),
                    ),
                )


        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int) -> str | RequestError:
        """requires oauth scope"""
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
