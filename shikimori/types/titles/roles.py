from dataclasses import dataclass
from .base import BaseCharacter

@dataclass
class Character(BaseCharacter):
    pass

@dataclass
class Role:
    roles: list[str]
    roles_russian: list[str]
    character: Character
