from enum import Enum


class GetIndexWolfsslStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
