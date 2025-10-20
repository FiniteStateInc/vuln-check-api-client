from enum import Enum


class GetIndexCpeVulnerableStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
