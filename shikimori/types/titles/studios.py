from pydantic import BaseModel

class Studio(BaseModel):
    id: int
    name: str
    filtered_name: str
    real: bool
    image: str