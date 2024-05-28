import pytest

from shikimori.endpoints.users import UserEndpoint
from shikimori.types.animes import Anime
from shikimori.types.bans import Ban
from shikimori.types.comment import CommentBrief
from shikimori.types.club import Club, Logo
from shikimori.types.manga import Manga
from shikimori.types.message import MessageInfo
from shikimori.types.photo import PhotoExtended, Photo
from shikimori.types.topics import Linked
from shikimori.types.user import (
    User,
    UserInfo,
    Stats,
    Statuses,
    UserTitle,
    Obj,
    ValueObj,
    UserInfoInc,
    Rate,
    Favourites,
    FavouritesObj,
    UnreadMessages,
    HistoryObj,
    TitleHistory,
)


@pytest.fixture
def user_client():
    return UserEndpoint("", "", "")


@pytest.fixture
def users_list_json():
    return [
        {
            "id": 23456806,
            "nickname": "Test1",
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
            "last_online_at": "2022-11-26T17:19:31.010+03:00",
            "url": "http://test.host/Test1",
        },
        {
            "id": 23456807,
            "nickname": "Test2",
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
            "last_online_at": "2022-11-26T17:19:31.010+03:00",
            "url": "http://test.host/Test2",
        },
    ]


@pytest.fixture
def users_list_resp(users_list_json):
    return [
        User(
            id=u["id"],
            nickname=u["nickname"],
            avatar=u["avatar"],
            last_online_at=u["last_online_at"],
            url=u["url"],
            image=PhotoExtended(**u["image"]),
        )
        for u in users_list_json
    ]


@pytest.fixture
def users_byid_json():
    return {
        "id": 23456816,
        "nickname": "Test",
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
        "last_online_at": "2022-11-26T17:19:31.451+03:00",
        "url": "http://test.host/Test",
        "name": None,
        "sex": None,
        "full_years": None,
        "last_online": "сейчас на сайте",
        "website": "",
        "location": None,
        "banned": False,
        "about": "",
        "about_html": "",
        "common_info": [
            "Нет личных данных",
            "на сайте с <span class='b-tooltipped dotted mobile unprocessed' data-direction='right' title='26 ноября 2022 г.'>26 ноября 2022 г.</span>",
        ],
        "show_comments": False,
        "in_friends": None,
        "is_ignored": False,
        "stats": {
            "statuses": {
                "anime": [
                    {
                        "id": 0,
                        "grouped_id": "planned",
                        "name": "planned",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 1,
                        "grouped_id": "watching,rewatching",
                        "name": "watching",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 2,
                        "grouped_id": "completed",
                        "name": "completed",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 3,
                        "grouped_id": "on_hold",
                        "name": "on_hold",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 4,
                        "grouped_id": "dropped",
                        "name": "dropped",
                        "size": 0,
                        "type": "Anime",
                    },
                ],
                "manga": [
                    {
                        "id": 0,
                        "grouped_id": "planned",
                        "name": "planned",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 1,
                        "grouped_id": "watching,rewatching",
                        "name": "watching",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 2,
                        "grouped_id": "completed",
                        "name": "completed",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 3,
                        "grouped_id": "on_hold",
                        "name": "on_hold",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 4,
                        "grouped_id": "dropped",
                        "name": "dropped",
                        "size": 0,
                        "type": "Manga",
                    },
                ],
            },
            "full_statuses": {
                "anime": [
                    {
                        "id": 0,
                        "grouped_id": "planned",
                        "name": "planned",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 1,
                        "grouped_id": "watching",
                        "name": "watching",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 9,
                        "grouped_id": "rewatching",
                        "name": "rewatching",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 2,
                        "grouped_id": "completed",
                        "name": "completed",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 3,
                        "grouped_id": "on_hold",
                        "name": "on_hold",
                        "size": 0,
                        "type": "Anime",
                    },
                    {
                        "id": 4,
                        "grouped_id": "dropped",
                        "name": "dropped",
                        "size": 0,
                        "type": "Anime",
                    },
                ],
                "manga": [
                    {
                        "id": 0,
                        "grouped_id": "planned",
                        "name": "planned",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 1,
                        "grouped_id": "watching",
                        "name": "watching",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 9,
                        "grouped_id": "rewatching",
                        "name": "rewatching",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 2,
                        "grouped_id": "completed",
                        "name": "completed",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 3,
                        "grouped_id": "on_hold",
                        "name": "on_hold",
                        "size": 0,
                        "type": "Manga",
                    },
                    {
                        "id": 4,
                        "grouped_id": "dropped",
                        "name": "dropped",
                        "size": 0,
                        "type": "Manga",
                    },
                ],
            },
            "scores": {"anime": [], "manga": []},
            "types": {"anime": [], "manga": []},
            "ratings": {"anime": []},
            "has_anime?": False,
            "has_manga?": False,
            "genres": [],
            "studios": [],
            "publishers": [],
            "activity": {},
        },
        "style_id": None,
    }


