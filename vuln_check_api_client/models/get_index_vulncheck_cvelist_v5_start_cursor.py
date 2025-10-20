from enum import Enum


class GetIndexVulncheckCvelistV5StartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
