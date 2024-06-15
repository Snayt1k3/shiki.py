import pytest

from shikimori.endpoints.animes import AnimeEndpoint
from shikimori.types.animes import Anime, AnimeInfo
from shikimori.types.photo import Photo
from shikimori.types.roles import Role
from shikimori.types.character import CharacterBrief
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.topics import Topic, Forum, Linked
from shikimori.types.user_rates import UserRateBrief
from shikimori.types.animes import (
    Anime,
    AnimeInfo,
    GenreExtended,
    Relation,
)
from shikimori.types.externalLink import ExternalLink
from shikimori.types.franchise import Franchise, Node, Link
from shikimori.types.manga import Manga
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.roles import Role
from shikimori.types.screenshots import ScreenShot
from shikimori.types.studios import Studio
from shikimori.types.videos import Video
from shikimori.types.user import User


@pytest.fixture
def anime_client():
    return AnimeEndpoint("", "", "")


@pytest.fixture
def animes_list_json():
    return [
        {
            "id": 56,
            "name": "Test",
            "russian": "аниме_56",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/animes/56-test",
            "kind": "tv",
            "score": "8.0",
            "status": "released",
            "episodes": 0,
            "episodes_aired": 0,
            "aired_on": "2014-01-01",
            "released_on": None,
        }
    ]


@pytest.fixture
def animes_list_resp(animes_list_json):
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
        for anime in animes_list_json
    ]


