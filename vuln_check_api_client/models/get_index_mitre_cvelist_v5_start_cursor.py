from enum import Enum


class GetIndexMitreCvelistV5StartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
