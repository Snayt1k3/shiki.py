from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Publisher:
    id: int
    name: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(id=data.get("id"), name=data.get("name"))
