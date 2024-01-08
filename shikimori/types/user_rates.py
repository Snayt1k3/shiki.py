from pydantic import BaseModel


class UserRateResponse(BaseModel):
    id: int
    user_id: int
    target_id: int
    target_type: str
    score: int
    status: str
    rewatches: int
    episodes: int
    volumes: int
    chapters: int
    text: str
    text_html: str
    created_at: str
    updated_at: str


class UserRateCreate(BaseModel):
    user_id: int
    target_id: int
    target_type: str
    status: str | None = None
    score: int | None = None
    chapters: int | None = None
    episodes: int | None = None
    volumes: int | None = None
    rewatches: int | None = None
    text: str | None = None

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "target_id": self.target_id,
            "target_type": self.target_type,
            "status": self.status,
            "score": self.score,
            "chapters": self.chapters,
            "episodes": self.episodes,
            "volumes": self.volumes,
            "rewatches": self.rewatches,
            "text": self.text,
        }


class UserRateUpdate(BaseModel):
    status: str | None = None
    score: int | None = None
    chapters: int | None = None
    episodes: int | None = None
    volumes: int | None = None
    rewatches: int | None = None
    text: str | None = None

    def to_dict(self):
        return {
            "score": self.score,
            "chapters": self.chapters,
            "episodes": self.episodes,
            "volumes": self.volumes,
            "rewatches": self.rewatches,
            "text": self.text,
        }

