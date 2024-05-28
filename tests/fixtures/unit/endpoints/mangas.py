import pytest

from shikimori.endpoints.manga import MangaEndpoint
from shikimori.types.animes import Anime, Relation
from shikimori.types.externalLink import ExternalLink
from shikimori.types.franchise import Franchise, Node, Link
from shikimori.types.genres import Genre
from shikimori.types.manga import Manga, MangaInfo
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.roles import Role
from shikimori.types.character import CharacterBrief
from shikimori.types.topics import Topic, Forum, Linked
from shikimori.types.user import User
from shikimori.types.user_rates import UserRateBrief


@pytest.fixture
def manga_client():
    return MangaEndpoint("", "", "")


@pytest.fixture
def mangas_list_json():
    return [
        {
            "id": 24,
            "name": "Test",
            "russian": "манга_13",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/mangas/24-test",
            "kind": "manga",
            "score": "1.0",
            "status": "released",
            "volumes": 0,
            "chapters": 0,
            "aired_on": "2014-01-01",
            "released_on": None,
        }
    ]


@pytest.fixture
def mangas_list_resp(mangas_list_json):
    return [
        Manga(
            id=s["id"],
            name=s["name"],
            russian=s["russian"],
            image=Photo(**s["image"]),
            url=s["url"],
            kind=s["kind"],
            score=s["score"],
            status=s["status"],
            chapters=s["chapters"],
            volumes=s["volumes"],
            aired_on=s["aired_on"],
            released_on=s["released_on"],
        )
        for s in mangas_list_json
    ]


@pytest.fixture
def mangas_ById_json():
    return {
        "id": 27,
        "name": "manga_13",
        "russian": "манга_16",
        "image": {
            "original": "/assets/globals/missing_original.jpg",
            "preview": "/assets/globals/missing_preview.jpg",
            "x96": "/assets/globals/missing_x96.jpg",
            "x48": "/assets/globals/missing_x48.jpg",
        },
        "url": "/mangas/27-manga-13",
        "kind": "manga",
        "score": "1.0",
        "status": "released",
        "volumes": 0,
        "chapters": 0,
        "aired_on": None,
        "released_on": None,
        "english": [None],
        "japanese": [None],
        "synonyms": [],
        "license_name_ru": None,
        "description": None,
        "description_html": '<div class="b-text_with_paragraphs"></div>',
        "description_source": None,
        "franchise": None,
        "favoured": False,
        "anons": False,
        "ongoing": False,
        "thread_id": 270112,
        "topic_id": 270112,
        "myanimelist_id": 27,
        "rates_scores_stats": [],
        "rates_statuses_stats": [],
        "licensors": [],
        "genres": [],
        "publishers": [],
        "user_rate": None,
    }


@pytest.fixture
def mangas_ById_resp(mangas_ById_json):
    response = mangas_ById_json
    return MangaInfo(
        id=response["id"],
        name=response["name"],
        russian=response["russian"],
        image=Photo(**response["image"]),
        url=response["url"],
        kind=response["kind"],
        score=response["score"],
        status=response["status"],
        volumes=response["volumes"],
        chapters=response["chapters"],
        aired_on=response["aired_on"],
        released_on=response["released_on"],
        english=response["english"],
        japanese=response["japanese"],
        synonyms=response["synonyms"],
        license_name_ru=response["license_name_ru"],
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
        licensors=response["licensors"],
        genres=[Genre(**genre) for genre in response["genres"]],
        user_rate=(
            UserRateBrief(**response["user_rate"]) if response["user_rate"] else None
        ),
    )


@pytest.fixture
def mangas_roles_json():
    return [
        {
            "roles": ["Main"],
            "roles_russian": ["Main"],
            "character": {
                "id": 4,
                "name": "character_4",
                "russian": "персонаж_4",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/characters/4-character-4",
            },
            "person": None,
        },
        {
            "roles": ["Director"],
            "roles_russian": ["Режиссёр"],
            "character": None,
            "person": {
                "id": 2,
                "name": "person_2",
                "russian": "человек_2",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/people/2-person-2",
            },
        },
    ]


