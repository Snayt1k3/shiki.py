from pydantic import BaseModel


class BaseConstant(BaseModel):
    kind: list[str]
    status: list[str]


class MangaConstant(BaseConstant):
    pass


class AnimeConstant(BaseConstant):
    pass


class UserRateConstant(BaseModel):
    status: list[str]


class ClubConstant(BaseModel):
    join_policy: list[str]
    comment_policy: list[str]
    image_upload_policy: list[str]

class SmileConstant(BaseModel):
    bbcode: str
    path: str
