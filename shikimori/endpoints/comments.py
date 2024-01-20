import logging
from typing import List
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..requestLimiter import RequestLimiter
from ..types.general.comment import Comment
from ..utils.filter import filter_none_parameters
from ..types.user.user import User
from ..types.general.photo import PhotoExtended


class CommentEndpoint(BaseEndpoint):
    def __init__(self, base_url: str, request: RequestLimiter, user_agent: str):
        super().__init__(base_url, request, user_agent)

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
        :return:
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/comments",
            query_params=filter_none_parameters(
                {
                    "commentable_id": commentable_id,
                    "commentable_type": commentable_type,
                    "page": page,
                    "limit": limit,
                    "desc": desc,
                }
            ),
            headers=self.base_headers(self._user_agent),
        )

        if not isinstance(response, RequestError):
            return [
                Comment(
                    **response,
                    user=User(**s["user"], image=PhotoExtended(**s["user"]["image"])),
                )
                for s in response
            ]

        logging.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def ById(self, id: int) -> Comment | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/comments/{id}",
            headers=self.base_headers(self._user_agent),
        )

        if not isinstance(response, RequestError):
            return Comment(
                **response,
                user=User(
                    **response["user"], image=PhotoExtended(**response["user"]["image"])
                ),
            )

        logging.debug(
            f"Bad Request(ById): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def create(
        self,
        access_token: str,
        broadcast: bool = None,
        body: str = None,
        commentable_id: int = None,
        commentable_type: str = None,
        is_offtopic: bool = None,
        frontend: bool = None,
    ):
        """
        :param broadcast: Must be one of: true, false
        :param body: Must be a String
        :param commentable_id: Must be a number.
        :param commentable_type: Must be one of: Topic, User, Anime, Manga, Character, Person, Article, Club, ClubPage, Collection, Critique, Review
        :param is_offtopic: Must be one of: true, false
        :param frontend: Must be one of: true, false
        :param access_token: auth token
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
            headers=self.base_headers(self._user_agent),
        )

        if not isinstance(response, RequestError):
            return Comment(
                **response,
                user=User(
                    **response["user"], image=PhotoExtended(**response["user"]["image"])
                ),
            )

        logging.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def update(
        self, id: int, access_token: str, body: str, frontend: bool = None
    ) -> Comment | RequestError:
        """
        Update a comment.
        Use abuse_requests to change is_offtopic field.
        :param access_token: auth token
        :param body: string.
        :param frontend: string.
        """

        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}api/comments/{id}",
            body=filter_none_parameters(
                {"comment": {"body": body}, "frontend": frontend}
            ),
            headers=self.auth_headers(self._user_agent, access_token),
        )

        if not isinstance(response, RequestError):
            return Comment(
                **response,
                user=User(
                    **response["user"], image=PhotoExtended(**response["user"]["image"])
                ),
            )

        logging.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )

        return response

    async def delete(self, id: int, access_token: str) -> str | RequestError:
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/comments/{id}",
            headers=self.auth_headers(self._user_agent, access_token),
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logging.debug(
            f"Bad Request(delete): status - {response.status_code}: info - {str(response)}"
        )

        return response

