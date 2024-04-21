from dataclasses import dataclass


@dataclass
class Publisher:
    id: int
    name: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data.get("id"), name=data.get("name"))
