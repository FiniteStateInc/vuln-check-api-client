from enum import Enum


class GetIndexSierraWirelessStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
