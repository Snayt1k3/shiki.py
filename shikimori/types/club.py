from shikimori.types.manga import Manga
from shikimori.types.animes import Anime
from shikimori.types.character import CharacterBrief
from shikimori.types.user import User
from .photo import ClubImage, Logo
from .topics import Topic
from dataclasses import dataclass

from ..utils.filter import handle_none_data


@dataclass
class Club:
    id: int
    name: str
    logo: Logo
    is_censored: bool
    join_policy: str
    comment_policy: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            logo=Logo.from_dict(data.get("logo")),
            is_censored=data.get("is_censored"),
            join_policy=data.get("join_policy"),
            comment_policy=data.get("comment_policy"),
        )


@dataclass
class ClubInfo(Club):
    description: str
    description_html: str
    mangas: list[Manga]
    characters: list[CharacterBrief]
    thread_id: int
    topic_id: int
    user_role: str
    style_id: int
    members: list[User]
    animes: list[Anime]
    images: list[ClubImage]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            description=data.get("description"),
            description_html=data.get("description_html"),
            mangas=[
                Manga.from_dict(manga_data) for manga_data in data.get("mangas", [])
            ],
            characters=[
                CharacterBrief.from_dict(character_data)
                for character_data in data.get("characters", [])
            ],
            thread_id=data.get("thread_id"),
            topic_id=data.get("topic_id"),
            user_role=data.get("user_role"),
            style_id=data.get("style_id"),
            members=[
                User.from_dict(member_data) for member_data in data.get("members", [])
            ],
            animes=[
                Anime.from_dict(anime_data) for anime_data in data.get("animes", [])
            ],
            images=[
                ClubImage.from_dict(image_data) for image_data in data.get("images", [])
            ],
            id=data.get("id"),
            name=data.get("name"),
            logo=Logo.from_dict(data.get("logo")),
            is_censored=data.get("is_censored"),
            join_policy=data.get("join_policy"),
            comment_policy=data.get("comment_policy"),
        )


@dataclass
class Collection(Topic):
    pass
