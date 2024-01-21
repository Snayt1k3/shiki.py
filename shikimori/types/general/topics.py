from pydantic import BaseModel
from ..user.user import User
from ..general.photo import Photo

class Forum(BaseModel):
    id: int
    position: int
    name: str
    permalink: str
    url: str

class Linked(BaseModel):
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    episodes: int
    episodes_aired: int
    aired_on: str | None
    released_at: str | None

class Topic(BaseModel):
    id: int
    topic_title: str
    body: str
    html_body: str
    html_footer: str
    created_at: str
    comments_count: int
    forum: Forum
    user: User
    type: str
    linked_id: int
    linked_type: str
    linked: Linked
    viewed: bool
    last_comment_viewed: bool
    event: str
    episode: int


