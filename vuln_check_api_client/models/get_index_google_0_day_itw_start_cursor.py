from enum import Enum


class GetIndexGoogle0DayItwStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