@pytest.fixture
def users_byid_resp(users_byid_json):
    response = users_byid_json
    return UserInfo(
        id=response["id"],
        avatar=response["avatar"],
        about_html=response["about_html"],
        about=response["about"],
        last_online_at=response["last_online_at"],
        nickname=response["nickname"],
        name=response["name"],
        location=response["location"],
        full_years=response["full_years"],
        is_ignored=response["is_ignored"],
        in_friends=response["in_friends"],
        style_id=response["style_id"],
        common_info=response["common_info"],
        last_online=response["last_online"],
        banned=response["banned"],
        website=response["website"],
        show_comments=response["show_comments"],
        sex=response["sex"],
        url=response["url"],
        image=PhotoExtended(**response["image"]),
        stats=Stats(
            genres=response["stats"]["genres"],
            studios=response["stats"]["studios"],
            publishers=response["stats"]["publishers"],
            statuses=Statuses(
                animes=[
                    UserTitle(**a)
                    for a in response["stats"]["statuses"].get("anime", [])
                ],
                manga=[
                    UserTitle(**a)
                    for a in response["stats"]["statuses"].get("manga", [])
                ],
            ),
            full_statuses=Statuses(
                animes=[
                    UserTitle(**a)
                    for a in response["stats"]["full_statuses"].get("anime", [])
                ],
                manga=[
                    UserTitle(**a)
                    for a in response["stats"]["full_statuses"].get("manga", [])
                ],
            ),
            scores=Obj(
                anime=[
                    ValueObj(**a) for a in response["stats"]["scores"].get("anime", [])
                ],
                manga=[
                    ValueObj(**a) for a in response["stats"]["scores"].get("manga", [])
                ],
            ),
            types=Obj(
                anime=[
                    ValueObj(**a) for a in response["stats"]["types"].get("anime", [])
                ],
                manga=[
                    ValueObj(**a) for a in response["stats"]["types"].get("manga", [])
                ],
            ),
            ratings=Obj(
                anime=[
                    ValueObj(**a) for a in response["stats"]["ratings"].get("anime", [])
                ],
                manga=[
                    ValueObj(**a) for a in response["stats"]["ratings"].get("manga", [])
                ],
            ),
            activity=[ValueObj(**a) for a in response["stats"]["activity"]],
            has_anime=response["stats"]["has_anime?"],
            has_manga=response["stats"]["has_manga?"],
        ),
    )


@pytest.fixture
def users_info_json():
    return {
        "id": 23456815,
        "nickname": "Test",
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
        "last_online_at": "2022-11-26T17:19:31.424+03:00",
        "url": "http://test.host/Test",
        "name": None,
        "sex": None,
        "website": None,
        "birth_on": None,
        "full_years": None,
        "locale": "ru",
    }


