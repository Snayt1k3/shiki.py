from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Studio:
    id: int
    name: str
    filtered_name: str
    real: bool
    image: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            filtered_name=data.get("filtered_name"),
            real=data.get("real"),
            image=data.get("image"),
        )
