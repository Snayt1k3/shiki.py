from dataclasses import dataclass
from shikimori.constants import SHIKIMORI_URL
from shikimori.utils.filter import handle_none_data


@dataclass
class ScreenShot:
    preview: str
    original: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(preview=data.get("preview"), original=data.get("original"))

    @property
    def original_url(self) -> str:
        return f"{SHIKIMORI_URL}{self.original}"

    @property
    def preview_url(self) -> str:
        return f"{SHIKIMORI_URL}{self.preview}"