@pytest.fixture
def users_info_resp(users_info_json):
    response = users_info_json
    return UserInfoInc(
        sex=response["sex"],
        full_years=response["full_years"],
        avatar=response["avatar"],
        id=response["id"],
        birth_on=response["birth_on"],
        last_online_at=response["last_online_at"],
        locale=response["locale"],
        url=response["url"],
        name=response["name"],
        nickname=response["nickname"],
        image=PhotoExtended(**response["image"]),
    )


@pytest.fixture
def users_whoami_json():
    return {
        "id": 23456815,
        "nickname": "Test",
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
        "last_online_at": "2022-11-26T17:19:31.424+03:00",
        "url": "http://test.host/Test",
        "name": None,
        "sex": None,
        "website": None,
        "birth_on": None,
        "full_years": None,
        "locale": "ru",
    }


@pytest.fixture
def users_whoami_resp(users_whoami_json):
    response = users_whoami_json
    return UserInfoInc(
        sex=response["sex"],
        full_years=response["full_years"],
        avatar=response["avatar"],
        id=response["id"],
        birth_on=response["birth_on"],
        last_online_at=response["last_online_at"],
        locale=response["locale"],
        url=response["url"],
        name=response["name"],
        nickname=response["nickname"],
        image=PhotoExtended(**response["image"]),
    )


@pytest.fixture
def users_signout_json():
    return {
        "id": 23456815,
        "nickname": "Test",
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
        "last_online_at": "2022-11-26T17:19:31.424+03:00",
        "url": "http://test.host/Test",
        "name": None,
        "sex": None,
        "website": None,
        "birth_on": None,
        "full_years": None,
        "locale": "ru",
    }


@pytest.fixture
def users_signout_resp(users_signout_json):
    response = users_signout_json
    return UserInfoInc(
        sex=response["sex"],
        full_years=response["full_years"],
        avatar=response["avatar"],
        id=response["id"],
        birth_on=response["birth_on"],
        last_online_at=response["last_online_at"],
        locale=response["locale"],
        url=response["url"],
        name=response["name"],
        nickname=response["name"],
        image=PhotoExtended(**response["image"]),
    )


@pytest.fixture
def users_friends_json():
    return [
        {
            "id": 23456802,
            "nickname": "user_7",
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
            "last_online_at": "2022-11-26T17:19:30.832+03:00",
            "url": "http://test.host/user_7",
        }
    ]


@pytest.fixture
def users_friends_resp(users_friends_json):
    return [
        User(
            id=u["id"],
            nickname=u["nickname"],
            avatar=u["avatar"],
            last_online_at=u["last_online_at"],
            url=u["url"],
            image=PhotoExtended(**u["image"]),
        )
        for u in users_friends_json
    ]


