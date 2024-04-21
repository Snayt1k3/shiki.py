from dataclasses import dataclass


@dataclass
class BaseConstant:
    kind: list[str]
    status: list[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(kind=data.get("kind", []), status=data.get("status", []))


@dataclass
class MangaConstant(BaseConstant):
    pass


@dataclass
class AnimeConstant(BaseConstant):
    pass


@dataclass
class UserRateConstant:
    status: list[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(status=data.get("status", []))


@dataclass
class ClubConstant:
    join_policy: list[str]
    comment_policy: list[str]
    image_upload_policy: list[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            join_policy=data.get("join_policy", []),
            comment_policy=data.get("comment_policy", []),
            image_upload_policy=data.get("image_upload_policy", []),
        )


@dataclass
class SmileConstant:
    bbcode: str
    path: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(bbcode=data.get("bbcode"), path=data.get("path"))
