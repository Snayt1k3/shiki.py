from dataclasses import dataclass
from shikimori.types.photo import Photo
from shikimori.utils.filter import handle_none_data


@dataclass
class BaseTitle:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    aired_on: str
    released_on: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
        )


@dataclass
class BaseRole:
    role: str
    roles: list[str]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(role=data.get("role"), roles=data.get("roles", []))


@dataclass
class BaseCharacter:
    id: int
    name: str
    russian: str
    image: Photo
    url: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=int(data.get("id")),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
        )
