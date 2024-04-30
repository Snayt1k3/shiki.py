import pytest
from shikimori.endpoints.calendar import CalendarEndpoint
from shikimori.types.calendar import Calendar
from shikimori.types.photo import Photo
from shikimori.types.animes import Anime


@pytest.fixture
def calendar_client():
    return CalendarEndpoint("", "", "")


@pytest.fixture
def calendar_list_json():
    return [
        {
            "next_episode": 1,
            "next_episode_at": "2016-09-04T09:00:00.000+03:00",
            "duration": None,
            "anime": {
                "id": 20,
                "name": "anime_20",
                "russian": "аниме_20",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/20-anime-20",
                "kind": "tv",
                "score": "1.0",
                "status": "ongoing",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": "2016-09-04",
                "released_on": None,
            },
        },
        {
            "next_episode": 1,
            "next_episode_at": "2016-09-12T09:00:00.000+03:00",
            "duration": None,
            "anime": {
                "id": 26,
                "name": "anime_26",
                "russian": "аниме_26",
                "image": {
                    "original": "/assets/globals/missing_original.jpg",
                    "preview": "/assets/globals/missing_preview.jpg",
                    "x96": "/assets/globals/missing_x96.jpg",
                    "x48": "/assets/globals/missing_x48.jpg",
                },
                "url": "/animes/26-anime-26",
                "kind": "tv",
                "score": "1.0",
                "status": "anons",
                "episodes": 0,
                "episodes_aired": 0,
                "aired_on": "2016-09-12",
                "released_on": None,
            },
        },
    ]


@pytest.fixture
def calendar_list_resp(calendar_list_json):
    return [
        Calendar(
            next_episode=b["next_episode"],
            duration=b["duration"],
            next_episode_at=b["next_episode_at"],
            anime=Anime(
                id=b["anime"]["id"],
                name=b["anime"]["name"],
                russian=b["anime"]["russian"],
                aired_on=b["anime"]["aired_on"],
                episodes=b["anime"]["episodes"],
                episodes_aired=b["anime"]["episodes_aired"],
                kind=b["anime"]["kind"],
                released_on=b["anime"]["released_on"],
                score=b["anime"]["score"],
                status=b["anime"]["status"],
                url=b["anime"]["url"],
                image=Photo(**b["anime"]["image"]),
            ),
        )
        for b in calendar_list_json
    ]
