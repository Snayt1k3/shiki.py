from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Genre:
    id: int
    name: str
    russian: str
    kind: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            kind=data.get("kind"),
        )
