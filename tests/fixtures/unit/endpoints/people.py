import pytest

from shikimori.endpoints.people import PeopleEndpoint
from shikimori.types.animes import Anime
from shikimori.types.base import BaseCharacter
from shikimori.types.manga import Manga
from shikimori.types.people import People, Date, Works, Role
from shikimori.types.photo import Photo


@pytest.fixture
def people_client():
    return PeopleEndpoint("", "", "")


@pytest.fixture
def people_byid_json():
    return {
        "id": 4123,
        "name": "Komomo Yamada",
        "russian": "Комомо Ямада",
        "image": {
            "original": "/system/people/original/4123.jpg?1702242395",
            "preview": "/system/people/preview/4123.jpg?1702242395",
            "x96": "/system/people/x96/4123.jpg?1702242395",
            "x48": "/system/people/x48/4123.jpg?1702242395",
        },
        "url": "/people/4123-komomo-yamada",
        "japanese": "山田 こもも",
        "job_title": "Автор манги",
        "birth_on": {},
        "deceased_on": {},
        "website": "",
        "groupped_roles": [["Сюжет и иллюстрации", 16]],
        "roles": [],
        "works": [
            {
                "anime": None,
                "manga": {
                    "id": 67995,
                    "name": "Kore kara Hajimaru Koi wo Oshiete",
                    "russian": "Научи меня любить",
                    "image": {
                        "original": "/system/mangas/original/67995.jpg?1708786846",
                        "preview": "/system/mangas/preview/67995.jpg?1708786846",
                        "x96": "/system/mangas/x96/67995.jpg?1708786846",
                        "x48": "/system/mangas/x48/67995.jpg?1708786846",
                    },
                    "url": "/mangas/67995-kore-kara-hajimaru-koi-wo-oshiete",
                    "kind": "manga",
                    "score": "7.2",
                    "status": "released",
                    "volumes": 4,
                    "chapters": 20,
                    "aired_on": "2013-08-08",
                    "released_on": "2015-01-08",
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 4687,
                    "name": "Hadaka no Ouji-sama: Love Kingdom",
                    "russian": "Избалованный принц",
                    "image": {
                        "original": "/system/mangas/original/4687.jpg?1702208207",
                        "preview": "/system/mangas/preview/4687.jpg?1702208207",
                        "x96": "/system/mangas/x96/4687.jpg?1702208207",
                        "x48": "/system/mangas/x48/4687.jpg?1702208207",
                    },
                    "url": "/mangas/4687-hadaka-no-ouji-sama-love-kingdom",
                    "kind": "manga",
                    "score": "7.2",
                    "status": "released",
                    "volumes": 3,
                    "chapters": 10,
                    "aired_on": "2007-01-01",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 4683,
                    "name": "Otona no Jikan",
                    "russian": "Время взрослеть",
                    "image": {
                        "original": "/system/mangas/original/4683.jpg?1708866597",
                        "preview": "/system/mangas/preview/4683.jpg?1708866597",
                        "x96": "/system/mangas/x96/4683.jpg?1708866597",
                        "x48": "/system/mangas/x48/4683.jpg?1708866597",
                    },
                    "url": "/mangas/4683-otona-no-jikan",
                    "kind": "manga",
                    "score": "7.18",
                    "status": "released",
                    "volumes": 7,
                    "chapters": 28,
                    "aired_on": "2004-11-24",
                    "released_on": "2007-02-24",
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 4684,
                    "name": "Goshujinsama to Watashi",
                    "russian": "Мастер и я",
                    "image": {
                        "original": "/system/mangas/original/4684.jpg?1702207137",
                        "preview": "/system/mangas/preview/4684.jpg?1702207137",
                        "x96": "/system/mangas/x96/4684.jpg?1702207137",
                        "x48": "/system/mangas/x48/4684.jpg?1702207137",
                    },
                    "url": "/mangas/4684-goshujinsama-to-watashi",
                    "kind": "manga",
                    "score": "6.96",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 0,
                    "aired_on": None,
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 4686,
                    "name": "Kojin Jugyou",
                    "russian": "Частные уроки",
                    "image": {
                        "original": "/system/mangas/original/4686.jpg?1708786078",
                        "preview": "/system/mangas/preview/4686.jpg?1708786078",
                        "x96": "/system/mangas/x96/4686.jpg?1708786078",
                        "x48": "/system/mangas/x48/4686.jpg?1708786078",
                    },
                    "url": "/mangas/4686-kojin-jugyou",
                    "kind": "manga",
                    "score": "6.95",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 0,
                    "aired_on": "2005-01-01",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 13021,
                    "name": "Gokujou Koibana: Perfect Love Stories Best 5",
                    "russian": "Пять лучших историй об идеальной любви",
                    "image": {
                        "original": "/system/mangas/original/13021.jpg?1702206766",
                        "preview": "/system/mangas/preview/13021.jpg?1702206766",
                        "x96": "/system/mangas/x96/13021.jpg?1702206766",
                        "x48": "/system/mangas/x48/13021.jpg?1702206766",
                    },
                    "url": "/mangas/13021-gokujou-koibana-perfect-love-stories-best-5",
                    "kind": "manga",
                    "score": "6.93",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 5,
                    "aired_on": None,
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 13233,
                    "name": "Mainichi Kimi ni Koishiteru",
                    "russian": "Влюбляюсь в тебя каждый день",
                    "image": {
                        "original": "/system/mangas/original/13233.jpg?1708792371",
                        "preview": "/system/mangas/preview/13233.jpg?1708792371",
                        "x96": "/system/mangas/x96/13233.jpg?1708792371",
                        "x48": "/system/mangas/x48/13233.jpg?1708792371",
                    },
                    "url": "/mangas/13233-mainichi-kimi-ni-koishiteru",
                    "kind": "manga",
                    "score": "6.87",
                    "status": "released",
                    "volumes": 2,
                    "chapters": 8,
                    "aired_on": "2008-01-01",
                    "released_on": "2009-01-01",
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 4685,
                    "name": "Saikyou Koibana: Sweet & Erotic Best 5",
                    "russian": "Сильные любовные истории",
                    "image": {
                        "original": "/system/mangas/original/4685.jpg?1708873630",
                        "preview": "/system/mangas/preview/4685.jpg?1708873630",
                        "x96": "/system/mangas/x96/4685.jpg?1708873630",
                        "x48": "/system/mangas/x48/4685.jpg?1708873630",
                    },
                    "url": "/mangas/4685-saikyou-koibana-sweet-erotic-best-5",
                    "kind": "manga",
                    "score": "6.85",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 5,
                    "aired_on": "2007-08-24",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 7790,
                    "name": "Darenimo Himitsu no Koimonogatari",
                    "russian": "Тайные истории любви",
                    "image": {
                        "original": "/system/mangas/original/7790.jpg?1702193784",
                        "preview": "/system/mangas/preview/7790.jpg?1702193784",
                        "x96": "/system/mangas/x96/7790.jpg?1702193784",
                        "x48": "/system/mangas/x48/7790.jpg?1702193784",
                    },
                    "url": "/mangas/7790-darenimo-himitsu-no-koimonogatari",
                    "kind": "manga",
                    "score": "6.69",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 6,
                    "aired_on": "2004-09-24",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 16797,
                    "name": "Erotic Horror",
                    "russian": "Мистика любви: Кошмар в летнюю ночь",
                    "image": {
                        "original": "/system/mangas/original/16797.jpg?1702199701",
                        "preview": "/system/mangas/preview/16797.jpg?1702199701",
                        "x96": "/system/mangas/x96/16797.jpg?1702199701",
                        "x48": "/system/mangas/x48/16797.jpg?1702199701",
                    },
                    "url": "/mangas/16797-erotic-horror",
                    "kind": "manga",
                    "score": "6.58",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 5,
                    "aired_on": "2009-08-10",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 36483,
                    "name": "8-banme no Tsumi",
                    "russian": "Ошибка № 8",
                    "image": {
                        "original": "/system/mangas/original/36483.jpg?1702175003",
                        "preview": "/system/mangas/preview/36483.jpg?1702175003",
                        "x96": "/system/mangas/x96/36483.jpg?1702175003",
                        "x48": "/system/mangas/x48/36483.jpg?1702175003",
                    },
                    "url": "/mangas/36483-8-banme-no-tsumi",
                    "kind": "manga",
                    "score": "6.41",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 3,
                    "aired_on": "2009-01-01",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 89586,
                    "name": "Zettai Toudo",
                    "russian": "На 100% сладкий",
                    "image": {
                        "original": "/system/mangas/original/89586.jpg?1708934167",
                        "preview": "/system/mangas/preview/89586.jpg?1708934167",
                        "x96": "/system/mangas/x96/89586.jpg?1708934167",
                        "x48": "/system/mangas/x48/89586.jpg?1708934167",
                    },
                    "url": "/mangas/89586-zettai-toudo",
                    "kind": "manga",
                    "score": "0.0",
                    "status": "released",
                    "volumes": 2,
                    "chapters": 10,
                    "aired_on": "2015-05-08",
                    "released_on": "2016-01-08",
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 112457,
                    "name": "Koibito wa Dannasama",
                    "russian": "Мой муж — мой любовник",
                    "image": {
                        "original": "/system/mangas/original/112457.jpg?1708785701",
                        "preview": "/system/mangas/preview/112457.jpg?1708785701",
                        "x96": "/system/mangas/x96/112457.jpg?1708785701",
                        "x48": "/system/mangas/x48/112457.jpg?1708785701",
                    },
                    "url": "/mangas/112457-koibito-wa-dannasama",
                    "kind": "manga",
                    "score": "0.0",
                    "status": "ongoing",
                    "volumes": 0,
                    "chapters": 0,
                    "aired_on": "2017-06-08",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 94599,
                    "name": "Koibito ni Naru Jikan desu",
                    "russian": "",
                    "image": {
                        "original": "/system/mangas/original/94599.jpg?1708785648",
                        "preview": "/system/mangas/preview/94599.jpg?1708785648",
                        "x96": "/system/mangas/x96/94599.jpg?1708785648",
                        "x48": "/system/mangas/x48/94599.jpg?1708785648",
                    },
                    "url": "/mangas/94599-koibito-ni-naru-jikan-desu",
                    "kind": "manga",
                    "score": "0.0",
                    "status": "released",
                    "volumes": 3,
                    "chapters": 15,
                    "aired_on": "2012-02-08",
                    "released_on": "2013-03-08",
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 58109,
                    "name": "Hatsukoi wa Kanawanai",
                    "russian": "Первая любовь неизбежна",
                    "image": {
                        "original": "/system/mangas/original/58109.jpg?1702212668",
                        "preview": "/system/mangas/preview/58109.jpg?1702212668",
                        "x96": "/system/mangas/x96/58109.jpg?1702212668",
                        "x48": "/system/mangas/x48/58109.jpg?1702212668",
                    },
                    "url": "/mangas/58109-hatsukoi-wa-kanawanai",
                    "kind": "manga",
                    "score": "0.0",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 5,
                    "aired_on": None,
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
            {
                "anime": None,
                "manga": {
                    "id": 14169,
                    "name": "Kinkyori Lovers",
                    "russian": "",
                    "image": {
                        "original": "/system/mangas/original/14169.jpg?1708783981",
                        "preview": "/system/mangas/preview/14169.jpg?1708783981",
                        "x96": "/system/mangas/x96/14169.jpg?1708783981",
                        "x48": "/system/mangas/x48/14169.jpg?1708783981",
                    },
                    "url": "/mangas/14169-kinkyori-lovers",
                    "kind": "manga",
                    "score": "0.0",
                    "status": "released",
                    "volumes": 1,
                    "chapters": 0,
                    "aired_on": "2009-01-01",
                    "released_on": None,
                },
                "role": "Сюжет и иллюстрации",
            },
        ],
        "topic_id": 202001,
        "person_favoured": False,
        "producer": False,
        "producer_favoured": False,
        "mangaka": False,
        "mangaka_favoured": False,
        "seyu": False,
        "seyu_favoured": False,
        "updated_at": "2024-02-26T23:35:43.319+03:00",
        "thread_id": 202001,
        "birthday": {},
    }


@pytest.fixture
def people_byid_resp(people_byid_json):
    response = people_byid_json
    return People(
        id=response["id"],
        website=response["website"],
        url=response["url"],
        updated_at=response["url"],
        russian=response["russian"],
        groupped_roles=response["groupped_roles"],
        mangaka_favoured=response["mangaka_favoured"],
        mangaka=response["mangaka"],
        thread_id=response["thread_id"],
        name=response["name"],
        japanese=response["japanese"],
        seyu_favoured=response["seyu_favoured"],
        person_favoured=response["person_favoured"],
        producer_favoured=response["producer_favoured"],
        seyu=response["seyu"],
        job_title=response["job_title"],
        producer=response["producer"],
        topic_id=response["topic_id"],
        birth_on=Date(**response["birth_on"]),
        deceased_on=Date(**response["deceased_on"]),
        birthday=Date(**response["birthday"]),
        image=Photo(**response["image"]),
        works=[
            Works(
                anime=(
                    Anime(
                        id=work["anime"]["id"],
                        name=work["anime"]["name"],
                        russian=work["anime"]["russian"],
                        image=Photo(**work["anime"]["image"]),
                        url=work["anime"]["url"],
                        kind=work["anime"]["kind"],
                        score=work["anime"]["score"],
                        status=work["anime"]["status"],
                        episodes=work["anime"]["episodes"],
                        episodes_aired=work["anime"]["episodes_aired"],
                        aired_on=work["anime"]["aired_on"],
                        released_on=work["anime"]["released_on"],
                    )
                    if work.get("anime")
                    else None
                ),
                manga=(
                    Manga(
                        id=work["manga"]["id"],
                        name=work["manga"]["name"],
                        russian=work["manga"]["russian"],
                        image=Photo(**work["manga"]["image"]),
                        url=work["manga"]["url"],
                        kind=work["manga"]["kind"],
                        score=work["manga"]["score"],
                        status=work["manga"]["status"],
                        chapters=work["manga"]["chapters"],
                        volumes=work["manga"]["volumes"],
                        aired_on=work["manga"]["aired_on"],
                        released_on=work["manga"]["released_on"],
                    )
                    if work.get("manga")
                    else None
                ),
                role=work["role"],
            )
            for work in response["works"]
        ],
        roles=[
            Role(
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
                    for anime in role["animes"]
                ],
                characters=[
                    BaseCharacter(
                        image=Photo(**s["image"]),
                        id=s["id"],
                        name=s["name"],
                        russian=s["russian"],
                        url=s["url"],
                    )
                    for s in role["characters"]
                ],
            )
            for role in response["roles"]
        ],
    )


@pytest.fixture
def people_search_json():
    return [
  {
    "id": 5,
    "name": "asdf",
    "russian": "человек_5",
    "image": {
      "original": "/assets/globals/missing_original.jpg",
      "preview": "/assets/globals/missing_preview.jpg",
      "x96": "/assets/globals/missing_x96.jpg",
      "x48": "/assets/globals/missing_x48.jpg"
    },
    "url": "/people/5-asdf"
  }
]

@pytest.fixture
def people_search_resp(people_search_json):
    return [
                BaseCharacter(
                    id=ch["id"],
                    russian=ch["russian"],
                    url=ch["url"],
                    name=ch["name"],
                    image=Photo(**ch["image"]),
                )
                for ch in people_search_json
            ]