@pytest.fixture
def users_clubs_json():
    return [
        {
            "id": 1098,
            "name": "club_8",
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
def users_clubs_resp(users_clubs_json):
    return [
        Club(
            logo=Logo(**club["logo"]),
            comment_policy=club["comment_policy"],
            id=club["id"],
            name=club["name"],
            is_censored=club["is_censored"],
            join_policy=club["join_policy"],
        )
        for club in users_clubs_json
    ]


@pytest.fixture
def users_animerates_json():
    return [
        {
            "id": 20,
            "score": 0,
            "status": "completed",
            "text": None,
            "episodes": 0,
            "chapters": None,
            "volumes": None,
            "text_html": "",
            "rewatches": 0,
            "created_at": "2022-11-26T17:19:31.067+03:00",
            "updated_at": "2022-11-26T17:19:31.067+03:00",
            "user": {
                "id": 23456809,
                "nickname": "user_9",
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
                "last_online_at": "2022-11-26T17:19:31.067+03:00",
                "url": "http://test.host/user_9",
            },
            "anime": {
                "id": 32,
                "name": "anime_32",
                "russian": "аниме_32",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/32-anime-32",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "manga": None,
        }
    ]


@pytest.fixture
def users_animerates_resp(users_animerates_json):
    return [
        Rate(
            id=a["id"],
            chapters=a["chapters"],
            episodes=a["episodes"],
            manga=None,
            rewatches=a["rewatches"],
            status=a["status"],
            score=a["score"],
            text=a["text"],
            text_html=a["text_html"],
            volumes=a["volumes"],
            user=User(
                id=a["user"]["id"],
                nickname=a["user"]["nickname"],
                avatar=a["user"]["avatar"],
                last_online_at=a["user"]["last_online_at"],
                url=a["user"]["url"],
                image=PhotoExtended(**a["user"]["image"]),
            ),
            anime=Anime(
                id=a["anime"]["id"],
                name=a["anime"]["name"],
                russian=a["anime"]["russian"],
                image=Photo(**a["anime"]["image"]),
                url=a["anime"]["url"],
                kind=a["anime"]["kind"],
                score=a["anime"]["score"],
                status=a["anime"]["status"],
                episodes=a["anime"]["episodes"],
                episodes_aired=a["anime"]["episodes_aired"],
                aired_on=a["anime"]["aired_on"],
                released_on=a["anime"]["released_on"],
            ),
        )
        for a in users_animerates_json
    ]


@pytest.fixture
def users_mangarates_json():
    return [
        {
            "id": 21,
            "score": 0,
            "status": "watching",
            "text": None,
            "episodes": None,
            "chapters": 0,
            "volumes": 0,
            "text_html": "",
            "rewatches": 0,
            "created_at": "2022-11-26T17:19:31.153+03:00",
            "updated_at": "2022-11-26T17:19:31.153+03:00",
            "user": {
                "id": 23456811,
                "nickname": "Test",
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
                "last_online_at": "2022-11-26T17:19:31.153+03:00",
                "url": "http://test.host/Test",
            },
            "anime": None,
            "manga": {
                "id": 28,
                "name": "manga_14",
                "russian": "манга_17",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/mangas/28-manga-14",
                "kind": "manga",
                "score": "1.0",
                "status": "released",
                "volumes": 0,
                "chapters": 0,
                "aired_on": None,
                "released_on": None,
            },
        }
    ]


@pytest.fixture
def users_mangarates_resp(users_mangarates_json):
    return [
        Rate(
            id=a["id"],
            chapters=a["chapters"],
            episodes=a["episodes"],
            rewatches=a["rewatches"],
            status=a["status"],
            score=a["score"],
            text=a["text"],
            anime=None,
            text_html=a["text_html"],
            volumes=a["volumes"],
            user=User(
                id=a["user"]["id"],
                nickname=a["user"]["nickname"],
                avatar=a["user"]["avatar"],
                last_online_at=a["user"]["last_online_at"],
                url=a["user"]["url"],
                image=PhotoExtended(**a["user"]["image"]),
            ),
            manga=Manga(
                id=a["manga"]["id"],
                name=a["manga"]["name"],
                russian=a["manga"]["russian"],
                image=Photo(**a["manga"]["image"]),
                url=a["manga"]["url"],
                kind=a["manga"]["kind"],
                score=a["manga"]["score"],
                status=a["manga"]["status"],
                volumes=a["manga"]["volumes"],
                chapters=a["manga"]["chapters"],
                aired_on=a["manga"]["aired_on"],
                released_on=a["manga"]["released_on"],
            ),
        )
        for a in users_mangarates_json
    ]


@pytest.fixture
def users_favourites_json():
    return {
        "animes": [
            {
                "id": 1604,
                "name": "Katekyou Hitman Reborn!",
                "russian": "Репетитор-киллер Реборн!",
                "image": "/system/animes/x64/1604.jpg?1701418959",
                "url": None,
            },
            {
                "id": 2581,
                "name": "Kidou Senshi Gundam 00",
                "russian": "Мобильный воин Гандам 00",
                "image": "/system/animes/x64/2581.jpg?1701420126",
                "url": None,
            },
            {
                "id": 3927,
                "name": "Kidou Senshi Gundam 00 Second Season",
                "russian": "Мобильный воин Гандам 00 2",
                "image": "/system/animes/x64/3927.jpg?1701420124",
                "url": None,
            },
        ],
        "mangas": [],
        "ranobe": [],
        "characters": [],
        "people": [],
        "mangakas": [],
        "seyu": [
            {
                "id": 65,
                "name": "Mamoru Miyano",
                "russian": "Мамору Мияно",
                "image": "/system/people/x64/65.jpg?1706560238",
                "url": None,
            }
        ],
        "producers": [],
    }


@pytest.fixture
def users_favourites_resp(users_favourites_json):
    return Favourites(
        animes=[FavouritesObj(**a) for a in users_favourites_json["animes"]],
        characters=[FavouritesObj(**a) for a in users_favourites_json["characters"]],
        producers=[FavouritesObj(**a) for a in users_favourites_json["producers"]],
        mangakas=[FavouritesObj(**a) for a in users_favourites_json["mangakas"]],
        mangas=[FavouritesObj(**a) for a in users_favourites_json["mangas"]],
        seyu=[FavouritesObj(**a) for a in users_favourites_json["seyu"]],
        ranobe=[FavouritesObj(**a) for a in users_favourites_json["ranobe"]],
    )


@pytest.fixture
def users_messages_json():
    return [
        {
            "id": 4,
            "kind": "anons",
            "read": False,
            "body": "anime [b]anons[/b]",
            "html_body": "Анонсировано аниме anime_34",
            "created_at": "2022-11-26T17:19:31.349+03:00",
            "linked_id": 270114,
            "linked_type": "Topic",
            "linked": {
                "id": 34,
                "topic_url": "http://test.host/forum/news/270114-topic-5",
                "thread_id": 270114,
                "topic_id": 270114,
                "type": "Anime",
                "name": "anime_34",
                "russian": "аниме_34",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/34-anime-34",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
            "from": {
                "id": 23456814,
                "nickname": "user_10",
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
                "last_online_at": "2022-11-26T17:19:31.349+03:00",
                "url": "http://test.host/user_10",
            },
            "to": {
                "id": 23456813,
                "nickname": "Test",
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
                "last_online_at": "2022-11-26T17:19:31.349+03:00",
                "url": "http://test.host/Test",
            },
        }
    ]


@pytest.fixture
def users_messages_resp(users_messages_json):
    return [
        MessageInfo(
            id=s["id"],
            kind=s["kind"],
            body=s["body"],
            html_body=s["html_body"],
            created_at=s["created_at"],
            linked_id=s["linked_id"],
            linked_type=s["linked_type"],
            read=s["read"],
            linked=(
                Linked(
                    name=s["linked"]["name"],
                    id=s["linked"]["id"],
                    russian=s["linked"]["russian"],
                    url=s["linked"]["url"],
                    kind=s["linked"]["kind"],
                    score=s["linked"]["score"],
                    status=s["linked"]["status"],
                    episodes=s["linked"]["episodes"],
                    episodes_aired=s["linked"]["episodes_aired"],
                    aired_on=s["linked"]["aired_on"],
                    released_on=s["linked"]["released_on"],
                    image=Photo(**s["linked"]["image"]),
                )
                if s["linked"]
                else None
            ),
            to=User(
                id=s["to"]["id"],
                avatar=s["to"]["avatar"],
                image=PhotoExtended(**s["to"]["image"]),
                last_online_at=s["to"]["last_online_at"],
                nickname=s["to"]["nickname"],
                url=s["to"]["url"],
            ),
            sender=User(
                id=s["from"]["id"],
                avatar=s["from"]["avatar"],
                image=PhotoExtended(**s["from"]["image"]),
                last_online_at=s["from"]["last_online_at"],
                nickname=s["from"]["nickname"],
                url=s["from"]["url"],
            ),
        )
        for s in users_messages_json
    ]


@pytest.fixture
def users_unread_json():
    return {"messages": 0, "news": 0, "notifications": 0}


@pytest.fixture
def users_unread_resp(users_unread_json):
    return UnreadMessages(**users_unread_json)


@pytest.fixture
def users_history_json():
    return [
        {
            "id": 42,
            "created_at": "2022-11-26T17:19:30.888+03:00",
            "description": "Запланировано",
            "target": {
                "id": 31,
                "name": "anime_31",
                "russian": "аниме_31",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/31-anime-31",
                "kind": "tv",
                "score": "1.0",
                "status": "released",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": None,
                "released_on": None,
            },
        },
        {
            "id": 41,
            "created_at": "2022-11-26T17:19:30.888+03:00",
            "description": "Импортировано аниме - 522 записи",
            "target": None,
        },
    ]


@pytest.fixture
def users_history_resp(users_history_json):
    return [
        HistoryObj(
            id=obj["id"],
            description=obj["description"],
            target=(
                TitleHistory(
                    id=obj["target"]["id"],
                    name=obj["target"]["name"],
                    russian=obj["target"]["russian"],
                    image=Photo(**obj["target"]["image"]),
                    url=obj["target"]["url"],
                    kind=obj["target"]["kind"],
                    score=obj["target"]["score"],
                    status=obj["target"]["status"],
                    episodes=obj["target"].get("episodes"),
                    volumes=obj["target"].get("volumes"),
                    chapters=obj["target"].get("chapters"),
                    episodes_aired=obj["target"].get("episodes_aired"),
                    aired_on=obj["target"]["aired_on"],
                    released_on=obj["target"]["released_on"],
                )
                if obj["target"]
                else None
            ),
        )
        for obj in users_history_json
    ]


@pytest.fixture
def users_bans_json():
    return [
        {
            "id": 3,
            "user_id": 23456804,
            "comment": {
                "id": 9,
                "commentable_id": 82468,
                "commentable_type": "Topic",
                "body": "comment_body_9\n\n[ban=3]",
                "user_id": 23456804,
                "created_at": "2022-11-26T17:19:30.929+03:00",
                "updated_at": "2022-11-26T17:19:30.929+03:00",
                "is_offtopic": False,
            },
            "moderator_id": 23456804,
            "reason": "moderator comment",
            "created_at": "2022-11-26T17:19:30.929+03:00",
            "duration_minutes": 180,
            "user": {
                "id": 23456804,
                "nickname": "Test",
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
                "last_online_at": "2022-11-26T17:19:30.929+03:00",
                "url": "http://test.host/Test",
            },
            "moderator": {
                "id": 23456804,
                "nickname": "Test",
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
                "last_online_at": "2022-11-26T17:19:30.929+03:00",
                "url": "http://test.host/Test",
            },
        }
    ]


@pytest.fixture
def users_bans_resp(users_bans_json):
    return [
        Ban(
            id=b["id"],
            created_at=b["created_at"],
            duration_minutes=b["duration_minutes"],
            moderator_id=b["moderator_id"],
            reason=b["reason"],
            user_id=b["user_id"],
            comment=CommentBrief(**b["comment"]),
            user=User(
                id=b["user"]["id"],
                avatar=b["user"]["avatar"],
                image=PhotoExtended(**b["user"]["image"]),
                last_online_at=b["user"]["last_online_at"],
                nickname=b["user"]["nickname"],
                url=b["user"]["url"],
            ),
            moderator=User(
                id=b["moderator"]["id"],
                avatar=b["moderator"]["avatar"],
                image=PhotoExtended(**b["moderator"]["image"]),
                last_online_at=b["moderator"]["last_online_at"],
                nickname=b["moderator"]["nickname"],
                url=b["moderator"]["url"],
            ),
        )
        for b in users_bans_json
    ]
