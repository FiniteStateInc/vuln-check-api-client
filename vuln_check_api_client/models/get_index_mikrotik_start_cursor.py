from enum import Enum


class GetIndexMikrotikStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