@pytest.fixture
def animes_byId_json():
    return {
        "id": 52991,
        "name": "Sousou no Frieren",
        "russian": "Провожающая в последний путь Фрирен",
        "image": {
            "original": "/system/animes/original/52991.jpg?1708300030",
            "preview": "/system/animes/preview/52991.jpg?1708300030",
            "x96": "/system/animes/x96/52991.jpg?1708300030",
            "x48": "/system/animes/x48/52991.jpg?1708300030",
        },
        "url": "/animes/52991-sousou-no-frieren",
        "kind": "tv",
        "score": "9.14",
        "status": "ongoing",
        "episodes": 28,
        "episodes_aired": 23,
        "aired_on": "2023-09-29",
        "released_on": "2024-03-22",
        "rating": "pg_13",
        "english": ["Frieren: Beyond Journey's End"],
        "japanese": ["葬送のフリーレン"],
        "synonyms": ["Фрирен, провожающая в последний путь", "Frieren at the Funeral"],
        "license_name_ru": None,
        "duration": 24,
        "description": "Одержав победу над Королём демонов, отряд героя [character=186854]Химмеля[/character] вернулся домой. Приключение, растянувшееся на десятилетие, подошло к завершению. Волшебница-эльф [character=184947]Фрирен[/character] и её отважные товарищи принесли людям мир и разошлись в разные стороны, чтобы спокойно прожить остаток жизни. Однако не всех членов отряда ждёт одинаковая участь. Для эльфов время течёт иначе, поэтому [character=184947]Фрирен[/character] вынужденно становится свидетелем того, как её спутники один за другим постепенно уходят из жизни. Девушка осознала, что годы, проведённые в отряде героя, пронеслись в один миг, как падающая звезда в бескрайнем космосе её жизни, и столкнулась с сожалениями об упущенных возможностях. Сможет ли она смириться со смертью друзей и понять, что значит жизнь для окружающих её людей? [character=184947]Фрирен[/character] начинает новое путешествие, чтобы найти ответ.",
        "description_html": '<div class="b-text_with_paragraphs">Одержав победу над Королём демонов, отряд героя <a href="https://shikimori.one/characters/186854-himmel" title="Himmel" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/186854-himmel/tooltip" data-attrs="{&quot;id&quot;:186854,&quot;type&quot;:&quot;character&quot;,&quot;name&quot;:&quot;Himmel&quot;,&quot;russian&quot;:&quot;Химмель&quot;}">Химмеля</a> вернулся домой. Приключение, растянувшееся на десятилетие, подошло к завершению. Волшебница-эльф <a href="https://shikimori.one/characters/184947-frieren" title="Frieren" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/184947-frieren/tooltip" data-attrs="{&quot;id&quot;:184947,&quot;type&quot;:&quot;character&quot;,&quot;name&quot;:&quot;Frieren&quot;,&quot;russian&quot;:&quot;Фрирен&quot;}">Фрирен</a> и её отважные товарищи принесли людям мир и разошлись в разные стороны, чтобы спокойно прожить остаток жизни. Однако не всех членов отряда ждёт одинаковая участь. Для эльфов время течёт иначе, поэтому <a href="https://shikimori.one/characters/184947-frieren" title="Frieren" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/184947-frieren/tooltip" data-attrs="{&quot;id&quot;:184947,&quot;type&quot;:&quot;character&quot;,&quot;name&quot;:&quot;Frieren&quot;,&quot;russian&quot;:&quot;Фрирен&quot;}">Фрирен</a> вынужденно становится свидетелем того, как её спутники один за другим постепенно уходят из жизни. Девушка осознала, что годы, проведённые в отряде героя, пронеслись в один миг, как падающая звезда в бескрайнем космосе её жизни, и столкнулась с сожалениями об упущенных возможностях. Сможет ли она смириться со смертью друзей и понять, что значит жизнь для окружающих её людей? <a href="https://shikimori.one/characters/184947-frieren" title="Frieren" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/184947-frieren/tooltip" data-attrs="{&quot;id&quot;:184947,&quot;type&quot;:&quot;character&quot;,&quot;name&quot;:&quot;Frieren&quot;,&quot;russian&quot;:&quot;Фрирен&quot;}">Фрирен</a> начинает новое путешествие, чтобы найти ответ.</div>',
        "description_source": None,
        "franchise": "frieren",
        "favoured": False,
        "anons": False,
        "ongoing": True,
        "thread_id": 477808,
        "topic_id": 477808,
        "myanimelist_id": 52991,
        "rates_scores_stats": [
            {"name": 10, "value": 5817},
            {"name": 9, "value": 2137},
            {"name": 8, "value": 1316},
            {"name": 7, "value": 513},
            {"name": 6, "value": 228},
            {"name": 5, "value": 115},
            {"name": 4, "value": 72},
            {"name": 3, "value": 40},
            {"name": 2, "value": 38},
            {"name": 1, "value": 220},
        ],
        "rates_statuses_stats": [
            {"name": "Запланировано", "value": 30989},
            {"name": "Просмотрено", "value": 2238},
            {"name": "Смотрю", "value": 29604},
            {"name": "Брошено", "value": 719},
            {"name": "Отложено", "value": 987},
        ],
        "updated_at": "2024-02-23T14:35:08.131+03:00",
        "next_episode_at": "2024-02-23T17:00:00.000+03:00",
        "fansubbers": [
            "Crunchyroll",
            "Kazoku Project",
            "AniRise",
            "YakuSub Studio",
            "Sanae",
        ],
        "fandubbers": [
            "AniStar",
            "AnimeVost",
            "AniMaunt",
            "AniLibria",
            "Комната Диди",
            "OnWave",
            "Кладбище топовых релизов",
            "Оканэ",
            "Dream Cast",
            "AniBaza",
            "AniDUB",
            "DubClub",
            "Amazing Dubbing",
            "FreeDub",
            "MoonWalkers",
            "Дубляжная",
            "Shiroi Kitsune",
            "Studio Band",
            "Невинный Кружок",
            "Kazoku Project",
            "AniFame",
            "AEROChannelEkat & Риша",
            "AniRise",
            "SHIZA Project",
        ],
        "licensors": [],
        "genres": [
            {
                "id": 2,
                "name": "Adventure",
                "russian": "Приключения",
                "kind": "genre",
                "entry_type": "Anime",
            },
            {
                "id": 8,
                "name": "Drama",
                "russian": "Драма",
                "kind": "genre",
                "entry_type": "Anime",
            },
            {
                "id": 10,
                "name": "Fantasy",
                "russian": "Фэнтези",
                "kind": "genre",
                "entry_type": "Anime",
            },
            {
                "id": 27,
                "name": "Shounen",
                "russian": "Сёнен",
                "kind": "genre",
                "entry_type": "Anime",
            },
        ],
        "studios": [
            {
                "id": 11,
                "name": "Madhouse",
                "filtered_name": "Madhouse",
                "real": True,
                "image": "/system/studios/original/11.png?1457607773",
            }
        ],
        "videos": [
            {
                "id": 53836,
                "url": "https://youtu.be/f5ZEiJyqDKU",
                "image_url": "http://img.youtube.com/vi/f5ZEiJyqDKU/hqdefault.jpg",
                "player_url": "http://youtube.com/embed/f5ZEiJyqDKU",
                "name": "PV1",
                "kind": "pv",
                "hosting": "youtube",
            },
            {
                "id": 54006,
                "url": "https://youtu.be/bTccQKVzVlk",
                "image_url": "http://img.youtube.com/vi/bTccQKVzVlk/hqdefault.jpg",
                "player_url": "http://youtube.com/embed/bTccQKVzVlk",
                "name": "PV1 (AniMeow) Субтитры",
                "kind": "pv",
                "hosting": "youtube",
            },
        ],
        "screenshots": [
            {
                "original": "/system/screenshots/original/b8a37b9a2b5e01e581f3313278a4e38bee9a1527.jpg?1696000681",
                "preview": "/system/screenshots/x332/b8a37b9a2b5e01e581f3313278a4e38bee9a1527.jpg?1696000681",
            },
            {
                "original": "/system/screenshots/original/de4d563c7524eb560351c6a166078f0a5f44407c.jpg?1696000683",
                "preview": "/system/screenshots/x332/de4d563c7524eb560351c6a166078f0a5f44407c.jpg?1696000683",
            },
        ],
        "user_rate": {
            "id": 163477825,
            "score": 10,
            "status": "watching",
            "text": None,
            "episodes": 23,
            "chapters": 0,
            "volumes": 0,
            "text_html": "",
            "rewatches": 0,
            "created_at": "2024-01-02T18:57:18.601+03:00",
            "updated_at": "2024-02-17T13:37:18.057+03:00",
        },
    }


