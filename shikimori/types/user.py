from pydantic import BaseModel
from photo import PhotoExtended

class User(BaseModel):
    id: int
    nickname: str
    image: PhotoExtended
    avatar: str
    last_online_at: str
    url: str
