from shikimori.types.user import User
from shikimori.types.photo import Photo
from dataclasses import dataclass


@dataclass
class Forum:
    id: int
    position: int
    name: str
    permalink: str
    url: str


@dataclass
class Linked:
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


@dataclass
class Topic:
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


@dataclass
class Status:
    id: int
    linked: Linked
    event: str
    episode: int
    created_at: str
    url: str
