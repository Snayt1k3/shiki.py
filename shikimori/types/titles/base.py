from pydantic import BaseModel
from ..general.photo import Photo


class BaseTitle(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    episodes: int
    episodes_aired: int
    aired_on: str
    released_on: str


class BaseRole(BaseModel):
    role: str
    roles: list[str]


class BaseCharacter(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
