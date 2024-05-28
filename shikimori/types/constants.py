from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class MangaConstant:
    kind: list[str]
    status: list[str]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(kind=data.get("kind", []), status=data.get("status", []))


@dataclass
class AnimeConstant:
    kind: list[str]
    status: list[str]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(kind=data.get("kind", []), status=data.get("status", []))


@dataclass
class UserRateConstant:
    status: list[str]

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(status=data.get("status", []))


@dataclass
class ClubConstant:
    join_policy: list[str]
    comment_policy: list[str]
    image_upload_policy: list[str]

    @classmethod
    @handle_none_data
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
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(bbcode=data.get("bbcode"), path=data.get("path"))
