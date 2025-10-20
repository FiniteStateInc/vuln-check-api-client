from enum import Enum


class GetIndexVulncheckNvd2StartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