@pytest.fixture
def animes_byId_resp(animes_byId_json):
    response = animes_byId_json
    return AnimeInfo(
        id=response["id"],
        name=response["name"],
        russian=response["russian"],
        image=Photo(**response["image"]),
        url=response["url"],
        kind=response["kind"],
        score=response["score"],
        status=response["status"],
        episodes=response["episodes"],
        episodes_aired=response["episodes_aired"],
        aired_on=response["aired_on"],
        released_on=response["released_on"],
        rating=response["rating"],
        english=response["english"],
        japanese=response["japanese"],
        synonyms=response["synonyms"],
        license_name_ru=response["license_name_ru"],
        duration=response["duration"],
        description=response["description"],
        description_html=response["description_html"],
        description_source=response["description_source"],
        franchise=response["franchise"],
        favoured=response["favoured"],
        anons=response["anons"],
        ongoing=response["ongoing"],
        thread_id=response["thread_id"],
        topic_id=response["topic_id"],
        myanimelist_id=response["myanimelist_id"],
        rates_scores_stats=response["rates_scores_stats"],
        rates_statuses_stats=response["rates_statuses_stats"],
        updated_at=response["updated_at"],
        next_episode_at=response["next_episode_at"],
        fansubbers=response["fansubbers"],
        fandubbers=response["fandubbers"],
        licensors=response["licensors"],
        genres=[GenreExtended(**genre) for genre in response.get("genres")],
        screenshots=[ScreenShot(**s) for s in response.get("screenshots")],
        studios=[Studio(**s) for s in response.get("studios")],
        videos=[Video(**v) for v in response.get("videos")],
        user_rate=(
            UserRateBrief(**response["user_rate"]) if response["user_rate"] else None
        ),
    )


