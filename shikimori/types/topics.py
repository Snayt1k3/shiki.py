from shikimori.types.user import User
from shikimori.types.photo import Photo
from dataclasses import dataclass
from shikimori.utils.filter import handle_none_data


@dataclass
class Title:
    id: int
    name: str
    russian: str
    image: Photo
    url: str
    kind: str
    score: str
    status: str
    aired_on: str
    released_on: str
    episodes: int = 0
    episodes_aired: int = 0
    volumes: int = 0
    chapters: int = 0

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            episodes=data.get("episodes", 0),
            episodes_aired=data.get("episodes_aired", 0),
            volumes=data.get("volumes", 0),
            chapters=data.get("chapters", 0),
            id=data["id"],
            name=data["name"],
            russian=data["russian"],
            image=Photo.from_dict(data.get("image")),
            url=data["url"],
            kind=data["kind"],
            score=data["score"],
            status=data["status"],
            aired_on=data["aired_on"],
            released_on=data["released_on"],
        )


@dataclass
class Forum:
    id: int
    position: int
    name: str
    permalink: str
    url: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            position=data.get("position"),
            name=data.get("name"),
            permalink=data.get("permalink"),
            url=data.get("url"),
        )


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            russian=data.get("russian"),
            image=Photo.from_dict(data.get("image")),
            url=data.get("url"),
            kind=data.get("kind"),
            score=data.get("score"),
            status=data.get("status"),
            aired_on=data.get("aired_on"),
            released_on=data.get("released_on"),
            episodes=data.get("episodes"),
            episodes_aired=data.get("episodes_aired"),
            volumes=data.get("volumes"),
            chapters=data.get("chapters"),
        )


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            topic_title=data.get("topic_title"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            html_footer=data.get("html_footer"),
            created_at=data.get("created_at"),
            comments_count=data.get("comments_count"),
            forum=Forum.from_dict(data.get("forum")),
            user=User.from_dict(data.get("user")),
            type=data.get("type"),
            linked_id=data.get("linked_id"),
            linked_type=data.get("linked_type"),
            linked=Linked.from_dict(data.get("linked")) if data.get("linked") else None,
            viewed=data.get("viewed"),
            last_comment_viewed=data.get("last_comment_viewed"),
            event=data.get("event"),
            episode=data.get("episode"),
        )


@dataclass
class Status:
    id: int
    linked: Linked
    event: str
    episode: int
    created_at: str
    url: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            linked=Linked.from_dict(data.get("linked")),
            event=data.get("event"),
            episode=data.get("episode"),
            created_at=data.get("created_at"),
            url=data.get("url"),
        )


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

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            user=User.from_dict(data.get("user")),
            target=Title.from_dict(data.get("target")),
            votes_count=data.get("votes_count"),
            votes_for=data.get("votes_for"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            overall=data.get("overall"),
            storyline=data.get("storyline"),
            music=data.get("music"),
            characters=data.get("characters"),
            animation=data.get("animation"),
            created_at=data.get("created_at"),
        )


@dataclass
class TopicReview:
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
    linked: ReviewLinked | None

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            topic_title=data.get("topic_title"),
            body=data.get("body"),
            html_body=data.get("html_body"),
            html_footer=data.get("html_footer"),
            created_at=data.get("created_at"),
            comments_count=data.get("comments_count"),
            forum=Forum.from_dict(data.get("forum")),
            user=User.from_dict(data.get("user")),
            type=data.get("type"),
            linked_id=data.get("linked_id"),
            linked_type=data.get("linked_type"),
            linked=ReviewLinked.from_dict(data.get("linked")),
            viewed=data.get("viewed"),
            last_comment_viewed=data.get("last_comment_viewed"),
            event=data.get("event"),
            episode=data.get("episode"),
        )
