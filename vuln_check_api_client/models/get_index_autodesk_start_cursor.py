from enum import Enum


class GetIndexAutodeskStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