@pytest.fixture
def animes_roles_json():
    return [
        {
            "roles": ["Main"],
            "roles_russian": ["Main"],
            "character": {
                "id": 188176,
                "name": "Fern",
                "russian": "Ферн",
                "image": {
                    "original": "/system/characters/original/188176.jpg?1707427942",
                    "preview": "/system/characters/preview/188176.jpg?1707427942",
                    "x96": "/system/characters/x96/188176.jpg?1707427942",
                    "x48": "/system/characters/x48/188176.jpg?1707427942",
                },
                "url": "/characters/188176-fern",
            },
            "person": None,
        },
        {
            "roles": ["2nd Key Animation"],
            "roles_russian": ["Второстепен. анимация"],
            "character": None,
            "person": {
                "id": 70719,
                "name": "Shiori Nakasone",
                "russian": "Сиори Накасонэ",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/people/70719-shiori-nakasone",
            },
        },
    ]


@pytest.fixture
def animes_roles_resp(animes_roles_json):
    return [
        Role(
            roles=role["roles"],
            roles_russian=role["roles_russian"],
            character=(
                CharacterBrief(
                    id=role["character"]["id"],
                    name=role["character"]["name"],
                    russian=role["character"]["russian"],
                    url=role["character"]["url"],
                    image=Photo(**role["character"]["image"]),
                )
                if role["character"]
                else None
            ),
            person=(
                CharacterBrief(
                    id=role["person"]["id"],
                    name=role["person"]["name"],
                    russian=role["person"]["russian"],
                    url=role["person"]["url"],
                    image=Photo(**role["person"]["image"]),
                )
                if role["person"]
                else None
            ),
        )
        for role in animes_roles_json
    ]


@pytest.fixture
def animes_related_json():
    return [
        {
            "relation": "Adaptation",
            "relation_russian": "Адаптация",
            "anime": None,
            "manga": {
                "id": 126287,
                "name": "Sousou no Frieren",
                "russian": "Провожающая в последний путь Фрирен",
                "image": {
                    "original": "/system/mangas/original/126287.jpg?1702362784",
                    "preview": "/system/mangas/preview/126287.jpg?1702362784",
                    "x96": "/system/mangas/x96/126287.jpg?1702362784",
                    "x48": "/system/mangas/x48/126287.jpg?1702362784",
                },
                "url": "/mangas/126287-sousou-no-frieren",
                "kind": "manga",
                "score": "8.68",
                "status": "ongoing",
                "volumes": 0,
                "chapters": 0,
                "aired_on": "2020-04-28",
                "released_on": None,
            },
        },
        {
            "relation": "Other",
            "relation_russian": "Прочее",
            "anime": {
                "id": 56805,
                "name": "Yuusha",
                "russian": "Герой",
                "image": {
                    "original": "/system/animes/original/56805.jpg?1705088737",
                    "preview": "/system/animes/preview/56805.jpg?1705088737",
                    "x96": "/system/animes/x96/56805.jpg?1705088737",
                    "x48": "/system/animes/x48/56805.jpg?1705088737",
                },
                "url": "/animes/56805-yuusha",
                "kind": "music",
                "score": "7.86",
                "status": "released",
                "episodes": 1,
                "episodes_aired": 0,
                "aired_on": "2023-09-29",
                "released_on": None,
            },
            "manga": None,
        },
        {
            "relation": "Side story",
            "relation_russian": "Другая история",
            "anime": {
                "id": 56885,
                "name": "Sousou no Frieren: ●● no Mahou",
                "russian": "Провожающая в последний путь Фрирен: Магия ●●",
                "image": {
                    "original": "/system/animes/original/56885.jpg?1708488937",
                    "preview": "/system/animes/preview/56885.jpg?1708488937",
                    "x96": "/system/animes/x96/56885.jpg?1708488937",
                    "x48": "/system/animes/x48/56885.jpg?1708488937",
                },
                "url": "/animes/56885-sousou-no-frieren-no-mahou",
                "kind": "ona",
                "score": "7.33",
                "status": "ongoing",
                "episodes": 0,
                "episodes_aired": 10,
                "aired_on": "2023-10-11",
                "released_on": None,
            },
            "manga": None,
        },
    ]