@pytest.fixture
def mangas_roles_resp(mangas_roles_json):
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
        for role in mangas_roles_json
    ]


@pytest.fixture
def mangas_similar_json():
    return [
        {
            "id": 23,
            "name": "manga_10",
            "russian": "манга_12",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/mangas/23-manga-10",
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
def mangas_similar_resp(mangas_similar_json):
    return [
        Manga(
            id=s["id"],
            name=s["name"],
            russian=s["russian"],
            image=Photo(**s["image"]),
            url=s["url"],
            kind=s["kind"],
            score=s["score"],
            status=s["status"],
            chapters=s["chapters"],
            volumes=s["volumes"],
            aired_on=s["aired_on"],
            released_on=s["released_on"],
        )
        for s in mangas_similar_json
    ]


@pytest.fixture
def mangas_related_json():
    return [
        {
            "relation": "Adaptation",
            "relation_russian": "Адаптация",
            "anime": None,
            "manga": {
                "id": 16,
                "name": "manga_5",
                "russian": "манга_5",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/mangas/16-manga-5",
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
def mangas_related_resp(mangas_related_json):
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
        for relation in mangas_related_json
    ]


@pytest.fixture
def mangas_franchise_json():
    return {
        "links": [],
        "nodes": [
            {
                "id": 17,
                "date": 1669472370,
                "name": "манга_6",
                "image_url": "/assets/globals/missing_x96.jpg",
                "url": "/mangas/17-manga-6",
                "year": None,
                "kind": "Манга",
                "weight": 1,
            }
        ],
        "current_id": 17,
    }


@pytest.fixture
def mangas_franchise_resp(mangas_franchise_json):
    return Franchise(
        nodes=[Node(**node) for node in mangas_franchise_json.get("nodes")],
        links=[Link(**link) for link in mangas_franchise_json.get("links")],
        current_id=mangas_franchise_json["current_id"],
    )


@pytest.fixture
def mangas_ExternalLinks_json():
    return [
        {
            "id": 2,
            "kind": "wikipedia",
            "url": "http://en.wikipedia.org",
            "source": "shikimori",
            "entry_id": 19,
            "entry_type": "Manga",
            "created_at": "2022-11-26T17:19:30.181+03:00",
            "updated_at": "2022-11-26T17:19:30.181+03:00",
            "imported_at": None,
        },
        {
            "id": None,
            "kind": "myanimelist",
            "url": "http://myanimelist.net/manga/123",
            "source": "myanimelist",
            "entry_id": 19,
            "entry_type": "Manga",
            "created_at": None,
            "updated_at": None,
            "imported_at": None,
        },
    ]


@pytest.fixture
def mangas_ExternalLinks_resp(mangas_ExternalLinks_json):
    return [ExternalLink(**s) for s in mangas_ExternalLinks_json]


@pytest.fixture
def mangas_topics_json():
    return [
        {
            "id": 270111,
            "topic_title": "topic_4",
            "body": "topic_text_4",
            "html_body": "topic_text_4",
            "html_footer": "",
            "created_at": "2022-11-26T17:19:30.292+03:00",
            "comments_count": 0,
            "forum": {
                "id": 8,
                "position": 0,
                "name": "Оффтопик",
                "permalink": "offtopic",
                "url": "/forum/offtopic",
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
            "linked_id": 25,
            "linked_type": "Manga",
            "linked": {
                "id": 25,
                "name": "manga_11",
                "russian": "манга_14",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/mangas/25-manga-11",
                "kind": "manga",
                "score": "1.0",
                "status": "released",
                "volumes": 0,
                "chapters": 0,
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
def mangas_topics_resp(mangas_topics_json):
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
                volumes=topic["linked"]["volumes"],
                chapters=topic["linked"]["chapters"],
                aired_on=topic["linked"]["aired_on"],
                released_on=topic["linked"]["released_on"],
                image=Photo(**topic["linked"]["image"]),
            ),
        )
        for topic in mangas_topics_json
    ]
