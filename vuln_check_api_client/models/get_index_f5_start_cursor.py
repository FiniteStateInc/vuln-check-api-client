from enum import Enum


class GetIndexF5StartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