@pytest.fixture
def animes_related_resp(animes_related_json):
    return [
        Relation(
            relation=relation["relation"],
            relation_russian=relation["relation_russian"],
            anime=(
                Anime(
                    id=relation["anime"]["id"],
                    name=relation["anime"]["name"],
                    russian=relation["anime"]["russian"],
                    image=Photo(**relation["anime"]["image"]),
                    url=relation["anime"]["url"],
                    kind=relation["anime"]["kind"],
                    score=relation["anime"]["score"],
                    status=relation["anime"]["status"],
                    episodes=relation["anime"]["episodes"],
                    episodes_aired=relation["anime"]["episodes_aired"],
                    aired_on=relation["anime"]["aired_on"],
                    released_on=relation["anime"]["released_on"],
                )
                if relation["anime"]
                else None
            ),
            manga=(
                Manga(
                    id=relation["manga"]["id"],
                    name=relation["manga"]["name"],
                    russian=relation["manga"]["russian"],
                    image=Photo(**relation["manga"]["image"]),
                    url=relation["manga"]["url"],
                    kind=relation["manga"]["kind"],
                    score=relation["manga"]["score"],
                    status=relation["manga"]["status"],
                    chapters=relation["manga"]["chapters"],
                    volumes=relation["manga"]["volumes"],
                    aired_on=relation["manga"]["aired_on"],
                    released_on=relation["manga"]["released_on"],
                )
                if relation["manga"]
                else None
            ),
        )
        for relation in animes_related_json
    ]


@pytest.fixture
def animes_screenshots_json():
    return [
        {
            "original": "/system/screenshots/original/b8a37b9a2b5e01e581f3313278a4e38bee9a1527.jpg?1696000681",
            "preview": "/system/screenshots/x332/b8a37b9a2b5e01e581f3313278a4e38bee9a1527.jpg?1696000681",
        },
        {
            "original": "/system/screenshots/original/de4d563c7524eb560351c6a166078f0a5f44407c.jpg?1696000683",
            "preview": "/system/screenshots/x332/de4d563c7524eb560351c6a166078f0a5f44407c.jpg?1696000683",
        },
    ]


@pytest.fixture
def animes_screenshots_resp(animes_screenshots_json):
    return [ScreenShot(**s) for s in animes_screenshots_json]


@pytest.fixture
def animes_franchise_json():
    return {
        "links": [
            {
                "id": 33316685,
                "source_id": 52991,
                "target_id": 56805,
                "source": 2,
                "target": 1,
                "weight": 2,
                "relation": "other",
            },
            {
                "id": 33316686,
                "source_id": 52991,
                "target_id": 56885,
                "source": 2,
                "target": 0,
                "weight": 2,
                "relation": "side_story",
            },
            {
                "id": 33309900,
                "source_id": 56805,
                "target_id": 52991,
                "source": 1,
                "target": 2,
                "weight": 1,
                "relation": "other",
            },
            {
                "id": 33317008,
                "source_id": 56885,
                "target_id": 52991,
                "source": 0,
                "target": 2,
                "weight": 1,
                "relation": "parent_story",
            },
        ],
        "nodes": [
            {
                "id": 56885,
                "date": 1696971600,
                "name": "Провожающая в последний путь Фрирен: Магия ●●",
                "image_url": "https://desu.shikimori.one/system/animes/x96/56885.jpg?1708488937",
                "url": "/animes/56885-sousou-no-frieren-no-mahou",
                "year": 2023,
                "kind": "ONA",
                "weight": 1,
            },
            {
                "id": 56805,
                "date": 1695934800,
                "name": "Герой",
                "image_url": "https://desu.shikimori.one/system/animes/x96/56805.jpg?1705088737",
                "url": "/animes/56805-yuusha",
                "year": 2023,
                "kind": "Клип",
                "weight": 1,
            },
            {
                "id": 52991,
                "date": 1695934800,
                "name": "Провожающая в последний путь Фрирен",
                "image_url": "https://desu.shikimori.one/system/animes/x96/52991.jpg?1708300030",
                "url": "/animes/52991-sousou-no-frieren",
                "year": 2023,
                "kind": "TV Сериал",
                "weight": 2,
            },
        ],
        "current_id": 52991,
    }


