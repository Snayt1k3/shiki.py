import pytest

from shikimori.endpoints.club import ClubEndpoint
from shikimori.types.animes import Anime
from shikimori.types.club import Logo, Club, ClubImage, ClubInfo, Collection
from shikimori.types.manga import Manga
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.ranobe import Ranobe
from shikimori.types.character import CharacterBrief
from shikimori.types.topics import Forum
from shikimori.types.user import User


@pytest.fixture
def club_client():
    return ClubEndpoint("", "", "")


@pytest.fixture
def club_list_json():
    return [
        {
            "id": 2,
            "name": "club_4",
            "logo": {
                "original": "/assets/globals/missing_original_original.png",
                "main": "/assets/globals/missing_main_main.png",
                "x96": "/assets/globals/missing_x96_x96.png",
                "x73": "/assets/globals/missing_x73_x73.png",
                "x48": "/assets/globals/missing_x48_x48.png",
            },
            "is_censored": False,
            "join_policy": "free",
            "comment_policy": "free",
        },
        {
            "id": 3,
            "name": "club_5",
            "logo": {
                "original": "/assets/globals/missing_original_original.png",
                "main": "/assets/globals/missing_main_main.png",
                "x96": "/assets/globals/missing_x96_x96.png",
                "x73": "/assets/globals/missing_x73_x73.png",
                "x48": "/assets/globals/missing_x48_x48.png",
            },
            "is_censored": False,
            "join_policy": "free",
            "comment_policy": "free",
        },
    ]


@pytest.fixture
def club_list_resp(club_list_json):
    return [
        Club(
            logo=Logo(**c["logo"]),
            comment_policy=c["comment_policy"],
            id=c["id"],
            name=c["name"],
            is_censored=c["is_censored"],
            join_policy=c["join_policy"],
        )
        for c in club_list_json
    ]


