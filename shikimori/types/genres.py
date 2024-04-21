from dataclasses import dataclass


@dataclass
class Genre:
    id: int
    name: str
    russian: str
    kind: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            kind=data.get("kind"),
        )
