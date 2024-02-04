from dataclasses import dataclass


@dataclass
class Photo:
    original: str
    preview: str
    x96: str
    x48: str


@dataclass
class PhotoExtended:
    x160: str
    x148: str
    x80: str
    x64: str
    x48: str
    x32: str
    x16: str


@dataclass
class ClubImage:
    id: int
    original_url: str
    main_url: str
    preview_url: str
    can_destroy: bool
    user_id: int

@dataclass
class UserImage:
    id: int
    preview: str
    url: str
    bbcode: str
