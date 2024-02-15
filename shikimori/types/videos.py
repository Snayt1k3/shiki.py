from dataclasses import dataclass


@dataclass
class Video:
    id: int
    url: str
    image_url: str
    player_url: str
    name: str
    kind: str
    hosting: str
