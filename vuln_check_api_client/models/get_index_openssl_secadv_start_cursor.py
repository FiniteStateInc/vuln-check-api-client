from enum import Enum


class GetIndexOpensslSecadvStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
