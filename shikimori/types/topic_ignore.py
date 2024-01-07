from pydantic import BaseModel


class Topic(BaseModel):
    topic_id: str
    is_ignored: bool
