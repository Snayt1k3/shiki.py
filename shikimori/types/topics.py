from shikimori.types.user import User
from shikimori.types.photo import Photo
from dataclasses import dataclass
from shikimori.types.base import BaseTitle


@dataclass
class Title(BaseTitle):
    episodes: int = None
    episodes_aired: int = None
    volumes: int = None
    chapters: int = None


@dataclass
class Forum:
    id: int
    position: int
    name: str
    permalink: str
    url: str


@dataclass
class Linked:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    aired_on: str | None
    released_on: str | None
    episodes: int = None
    episodes_aired: int = None
    volumes: int = None
    chapters: int = None


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
    linked: Linked | None
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


@dataclass
class ReviewLinked:
    id: int
    user: User
    target: Title
    votes_count: int
    votes_for: int
    body: str
    html_body: str
    overall: int
    storyline: int
    music: int
    characters: int
    animation: int
    created_at: str
