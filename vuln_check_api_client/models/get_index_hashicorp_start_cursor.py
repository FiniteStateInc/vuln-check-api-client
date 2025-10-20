from enum import Enum


class GetIndexHashicorpStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