@pytest.fixture
def animes_franchise_resp(animes_franchise_json):
    return Franchise(
        nodes=[Node(**node) for node in animes_franchise_json.get("nodes")],
        links=[Link(**link) for link in animes_franchise_json.get("links")],
        current_id=animes_franchise_json["current_id"],
    )


@pytest.fixture
def animes_external_json():
    return [
        {
            "id": 3,
            "kind": "wikipedia",
            "url": "http://en.wikipedia.org",
            "source": "shikimori",
            "entry_id": 49,
            "entry_type": "Anime",
            "created_at": "2022-11-26T17:19:33.393+03:00",
            "updated_at": "2022-11-26T17:19:33.393+03:00",
            "imported_at": None,
        },
        {
            "id": None,
            "kind": "myanimelist",
            "url": "http://myanimelist.net/anime/123",
            "source": "myanimelist",
            "entry_id": 49,
            "entry_type": "Anime",
            "created_at": None,
            "updated_at": None,
            "imported_at": None,
        },
    ]


@pytest.fixture
def animes_external_resp(animes_external_json):
    return [ExternalLink(**s) for s in animes_external_json]


@pytest.fixture
def animes_topics_json():
    return [
        {
            "id": 539109,
            "topic_title": "Sousou no Frieren",
            "body": "",
            "html_body": "",
            "html_footer": "",
            "created_at": "2024-02-16T18:17:10.000+03:00",
            "comments_count": 0,
            "forum": {
                "id": 1,
                "position": 1,
                "name": "Аниме и манга",
                "permalink": "animanga",
                "url": "/forum/animanga",
            },
            "user": {
                "id": 15,
                "nickname": "Минацу-тян",
                "avatar": "https://desu.shikimori.one/system/users/x48/15.png?1447460712",
                "image": {
                    "x160": "https://desu.shikimori.one/system/users/x160/15.png?1447460712",
                    "x148": "https://desu.shikimori.one/system/users/x148/15.png?1447460712",
                    "x80": "https://desu.shikimori.one/system/users/x80/15.png?1447460712",
                    "x64": "https://desu.shikimori.one/system/users/x64/15.png?1447460712",
                    "x48": "https://desu.shikimori.one/system/users/x48/15.png?1447460712",
                    "x32": "https://desu.shikimori.one/system/users/x32/15.png?1447460712",
                    "x16": "https://desu.shikimori.one/system/users/x16/15.png?1447460712",
                },
                "last_online_at": "2011-01-25T22:06:53.000+03:00",
                "url": "https://shikimori.one/%D0%9C%D0%B8%D0%BD%D0%B0%D1%86%D1%83-%D1%82%D1%8F%D0%BD",
            },
            "type": "Topics::NewsTopic",
            "linked_id": 52991,
            "linked_type": "Anime",
            "linked": {
                "id": 52991,
                "name": "Sousou no Frieren",
                "russian": "Провожающая в последний путь Фрирен",
                "image": {
                    "original": "/system/animes/original/52991.jpg?1708300030",
                    "preview": "/system/animes/preview/52991.jpg?1708300030",
                    "x96": "/system/animes/x96/52991.jpg?1708300030",
                    "x48": "/system/animes/x48/52991.jpg?1708300030",
                },
                "url": "/animes/52991-sousou-no-frieren",
                "kind": "tv",
                "score": "9.14",
                "status": "ongoing",
                "episodes": 28,
                "episodes_aired": 23,
                "aired_on": "2023-09-29",
                "released_on": "2024-03-22",
            },
            "viewed": True,
            "last_comment_viewed": None,
            "event": "episode",
            "episode": 23,
        },
        {
            "id": 538388,
            "topic_title": "Sousou no Frieren",
            "body": "",
            "html_body": "",
            "html_footer": "",
            "created_at": "2024-02-09T18:26:21.000+03:00",
            "comments_count": 0,
            "forum": {
                "id": 1,
                "position": 1,
                "name": "Аниме и манга",
                "permalink": "animanga",
                "url": "/forum/animanga",
            },
            "user": {
                "id": 16,
                "nickname": "Ака-тян",
                "avatar": "https://desu.shikimori.one/system/users/x48/16.png?1447460712",
                "image": {
                    "x160": "https://desu.shikimori.one/system/users/x160/16.png?1447460712",
                    "x148": "https://desu.shikimori.one/system/users/x148/16.png?1447460712",
                    "x80": "https://desu.shikimori.one/system/users/x80/16.png?1447460712",
                    "x64": "https://desu.shikimori.one/system/users/x64/16.png?1447460712",
                    "x48": "https://desu.shikimori.one/system/users/x48/16.png?1447460712",
                    "x32": "https://desu.shikimori.one/system/users/x32/16.png?1447460712",
                    "x16": "https://desu.shikimori.one/system/users/x16/16.png?1447460712",
                },
                "last_online_at": "2014-05-25T23:56:07.000+04:00",
                "url": "https://shikimori.one/%D0%90%D0%BA%D0%B0-%D1%82%D1%8F%D0%BD",
            },
            "type": "Topics::NewsTopic",
            "linked_id": 52991,
            "linked_type": "Anime",
            "linked": {
                "id": 52991,
                "name": "Sousou no Frieren",
                "russian": "Провожающая в последний путь Фрирен",
                "image": {
                    "original": "/system/animes/original/52991.jpg?1708300030",
                    "preview": "/system/animes/preview/52991.jpg?1708300030",
                    "x96": "/system/animes/x96/52991.jpg?1708300030",
                    "x48": "/system/animes/x48/52991.jpg?1708300030",
                },
                "url": "/animes/52991-sousou-no-frieren",
                "kind": "tv",
                "score": "9.14",
                "status": "ongoing",
                "episodes": 28,
                "episodes_aired": 23,
                "aired_on": "2023-09-29",
                "released_on": "2024-03-22",
            },
            "viewed": True,
            "last_comment_viewed": None,
            "event": "episode",
            "episode": 22,
        },
    ]


