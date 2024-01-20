from pydantic import BaseModel


class UserIgnore(BaseModel):
    user_id: str
    is_ignored: bool
