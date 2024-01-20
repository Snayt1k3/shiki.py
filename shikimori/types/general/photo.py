from pydantic import BaseModel


class Photo(BaseModel):
    original: str
    preview: str
    x96: str
    x48: str

class PhotoExtended(BaseModel):
    x160: str
    x148: str
    x80: str
    x64: str
    x48: str
    x32: str
    x16: str

class ClubImage(BaseModel):
    id: int
    original_url: str
    main_url: str
    preview_url: str
    can_destroy: bool
    user_id: int
