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
    person: Character

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            roles=data.get("roles", []),
            roles_russian=data.get("roles_russian", []),
            character=Character.from_dict(character) if (character := data.get("character")) else None,
            person=Character.from_dict(person) if (person := data.get("person")) else None,
        )
