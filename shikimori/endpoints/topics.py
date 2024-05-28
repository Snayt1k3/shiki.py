import logging
from typing import List

from shikimori.types.topics import Topic, Status, TopicReview
from .base import BaseEndpoint
from ..exceptions import RequestError
from ..utils.filter import filter_none_parameters

logger = logging.getLogger(__name__)


class TopicsEndpoint(BaseEndpoint):
    async def list(
        self,
        page: int = None,
        limit: int = None,
        forum: str = None,
        linked_id: int = None,
        linked_type: str = None,
        type: str = None,
    ) -> List[Topic] | RequestError:
        """
        List topics.

        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum
        :param forum: Must be one of: all, animanga, site, games, vn, contests, offtopic, clubs, my_clubs, critiques, news, collections, articles, cosplay.
        :param linked_id: Used together with linked_type
        :param linked_type: Used together with linked_id. Must be one of: Anime, Manga, Ranobe, Character, Person, Club, ClubPage, Critique, Review, Contest, CosplayGallery, Collection, Article.
        :param type: Must be one of: Topic, Topics::ClubUserTopic, Topics::EntryTopic, Topics::EntryTopics::AnimeTopic, Topics::EntryTopics::ArticleTopic, Topics::EntryTopics::CharacterTopic, Topics::EntryTopics::ClubPageTopic, Topics::EntryTopics::ClubTopic, Topics::EntryTopics::CollectionTopic, Topics::EntryTopics::ContestTopic, Topics::EntryTopics::CosplayGalleryTopic, Topics::EntryTopics::MangaTopic, Topics::EntryTopics::PersonTopic, Topics::EntryTopics::RanobeTopic, Topics::EntryTopics::CritiqueTopic, Topics::EntryTopics::ReviewTopic, Topics::NewsTopic, Topics::NewsTopics::ContestStatusTopic.
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/topics",
            headers=self.headers,
            params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                    "forum": forum,
                    "linked_id": linked_id,
                    "linked_type": linked_type,
                    "type": type,
                }
            ),
        )

        if not isinstance(response, RequestError):
            return [Topic.from_dict(topic) for topic in response]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def updates(
        self, page: int = None, limit: int = None
    ) -> List[Status] | RequestError:
        """
        NewsTopics about database updates.

        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/topics/updates",
            headers=self.headers,
            params=filter_none_parameters(
                {
                    "page": page,
                    "limit": limit,
                }
            ),
        )

        if not isinstance(response, RequestError):
            return [Status.from_dict(t) for t in response]

        logger.debug(
            f"Bad Request(updates): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def hot(self, limit: int = None) -> List[Topic] | RequestError:
        """
        Hot topics.

        :param limit: 10 maximum
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/topics/hot",
            headers=self.headers,
            params=filter_none_parameters(
                {
                    "limit": limit,
                }
            ),
        )

        if not isinstance(response, RequestError):
            return [Topic.from_dict(topic) for topic in response]

        logger.debug(
            f"Bad Request(hot): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def ById(self, id: int) -> Topic | RequestError:
        """
        Show a topic.

        :param id: must be a number
        """
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/topics/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return TopicReview.from_dict(response)

        logger.debug(
            f"Bad Request(byId): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def create(
        self,
        body: str,
        forum_id: int,
        title: str,
        user_id: int,
        type: str = "Topic",
        linked_id: int = None,
        linked_type: str = None,
    ) -> Topic | RequestError:
        """
        Create a topic.

        Requires topics oauth scope.

        :param body: Must be a String.
        :param forum_id: Must be a number.
        :param title: Must be a String.
        :param user_id: Must be a number. .
        :param type: Must be one of: Topic.
        :param linked_id: Must be a number.
        :param linked_type: Must be one of: Anime, Manga, Ranobe, Character, Person, Club, ClubPage, Critique, Review, Contest, CosplayGallery, Collection, Article.
        """
        response = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/api/topics",
            headers=self.headers,
            json={
                "topic": filter_none_parameters(
                    {
                        "body": body,
                        "forum_id": forum_id,
                        "title": title,
                        "user_id": user_id,
                        "type": type,
                        "linked_id": linked_id,
                        "linked_type": linked_type,
                    }
                )
            },
        )

        if not isinstance(response, RequestError):
            return TopicReview.from_dict(response)

        logger.debug(
            f"Bad Request(create): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def update(
        self,
        id: int,
        body: str = None,
        linked_id: int = None,
        linked_type: str = None,
        title: str = None,
    ) -> Topic | RequestError:
        """
        Update a topic.

        Requires topics oauth scope.

        :param id: Must be a number.
        :param body: Must be a String.
        :param linked_id: Must be a number.
        :param linked_type: Must be one of: Anime, Manga, Ranobe, Character, Person, Club, ClubPage, Critique, Review, Contest, CosplayGallery, Collection, Article.
        :param title: Must be a String.
        """
        response = await self._request.make_request(
            "PATCH",
            url=f"{self._base_url}/api/topics/{id}",
            headers=self.headers,
            json={
                "topic": filter_none_parameters(
                    {
                        "body": body,
                        "title": title,
                        "linked_id": linked_id,
                        "linked_type": linked_type,
                    }
                )
            },
        )

        if not isinstance(response, RequestError):
            return TopicReview.from_dict(response)

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def delete(self, id: int) -> None | RequestError:
        """
        Destroy a topic.

        Requires topics oauth scope.

        :param id: Must be a number
        """
        response = await self._request.make_request(
            "DELETE",
            url=f"{self._base_url}/api/topics/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return response["notice"]

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )
        return response
