from pydantic import BaseModel
from .photo import Photo


class Ranobe(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    episodes: int
    episodes_aired: int
    aired_on: str
    released_on: str
