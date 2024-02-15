from dataclasses import dataclass


@dataclass
class UserRateResponse:
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
