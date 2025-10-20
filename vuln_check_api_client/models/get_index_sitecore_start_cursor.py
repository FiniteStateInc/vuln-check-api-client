from enum import Enum


class GetIndexSitecoreStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
