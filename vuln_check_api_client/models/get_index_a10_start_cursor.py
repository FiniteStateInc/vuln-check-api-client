from enum import Enum


class GetIndexA10StartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
