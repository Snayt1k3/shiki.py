from pydantic import BaseModel
from .animes import Photo

class Character(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str

class Role(BaseModel):
    roles: list[str]
    roles_russian: list[str]
    character: Character
