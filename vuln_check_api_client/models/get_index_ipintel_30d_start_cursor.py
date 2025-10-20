from enum import Enum


class GetIndexIpintel30DStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
