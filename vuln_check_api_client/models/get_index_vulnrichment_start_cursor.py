from enum import Enum


class GetIndexVulnrichmentStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
