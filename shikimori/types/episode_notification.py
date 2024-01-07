from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime


class EpisodeNotification(BaseModel):
    aired_at: datetime | str
    anime_id: int
    episode: int
    is_anime365: bool
    is_fandub: bool
    is_raw: bool
    is_subtitles: bool

    def to_dict(self):
        return {
            "aired_at": self.aired_at,
            "anime_id": self.anime_id,
            "episode": self.episode,
            "is_anime365": self.is_anime365,
            "is_fandub": self.is_fandub,
            "is_raw": self.is_raw,
            "is_subtitles": self.is_subtitles,
        }

    @classmethod
    @field_validator("aired_at")
    def validate_date(cls, v: str | datetime) -> str:
        if isinstance(v, str):
            date = datetime.strptime(v, "YYYY-MM-DDTHH:MM:SS+HH:MM")
            return date.strftime("YYYY-MM-DDTHH:MM:SS+HH:MM")

        elif isinstance(v, datetime):
            return v.strftime("YYYY-MM-DDTHH:MM:SS+HH:MM")

        else:
            raise ValidationError


class EpisodeNotificationResponse(BaseModel):
    id: int
    anime_id: int
    episode: int
    is_raw: bool
    is_subtitles: bool
    is_fandub: bool
    is_anime365: bool
    topic_id: bool
