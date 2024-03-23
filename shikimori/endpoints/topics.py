import logging
from typing import List

from .base import BaseEndpoint
from ..exceptions import RequestError
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.topics import Topic, Forum, Linked, Status, ReviewLinked, Title
from shikimori.types.user import User
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

        :param page: Must be a number between 1 and 100000.
        :param limit: 30 maximum
        :param forum: Must be one of: all, animanga, site, games, vn, contests, offtopic, clubs, my_clubs, critiques, news, collections, articles, cosplay.
        :param linked_id: Used together with linked_type
        :param linked_type: Used together with linked_id.
        Must be one of: Anime, Manga, Ranobe, Character, Person, Club, ClubPage, Critique, Review, Contest, CosplayGallery, Collection, Article.

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
            return [
                Topic(
                    id=t["id"],
                    body=t["body"],
                    linked_id=t["linked_id"],
                    linked_type=t["linked_type"],
                    created_at=t["created_at"],
                    last_comment_viewed=t["last_comment_viewed"],
                    html_body=t["html_body"],
                    topic_title=t["topic_title"],
                    html_footer=t["html_footer"],
                    comments_count=t["comments_count"],
                    viewed=t["viewed"],
                    episode=t["episode"],
                    event=t["event"],
                    type=t["type"],
                    forum=Forum(**t["forum"]),
                    user=User(
                        id=t["user"]["id"],
                        nickname=t["user"]["nickname"],
                        avatar=t["user"]["avatar"],
                        last_online_at=t["user"]["last_online_at"],
                        url=t["user"]["url"],
                        image=PhotoExtended(**t["user"]["image"]),
                    ),
                    linked=(
                        Linked(
                            name=t["linked"]["name"],
                            id=t["linked"]["id"],
                            russian=t["linked"]["russian"],
                            url=t["linked"]["url"],
                            kind=t["linked"]["kind"],
                            score=t["linked"]["score"],
                            status=t["linked"]["status"],
                            episodes=t["linked"]["episodes"],
                            episodes_aired=t["linked"]["episodes_aired"],
                            aired_on=t["linked"]["aired_on"],
                            released_on=t["linked"]["released_on"],
                            image=Photo(**t["linked"]["image"]),
                        )
                        if t["linked"]
                        else None
                    ),
                )
                for t in response
            ]

        logger.debug(
            f"Bad Request(list): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def updates(
        self, page: int = None, limit: int = None
    ) -> List[Status] | RequestError:
        """

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
            return [
                Status(
                    id=t["id"],
                    event=t["event"],
                    episode=t["episode"],
                    created_at=t["created_at"],
                    url=t["id"],
                    linked=(
                        Linked(
                            name=t["linked"]["name"],
                            id=t["linked"]["id"],
                            russian=t["linked"]["russian"],
                            url=t["linked"]["url"],
                            kind=t["linked"]["kind"],
                            score=t["linked"]["score"],
                            status=t["linked"]["status"],
                            episodes=t["linked"]["episodes"],
                            episodes_aired=t["linked"]["episodes_aired"],
                            aired_on=t["linked"]["aired_on"],
                            released_on=t["linked"]["released_on"],
                            image=Photo(**t["linked"]["image"]),
                        )
                        if t["linked"]
                        else None
                    ),
                )
                for t in response
            ]

        logger.debug(
            f"Bad Request(updates): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def hot(self, limit: int = None) -> List[Topic] | RequestError:
        """
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
            return [
                Topic(
                    id=t["id"],
                    body=t["body"],
                    linked_id=t["linked_id"],
                    linked_type=t["linked_type"],
                    created_at=t["created_at"],
                    last_comment_viewed=t["last_comment_viewed"],
                    html_body=t["html_body"],
                    topic_title=t["topic_title"],
                    html_footer=t["html_footer"],
                    comments_count=t["comments_count"],
                    viewed=t["viewed"],
                    episode=t["episode"],
                    event=t["event"],
                    type=t["type"],
                    forum=Forum(**t["forum"]),
                    user=User(
                        id=t["user"]["id"],
                        nickname=t["user"]["nickname"],
                        avatar=t["user"]["avatar"],
                        last_online_at=t["user"]["last_online_at"],
                        url=t["user"]["url"],
                        image=PhotoExtended(**t["user"]["image"]),
                    ),
                    linked=(
                        Linked(
                            name=t["linked"]["name"],
                            id=t["linked"]["id"],
                            russian=t["linked"]["russian"],
                            url=t["linked"]["url"],
                            kind=t["linked"]["kind"],
                            score=t["linked"]["score"],
                            status=t["linked"]["status"],
                            episodes=t["linked"]["episodes"],
                            episodes_aired=t["linked"]["episodes_aired"],
                            aired_on=t["linked"]["aired_on"],
                            released_on=t["linked"]["released_on"],
                            image=Photo(**t["linked"]["image"])
                        )
                        if t["linked"]
                        else None
                    )
                )
                for t in response
            ]

        logger.debug(
            f"Bad Request(hot): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def byId(self, id: int) -> Topic | RequestError:
        response = await self._request.make_request(
            "GET",
            url=f"{self._base_url}/api/topics/{id}",
            headers=self.headers,
        )

        if not isinstance(response, RequestError):
            return Topic(
                id=response["id"],
                body=response["body"],
                linked_id=response["linked_id"],
                linked_type=response["linked_type"],
                created_at=response["created_at"],
                last_comment_viewed=response["last_comment_viewed"],
                html_body=response["html_body"],
                topic_title=response["topic_title"],
                html_footer=response["html_footer"],
                comments_count=response["comments_count"],
                viewed=response["viewed"],
                episode=response["episode"],
                event=response["event"],
                type=response["type"],
                forum=Forum(**response["forum"]),
                user=User(
                    id=response["user"]["id"],
                    nickname=response["user"]["nickname"],
                    avatar=response["user"]["avatar"],
                    last_online_at=response["user"]["last_online_at"],
                    url=response["user"]["url"],
                    image=PhotoExtended(**response["user"]["image"]),
                ),
                linked=(
                        ReviewLinked(
                            id=response["linked"]["id"],
                            animation=response["linked"]["animation"],
                            body=response["linked"]["body"],
                            created_at=response["linked"]["created_at"],
                            characters=response["linked"]["characters"],
                            overall=response["linked"]["overall"],
                            html_body=response["linked"]["html_body"],
                            music=response["linked"]["music"],
                            storyline=response["linked"]["storyline"],
                            votes_for=response["linked"]["votes_for"],
                            votes_count=response["linked"]["votes_count"],
                            target=Title(
                                id=response["linked"]["target"]["id"],
                                name=response["linked"]["target"]["name"],
                                russian=response["linked"]["target"]["russian"],
                                aired_on=response["linked"]["target"]["aired_on"],
                                image=Photo(
                                    **response["linked"]["target"]["image"]
                                ),
                                kind=response["linked"]["target"]["kind"],
                                released_on=response["linked"]["target"]["released_on"],
                                status=response["linked"]["target"]["status"],
                                score=response["linked"]["target"]["score"],
                                url=response["linked"]["target"]["url"],
                            ),
                            user=User(
                                id=response["linked"]["user"]["id"],
                                nickname=response["linked"]["user"]["nickname"],
                                avatar=response["linked"]["user"]["avatar"],
                                last_online_at=response["linked"]["user"]["last_online_at"],
                                url=response["linked"]["user"]["url"],
                                image=PhotoExtended(**response["linked"]["user"]["image"]),
                            ),
                        )
                        if response["linked"]
                        else None
                    )
            )

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
        Requires topics oauth scope
        :param body: str.
        :param forum_id: num.
        :param title: str.
        :param user_id:num .
        :param type: Must be one of: Topic.
        :param linked_id: num.
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
            return Topic(
                id=response["id"],
                body=response["body"],
                linked_id=response["linked_id"],
                linked_type=response["linked_type"],
                created_at=response["created_at"],
                last_comment_viewed=response["last_comment_viewed"],
                html_body=response["html_body"],
                topic_title=response["topic_title"],
                html_footer=response["html_footer"],
                comments_count=response["comments_count"],
                viewed=response["viewed"],
                episode=response["episode"],
                event=response["event"],
                type=response["type"],
                forum=Forum(**response["forum"]),
                user=User(
                    id=response["user"]["id"],
                    nickname=response["user"]["nickname"],
                    avatar=response["user"]["avatar"],
                    last_online_at=response["user"]["last_online_at"],
                    url=response["user"]["url"],
                    image=PhotoExtended(**response["user"]["image"]),
                ),
                linked=(
                        ReviewLinked(
                            id=response["linked"]["id"],
                            animation=response["linked"]["animation"],
                            body=response["linked"]["body"],
                            created_at=response["linked"]["created_at"],
                            characters=response["linked"]["characters"],
                            overall=response["linked"]["overall"],
                            html_body=response["linked"]["html_body"],
                            music=response["linked"]["music"],
                            storyline=response["linked"]["storyline"],
                            votes_for=response["linked"]["votes_for"],
                            votes_count=response["linked"]["votes_count"],
                            target=Title(
                                id=response["linked"]["target"]["id"],
                                name=response["linked"]["target"]["name"],
                                russian=response["linked"]["target"]["russian"],
                                aired_on=response["linked"]["target"]["aired_on"],
                                image=Photo(
                                    **response["linked"]["target"]["image"]
                                ),
                                kind=response["linked"]["target"]["kind"],
                                released_on=response["linked"]["target"]["released_on"],
                                status=response["linked"]["target"]["status"],
                                score=response["linked"]["target"]["score"],
                                url=response["linked"]["target"]["url"],
                            ),
                            user=User(
                                id=response["linked"]["user"]["id"],
                                nickname=response["linked"]["user"]["nickname"],
                                avatar=response["linked"]["user"]["avatar"],
                                last_online_at=response["linked"]["user"]["last_online_at"],
                                url=response["linked"]["user"]["url"],
                                image=PhotoExtended(**response["linked"]["user"]["image"]),
                            ),
                        )
                        if response["linked"]
                        else None
                    )
            )

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
        :param id: num.
        :param body: str.
        :param linked_id: num.
        :param linked_type: Must be one of: Anime, Manga, Ranobe, Character, Person, Club, ClubPage, Critique, Review, Contest, CosplayGallery, Collection, Article.
        :param title: str.
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

            return Topic(
                id=response["id"],
                body=response["body"],
                linked_id=response["linked_id"],
                linked_type=response["linked_type"],
                created_at=response["created_at"],
                last_comment_viewed=response["last_comment_viewed"],
                html_body=response["html_body"],
                topic_title=response["topic_title"],
                html_footer=response["html_footer"],
                comments_count=response["comments_count"],
                viewed=response["viewed"],
                episode=response["episode"],
                event=response["event"],
                type=response["type"],
                forum=Forum(**response["forum"]),
                user=User(
                    id=response["user"]["id"],
                    nickname=response["user"]["nickname"],
                    avatar=response["user"]["avatar"],
                    last_online_at=response["user"]["last_online_at"],
                    url=response["user"]["url"],
                    image=PhotoExtended(**response["user"]["image"]),
                ),
                linked=(
                        ReviewLinked(
                            id=response["linked"]["id"],
                            animation=response["linked"]["animation"],
                            body=response["linked"]["body"],
                            created_at=response["linked"]["created_at"],
                            characters=response["linked"]["characters"],
                            overall=response["linked"]["overall"],
                            html_body=response["linked"]["html_body"],
                            music=response["linked"]["music"],
                            storyline=response["linked"]["storyline"],
                            votes_for=response["linked"]["votes_for"],
                            votes_count=response["linked"]["votes_count"],
                            target=Title(
                                id=response["linked"]["target"]["id"],
                                name=response["linked"]["target"]["name"],
                                russian=response["linked"]["target"]["russian"],
                                aired_on=response["linked"]["target"]["aired_on"],
                                image=Photo(
                                    **response["linked"]["target"]["image"]
                                ),
                                kind=response["linked"]["target"]["kind"],
                                released_on=response["linked"]["target"]["released_on"],
                                status=response["linked"]["target"]["status"],
                                score=response["linked"]["target"]["score"],
                                url=response["linked"]["target"]["url"],
                            ),
                            user=User(
                                id=response["linked"]["user"]["id"],
                                nickname=response["linked"]["user"]["nickname"],
                                avatar=response["linked"]["user"]["avatar"],
                                last_online_at=response["linked"]["user"]["last_online_at"],
                                url=response["linked"]["user"]["url"],
                                image=PhotoExtended(**response["linked"]["user"]["image"]),
                            ),
                        )
                        if response["linked"]
                        else None
                    )
            )

        logger.debug(
            f"Bad Request(update): status - {response.status_code}: info - {str(response)}"
        )
        return response

    async def delete(self, id: int) -> None | RequestError:
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
