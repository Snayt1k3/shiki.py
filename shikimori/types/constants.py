from dataclasses import dataclass


@dataclass
class BaseConstant:
    kind: list[str]
    status: list[str]


@dataclass
class MangaConstant(BaseConstant):
    pass


@dataclass
class AnimeConstant(BaseConstant):
    pass


@dataclass
class UserRateConstant:
    status: list[str]


@dataclass
class ClubConstant:
    join_policy: list[str]
    comment_policy: list[str]
    image_upload_policy: list[str]


@dataclass
class SmileConstant:
    bbcode: str
    path: str
