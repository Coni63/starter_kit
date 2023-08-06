from __future__ import annotations

import re

from pydantic import BaseModel
from pydantic import field_validator


class Item(BaseModel):
    id: int | None = None
    title: str
    description: str

    @field_validator("description", "description")
    @staticmethod
    def is_valid_str(v):
        pattern = r"[^0-9A-Za-z\s_-]"
        validated_input = re.sub(pattern, "_", v)
        return validated_input
