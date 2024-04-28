from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Video:
    id: int
    url: str
    image_url: str
    player_url: str
    name: str
    kind: str
    hosting: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            url=data.get("url"),
            image_url=data.get("image_url"),
            player_url=data.get("player_url"),
            name=data.get("name"),
            kind=data.get("kind"),
            hosting=data.get("hosting"),
        )
