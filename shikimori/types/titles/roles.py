from pydantic import BaseModel
from .base import BaseCharacter


class Character(BaseCharacter):
    pass


class Role(BaseModel):
    roles: list[str]
    roles_russian: list[str]
    character: Character
