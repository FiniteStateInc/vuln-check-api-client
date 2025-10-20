from enum import Enum


class GetIndexJetbrainsStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
