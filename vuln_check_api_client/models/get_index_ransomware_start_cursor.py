from enum import Enum


class GetIndexRansomwareStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
