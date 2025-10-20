from enum import Enum


class GetIndexKorelogicStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
