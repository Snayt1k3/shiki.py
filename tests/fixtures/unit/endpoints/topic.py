import pytest

from shikimori.endpoints.topics import TopicsEndpoint
from shikimori.types.photo import PhotoExtended, Photo
from shikimori.types.topics import Topic, Linked, Forum, Status, ReviewLinked, Title
from shikimori.types.user import User


@pytest.fixture
def topic_client():
    return TopicsEndpoint("", "", "")


@pytest.fixture
def topic_list_json():
    return [
        {
            "id": 270120,
            "topic_title": "topic_10",
            "body": "test [spoiler=спойлер]test[/spoiler] test",
            "html_body": 'test <span class="b-spoiler_inline to-process" data-dynamic="spoiler_inline" tabindex="0"><span>test</span></span> test',
            "html_footer": "",
            "created_at": "2022-11-26T17:19:31.939+03:00",
            "comments_count": 0,
            "forum": {
                "id": 1,
                "position": 0,
                "name": "Аниме и манга",
                "permalink": "animanga",
                "url": "/forum/animanga",
            },
            "user": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "type": "Topic",
            "linked_id": 37,
            "linked_type": "Anime",
            "linked": {
                "id": 37,
                "name": "anime_37",
                "russian": "аниме_37",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/37-anime-37",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "viewed": True,
            "last_comment_viewed": None,
            "event": None,
            "episode": None,
        }
    ]


@pytest.fixture
def topic_list_resp(topic_list_json):
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
        for t in topic_list_json
    ]


@pytest.fixture
def topic_updates_json():
    return [
        {
            "id": 270124,
            "linked": {
                "id": 40,
                "name": "anime_40",
                "russian": "аниме_40",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/40-anime-40",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "event": "episode",
            "episode": 5,
            "created_at": "2022-11-26T17:19:32.123+03:00",
            "url": "http://test.host/forum/animanga/anime-40-anime-40/270124-topic-14",
        }
    ]


@pytest.fixture
def topic_updates_resp(topic_updates_json):
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
        for t in topic_updates_json
    ]


@pytest.fixture
def topics_hot_json():
    return [
        {
            "id": 270121,
            "topic_title": "topic_11",
            "body": "topic_text_10",
            "html_body": "topic_text_10",
            "html_footer": "",
            "created_at": "2022-11-26T17:19:31.981+03:00",
            "comments_count": 0,
            "forum": {
                "id": 1,
                "position": 0,
                "name": "Аниме и манга",
                "permalink": "animanga",
                "url": "/forum/animanga",
            },
            "user": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "type": "Topic",
            "linked_id": 38,
            "linked_type": "Anime",
            "linked": {
                "id": 38,
                "name": "anime_38",
                "russian": "аниме_38",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/38-anime-38",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "viewed": True,
            "last_comment_viewed": None,
            "event": "episode",
            "episode": 5,
        }
    ]


@pytest.fixture
def topics_hot_resp(topics_hot_json):
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
        for t in topics_hot_json
    ]


@pytest.fixture
def topics_byid_json():
    return {
        "id": 270123,
        "topic_title": "Рецензия на аниме &laquo;аниме_39&raquo;",
        "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        "html_body": '<div class="critique-stars"><div class="star-line"><div class="title">Сюжет</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Персонажи</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Рисовка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Звуковой ряд</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Итоговая оценка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div></div><meta content="1" itemprop="critiqueRating" />ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        "html_footer": "",
        "created_at": "2022-11-26T17:19:32.048+03:00",
        "comments_count": 0,
        "forum": {
            "id": 12,
            "position": 0,
            "name": "Рецензии",
            "permalink": "critiques",
            "url": "/forum/critiques",
        },
        "user": {
            "id": 23456789,
            "nickname": "user_user",
            "avatar": "/assets/globals/missing_avatar/x48.png",
            "image": {
                "x160": "/assets/globals/missing_avatar/x160.png",
                "x148": "/assets/globals/missing_avatar/x148.png",
                "x80": "/assets/globals/missing_avatar/x80.png",
                "x64": "/assets/globals/missing_avatar/x64.png",
                "x48": "/assets/globals/missing_avatar/x48.png",
                "x32": "/assets/globals/missing_avatar/x32.png",
                "x16": "/assets/globals/missing_avatar/x16.png",
            },
            "last_online_at": "2022-11-26T17:19:26.755+03:00",
            "url": "http://test.host/user_user",
        },
        "type": "Topics::EntryTopics::CritiqueTopic",
        "linked_id": 1,
        "linked_type": "Critique",
        "linked": {
            "id": 1,
            "target": {
                "id": 39,
                "name": "anime_39",
                "russian": "аниме_39",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/39-anime-39",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "user": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "votes_count": 0,
            "votes_for": 0,
            "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "html_body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "overall": 1,
            "storyline": 1,
            "music": 1,
            "characters": 1,
            "animation": 1,
            "created_at": "2022-11-26T17:19:32.048+03:00",
        },
        "viewed": True,
        "last_comment_viewed": None,
        "event": None,
        "episode": None,
    }


@pytest.fixture
def topics_byid_resp(topics_byid_json):
    response = topics_byid_json
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
                    image=Photo(**response["linked"]["target"]["image"]),
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
        ),
    )


