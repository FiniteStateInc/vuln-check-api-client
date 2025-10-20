from enum import Enum


class GetIndexCompassSecurityStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
