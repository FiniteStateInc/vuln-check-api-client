from enum import Enum


class GetIndexGoogleContainerOptimizedOsStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