@pytest.fixture
def topics_create_json():
    return {
        "id": 270123,
        "topic_title": "Рецензия на аниме &laquo;аниме_39&raquo;",
        "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        "html_body": '<div class="critique-stars"><div class="star-line"><div class="title">Сюжет</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Персонажи</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Рисовка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Звуковой ряд</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Итоговая оценка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div></div><meta content="1" itemprop="critiqueRating" />ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        "html_footer": "",
        "created_at": "2022-11-26T17:19:32.048+03:00",
        "comments_count": 0,
        "forum": {
            "id": 12,
            "position": 0,
            "name": "Рецензии",
            "permalink": "critiques",
            "url": "/forum/critiques",
        },
        "user": {
            "id": 23456789,
            "nickname": "user_user",
            "avatar": "/assets/globals/missing_avatar/x48.png",
            "image": {
                "x160": "/assets/globals/missing_avatar/x160.png",
                "x148": "/assets/globals/missing_avatar/x148.png",
                "x80": "/assets/globals/missing_avatar/x80.png",
                "x64": "/assets/globals/missing_avatar/x64.png",
                "x48": "/assets/globals/missing_avatar/x48.png",
                "x32": "/assets/globals/missing_avatar/x32.png",
                "x16": "/assets/globals/missing_avatar/x16.png",
            },
            "last_online_at": "2022-11-26T17:19:26.755+03:00",
            "url": "http://test.host/user_user",
        },
        "type": "Topics::EntryTopics::CritiqueTopic",
        "linked_id": 1,
        "linked_type": "Critique",
        "linked": {
            "id": 1,
            "target": {
                "id": 39,
                "name": "anime_39",
                "russian": "аниме_39",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/39-anime-39",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "user": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "votes_count": 0,
            "votes_for": 0,
            "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "html_body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "overall": 1,
            "storyline": 1,
            "music": 1,
            "characters": 1,
            "animation": 1,
            "created_at": "2022-11-26T17:19:32.048+03:00",
        },
        "viewed": True,
        "last_comment_viewed": None,
        "event": None,
        "episode": None,
    }


@pytest.fixture
def topics_create_resp(topics_byid_json):
    response = topics_byid_json
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
                    image=Photo(**response["linked"]["target"]["image"]),
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
        ),
    )


@pytest.fixture
def topics_update_json():
    return {
        "id": 270123,
        "topic_title": "Рецензия на аниме &laquo;аниме_39&raquo;",
        "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        "html_body": '<div class="critique-stars"><div class="star-line"><div class="title">Сюжет</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Персонажи</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Рисовка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Звуковой ряд</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div><div class="star-line"><div class="title">Итоговая оценка</div><div class="b-rate"><div class="stars-container"><div class="hoverable-trigger"></div><div class="stars score score-1"></div><div class="stars hover"></div><div class="stars background"></div></div><div class="text-score"><div class="score-value score-1">1</div><div class="score-notice">Хуже некуда</div></div></div></div></div><meta content="1" itemprop="critiqueRating" />ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss',
        "html_footer": "",
        "created_at": "2022-11-26T17:19:32.048+03:00",
        "comments_count": 0,
        "forum": {
            "id": 12,
            "position": 0,
            "name": "Рецензии",
            "permalink": "critiques",
            "url": "/forum/critiques",
        },
        "user": {
            "id": 23456789,
            "nickname": "user_user",
            "avatar": "/assets/globals/missing_avatar/x48.png",
            "image": {
                "x160": "/assets/globals/missing_avatar/x160.png",
                "x148": "/assets/globals/missing_avatar/x148.png",
                "x80": "/assets/globals/missing_avatar/x80.png",
                "x64": "/assets/globals/missing_avatar/x64.png",
                "x48": "/assets/globals/missing_avatar/x48.png",
                "x32": "/assets/globals/missing_avatar/x32.png",
                "x16": "/assets/globals/missing_avatar/x16.png",
            },
            "last_online_at": "2022-11-26T17:19:26.755+03:00",
            "url": "http://test.host/user_user",
        },
        "type": "Topics::EntryTopics::CritiqueTopic",
        "linked_id": 1,
        "linked_type": "Critique",
        "linked": {
            "id": 1,
            "target": {
                "id": 39,
                "name": "anime_39",
                "russian": "аниме_39",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/39-anime-39",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "user": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "votes_count": 0,
            "votes_for": 0,
            "body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "html_body": "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
            "overall": 1,
            "storyline": 1,
            "music": 1,
            "characters": 1,
            "animation": 1,
            "created_at": "2022-11-26T17:19:32.048+03:00",
        },
        "viewed": True,
        "last_comment_viewed": None,
        "event": None,
        "episode": None,
    }


@pytest.fixture
def topics_update_resp(topics_byid_json):
    response = topics_byid_json
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
                    image=Photo(**response["linked"]["target"]["image"]),
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
        ),
    )
