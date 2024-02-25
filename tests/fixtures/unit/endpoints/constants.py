import pytest

from shikimori.endpoints.constants import ConstantsEndpoint
from shikimori.types.constants import (
    SmileConstant,
    ClubConstant,
    AnimeConstant,
    MangaConstant,
    UserRateConstant,
)


@pytest.fixture
def const_client():
    return ConstantsEndpoint("", "", "")


@pytest.fixture
def const_animes_json():
    return {
        "kind": ["tv", "movie", "ova", "ona", "special", "music"],
        "status": ["anons", "ongoing", "released"],
    }


@pytest.fixture
def const_animes_resp(const_animes_json):
    return AnimeConstant(**const_animes_json)


@pytest.fixture
def const_mangas_json():
    return {
        "kind": [
            "manga",
            "manhwa",
            "manhua",
            "light_novel",
            "novel",
            "one_shot",
            "doujin",
        ],
        "status": ["anons", "ongoing", "released", "paused", "discontinued"],
    }


@pytest.fixture
def const_mangas_resp(const_mangas_json):
    return MangaConstant(**const_mangas_json)


@pytest.fixture
def const_user_rate_json():
    return {
        "status": [
            "planned",
            "watching",
            "rewatching",
            "completed",
            "on_hold",
            "dropped",
        ]
    }


@pytest.fixture
def const_user_rate_resp(const_user_rate_json):
    return UserRateConstant(**const_user_rate_json)


@pytest.fixture
def const_club_json():
    return {
        "join_policy": ["free", "member_invite", "admin_invite", "owner_invite"],
        "comment_policy": ["free", "members", "admins"],
        "image_upload_policy": ["members", "admins"],
    }


@pytest.fixture
def const_club_resp(const_club_json):
    return ClubConstant(**const_club_json)


@pytest.fixture
def const_smile_json():
    return [
        {"bbcode": ":)", "path": "/images/smileys/:).gif"},
        {"bbcode": ":D", "path": "/images/smileys/:D.gif"},
    ]

@pytest.fixture
def const_smile_resp(const_smile_json):
    return [SmileConstant(**s) for s in const_smile_json]