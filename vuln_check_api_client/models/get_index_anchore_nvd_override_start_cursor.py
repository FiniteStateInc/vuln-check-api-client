from enum import Enum


class GetIndexAnchoreNvdOverrideStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
