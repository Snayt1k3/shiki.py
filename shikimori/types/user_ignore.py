from pydantic import BaseModel


class UserIgnore(BaseModel):
    user_id: str | None = None
    is_ignored: bool | None = None