@pytest.fixture
def club_byId_json():
    return {
        "id": 1097,
        "name": "club_7",
        "logo": {
            "original": "/assets/globals/missing_original_original.png",
            "main": "/assets/globals/missing_main_main.png",
            "x96": "/assets/globals/missing_x96_x96.png",
            "x73": "/assets/globals/missing_x73_x73.png",
            "x48": "/assets/globals/missing_x48_x48.png",
        },
        "is_censored": None,
        "join_policy": "free",
        "comment_policy": "free",
        "description": "",
        "description_html": "<p class='b-nothing_here'>Нет описания</p>",
        "mangas": [
            {
                "id": 14,
                "name": "manga_3",
                "russian": "манга_3",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/mangas/14-manga-3",
                "kind": "manga",
                "score": "1.0",
                "status": "released",
                "volumes": 0,
                "chapters": 0,
                "aired_on": None,
                "released_on": None,
            }
        ],
        "characters": [
            {
                "id": 3,
                "name": "character_3",
                "russian": "персонаж_3",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/characters/3-character-3",
            }
        ],
        "thread_id": 270110,
        "topic_id": 270110,
        "user_role": "member",
        "style_id": None,
        "members": [
            {
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
            }
        ],
        "animes": [
            {
                "id": 18,
                "name": "anime_18",
                "russian": "аниме_18",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/18-anime-18",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            }
        ],
        "images": [
            {
                "id": 2,
                "original_url": "/system/images/original/2.jpg?1669472369",
                "main_url": "/system/images/original/2.jpg?1669472369",
                "preview_url": "/system/images/preview/2.jpg?1669472369",
                "can_destroy": False,
                "user_id": 1002,
            }
        ],
    }


@pytest.fixture
def club_byId_resp(club_byId_json):
    response = club_byId_json
    return ClubInfo(
        id=response["id"],
        name=response["name"],
        is_censored=response["is_censored"],
        logo=Logo(**response["logo"]),
        join_policy=response["join_policy"],
        comment_policy=response["comment_policy"],
        description=response["description"],
        description_html=response["description_html"],
        style_id=response["style_id"],
        topic_id=response["topic_id"],
        thread_id=response["thread_id"],
        user_role=response["user_role"],
        animes=[
            Anime(
                id=anime["id"],
                name=anime["name"],
                russian=anime["russian"],
                image=Photo(**anime["image"]),
                url=anime["url"],
                kind=anime["kind"],
                score=anime["score"],
                status=anime["status"],
                episodes=anime["episodes"],
                episodes_aired=anime["episodes_aired"],
                aired_on=anime["aired_on"],
                released_on=anime["released_on"],
            )
            for anime in response["animes"]
        ],
        mangas=[
            Manga(
                id=manga["id"],
                name=manga["name"],
                russian=manga["russian"],
                image=Photo(**manga["image"]),
                url=manga["url"],
                kind=manga["kind"],
                score=manga["score"],
                status=manga["status"],
                volumes=manga["volumes"],
                chapters=manga["chapters"],
                aired_on=manga["aired_on"],
                released_on=manga["released_on"],
            )
            for manga in response["mangas"]
        ],
        characters=[
            CharacterBrief(
                id=ch["id"],
                name=ch["name"],
                russian=ch["russian"],
                url=ch["url"],
                image=Photo(**ch["image"]),
            )
            for ch in response["characters"]
        ],
        members=[
            User(
                id=u["id"],
                nickname=u["nickname"],
                avatar=u["avatar"],
                last_online_at=u["last_online_at"],
                url=u["url"],
                image=PhotoExtended(**u["image"]),
            )
            for u in response["members"]
        ],
        images=[ClubImage(**image) for image in response["images"]],
    )


@pytest.fixture
def club_animes_json():
    return [
        {
            "id": 17,
            "name": "anime_17",
            "russian": "аниме_17",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/animes/17-anime-17",
            "kind": "tv",
            "score": "1.0",
            "status": "released",
            "episodes": 0,
            "episodes_aired": 0,
            "aired_on": None,
            "released_on": None,
        }
    ]


@pytest.fixture
def club_animes_resp(club_animes_json):
    return [
        Anime(
            id=anime["id"],
            name=anime["name"],
            russian=anime["russian"],
            image=Photo(**anime["image"]),
            url=anime["url"],
            kind=anime["kind"],
            score=anime["score"],
            status=anime["status"],
            episodes=anime["episodes"],
            episodes_aired=anime["episodes_aired"],
            aired_on=anime["aired_on"],
            released_on=anime["released_on"],
        )
        for anime in club_animes_json
    ]


@pytest.fixture
def club_mangas_json():
    return [
        {
            "id": 13,
            "name": "manga_2",
            "russian": "манга_2",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/mangas/13-manga-2",
            "kind": "manga",
            "score": "1.0",
            "status": "released",
            "volumes": 0,
            "chapters": 0,
            "aired_on": None,
            "released_on": None,
        }
    ]


@pytest.fixture
def club_mangas_resp(club_mangas_json):
    return [
        Manga(
            id=manga["id"],
            name=manga["name"],
            russian=manga["russian"],
            image=Photo(**manga["image"]),
            url=manga["url"],
            kind=manga["kind"],
            score=manga["score"],
            status=manga["status"],
            volumes=manga["volumes"],
            chapters=manga["chapters"],
            aired_on=manga["aired_on"],
            released_on=manga["released_on"],
        )
        for manga in club_mangas_json
    ]


@pytest.fixture
def club_ranobes_resp(club_mangas_json):
    return [
        Ranobe(
            id=manga["id"],
            name=manga["name"],
            russian=manga["russian"],
            image=Photo(**manga["image"]),
            url=manga["url"],
            kind=manga["kind"],
            score=manga["score"],
            status=manga["status"],
            volumes=manga["volumes"],
            chapters=manga["chapters"],
            aired_on=manga["aired_on"],
            released_on=manga["released_on"],
        )
        for manga in club_mangas_json
    ]


@pytest.fixture
def club_characters_json():
    return [
        {
            "id": 2,
            "name": "character_2",
            "russian": "персонаж_2",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/characters/2-character-2",
        }
    ]


@pytest.fixture
def club_characters_resp(club_characters_json):
    return [
        CharacterBrief(
            id=s["id"],
            name=s["name"],
            russian=s["russian"],
            url=s["url"],
            image=Photo(**s["image"]),
        )
        for s in club_characters_json
    ]


@pytest.fixture
def club_collection_json():
    return [
        {
            "id": 270106,
            "topic_title": "Collection 1",
            "body": "Топик обсуждения [collection=1]коллекции[/collection].",
            "html_body": '<div class="collection-groups" data-texts="[]"></div>',
            "html_footer": "",
            "created_at": "2022-11-26T17:19:29.053+03:00",
            "comments_count": 0,
            "forum": {
                "id": 14,
                "position": 0,
                "name": "Коллекции",
                "permalink": "collections",
                "url": "/forum/collections",
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
            "type": "Topics::EntryTopics::CollectionTopic",
            "linked_id": 1,
            "linked_type": "Collection",
            "linked": None,
            "viewed": True,
            "last_comment_viewed": None,
            "event": None,
            "episode": None,
        }
    ]


@pytest.fixture
def club_collection_resp(club_collection_json):
    return [
        Collection(
            body=s["body"],
            comments_count=s["comments_count"],
            id=s["id"],
            linked=s["linked"],
            linked_id=s["linked_id"],
            created_at=s["created_at"],
            episode=s["episode"],
            event=s["event"],
            html_body=s["html_body"],
            html_footer=s["html_footer"],
            last_comment_viewed=s["last_comment_viewed"],
            linked_type=s["linked_type"],
            topic_title=s["topic_title"],
            type=s["type"],
            viewed=s["viewed"],
            forum=Forum(**s.get("forum")),
            user=User(
                id=s["user"]["id"],
                avatar=s["user"]["avatar"],
                url=s["user"]["url"],
                last_online_at=s["user"]["last_online_at"],
                nickname=s["user"]["nickname"],
                image=PhotoExtended(**s["user"]["image"]),
            ),
        )
        for s in club_collection_json
    ]


@pytest.fixture
def club_clubs_json():
    return [
        {
            "id": 1096,
            "name": "club_3",
            "logo": {
                "original": "/assets/globals/missing_original_original.png",
                "main": "/assets/globals/missing_main_main.png",
                "x96": "/assets/globals/missing_x96_x96.png",
                "x73": "/assets/globals/missing_x73_x73.png",
                "x48": "/assets/globals/missing_x48_x48.png",
            },
            "is_censored": False,
            "join_policy": "free",
            "comment_policy": "free",
        }
    ]


@pytest.fixture
def club_clubs_resp(club_clubs_json):
    return [
        Club(
            logo=Logo(**c["logo"]),
            comment_policy=c["comment_policy"],
            id=c["id"],
            name=c["name"],
            is_censored=c["is_censored"],
            join_policy=c["join_policy"],
        )
        for c in club_clubs_json
    ]


@pytest.fixture
def club_members_json():
    return [
        {
            "id": 23456792,
            "nickname": "user_1",
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
            "last_online_at": "2022-11-26T17:19:28.853+03:00",
            "url": "http://test.host/user_1",
        }
    ]


@pytest.fixture
def club_members_resp(club_members_json):
    return [
        User(
            id=u["id"],
            nickname=u["nickname"],
            avatar=u["avatar"],
            last_online_at=u["last_online_at"],
            url=u["url"],
            image=PhotoExtended(**u["image"]),
        )
        for u in club_members_json
    ]


@pytest.fixture
def club_images_json():
    return [
        {
            "id": 1,
            "original_url": "/system/images/original/1.jpg?1669472369",
            "main_url": "/system/images/original/1.jpg?1669472369",
            "preview_url": "/system/images/preview/1.jpg?1669472369",
            "can_destroy": None,
            "user_id": 1001,
        }
    ]


@pytest.fixture
def club_images_resp(club_images_json):
    return [ClubImage(**s) for s in club_images_json]
