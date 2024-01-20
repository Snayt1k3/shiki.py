from pydantic import BaseModel

class ScreenShot(BaseModel):
    preview: str
    original: str
    