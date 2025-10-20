from enum import Enum


class GetIndexHoneywellStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
