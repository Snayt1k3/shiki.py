from dataclasses import dataclass

from shikimori.utils.filter import handle_none_data


@dataclass
class ScreenShot:
    preview: str
    original: str

    @classmethod
    @handle_none_data
    def from_dict(cls, data: dict):
        return cls(preview=data.get("preview"), original=data.get("original"))
