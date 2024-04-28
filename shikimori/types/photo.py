from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class Photo:
    original: str
    preview: str
    x96: str
    x48: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            original=data.get("original"),
            preview=data.get("preview"),
            x96=data.get("x96"),
            x48=data.get("x48"),
        )


@dataclass
class PhotoExtended:
    x160: str
    x148: str
    x80: str
    x64: str
    x48: str
    x32: str
    x16: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            x160=data.get("x160"),
            x148=data.get("x148"),
            x80=data.get("x80"),
            x64=data.get("x64"),
            x48=data.get("x48"),
            x32=data.get("x32"),
            x16=data.get("x16"),
        )


@dataclass
class ClubImage:
    id: int
    original_url: str
    main_url: str
    preview_url: str
    can_destroy: bool
    user_id: int

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            original_url=data.get("original_url"),
            main_url=data.get("main_url"),
            preview_url=data.get("preview_url"),
            can_destroy=data.get("can_destroy"),
            user_id=data.get("user_id"),
        )


@dataclass
class UserImage:
    id: int
    preview: str
    url: str
    bbcode: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            preview=data.get("preview"),
            url=data.get("url"),
            bbcode=data.get("bbcode"),
        )


@dataclass
class Logo:
    original: str
    main: str
    x96: str
    x73: str
    x48: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(
            original=data.get("original"),
            main=data.get("main"),
            x96=data.get("x96"),
            x73=data.get("x73"),
            x48=data.get("x48"),
        )
