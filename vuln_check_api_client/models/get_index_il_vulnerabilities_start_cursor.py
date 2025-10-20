from enum import Enum


class GetIndexIlVulnerabilitiesStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
