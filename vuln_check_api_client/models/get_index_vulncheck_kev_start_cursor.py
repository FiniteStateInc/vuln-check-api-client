from enum import Enum


class GetIndexVulncheckKevStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
