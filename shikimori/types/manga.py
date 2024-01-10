from pydantic import BaseModel
from .photo import Photo
class Manga(BaseModel):
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: int
    status: str
    volumes: int
    aired_on: str
    released_on: str | None
