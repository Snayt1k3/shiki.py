from dataclasses import dataclass
from ..general.photo import Photo


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


@dataclass
class BaseRole:
    role: str
    roles: list[str]


@dataclass
class BaseCharacter:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
