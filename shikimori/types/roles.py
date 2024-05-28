from dataclasses import dataclass

from .character import CharacterBrief
from ..utils.filter import handle_none_data


@dataclass
class Role:
    roles: list[str]
    roles_russian: list[str]
    character: CharacterBrief
    person: CharacterBrief

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            roles=data.get("roles", []),
            roles_russian=data.get("roles_russian", []),
            character=(
                CharacterBrief.from_dict(character)
                if (character := data.get("character"))
                else None
            ),
            person=(
                CharacterBrief.from_dict(person)
                if (person := data.get("person"))
                else None
            ),
        )