@pytest.fixture
def animes_topics_resp(animes_topics_json):
    return [
        Topic(
            id=topic["id"],
            topic_title=topic["topic_title"],
            body=topic["body"],
            html_body=topic["html_body"],
            html_footer=topic["html_footer"],
            created_at=topic["created_at"],
            comments_count=topic["comments_count"],
            type=topic["type"],
            linked_id=topic["linked_id"],
            linked_type=topic["linked_type"],
            viewed=topic["viewed"],
            last_comment_viewed=topic["last_comment_viewed"],
            event=topic["event"],
            episode=topic["episode"],
            forum=Forum(**topic["forum"]),
            user=User(
                id=topic["user"]["id"],
                nickname=topic["user"]["nickname"],
                avatar=topic["user"]["avatar"],
                last_online_at=topic["user"]["last_online_at"],
                url=topic["user"]["url"],
                image=PhotoExtended(**topic["user"]["image"]),
            ),
            linked=Linked(
                name=topic["linked"]["name"],
                id=topic["linked"]["id"],
                russian=topic["linked"]["russian"],
                url=topic["linked"]["url"],
                kind=topic["linked"]["kind"],
                score=topic["linked"]["score"],
                status=topic["linked"]["status"],
                episodes=topic["linked"]["episodes"],
                episodes_aired=topic["linked"]["episodes_aired"],
                aired_on=topic["linked"]["aired_on"],
                released_on=topic["linked"]["released_on"],
                image=Photo(**topic["linked"]["image"]),
            ),
        )
        for topic in animes_topics_json
    ]
