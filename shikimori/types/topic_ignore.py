from pydantic import BaseModel


class Topic(BaseModel):
    topic_id: str | None = None
    is_ignored: bool | None = None
