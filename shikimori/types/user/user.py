from dataclasses import dataclass
from ..general.photo import PhotoExtended


@dataclass
class User:
    id: int
    nickname: str
    image: PhotoExtended
    avatar: str
    last_online_at: str
    url: str

