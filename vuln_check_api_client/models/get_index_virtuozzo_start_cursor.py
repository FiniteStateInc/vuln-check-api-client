from enum import Enum


class GetIndexVirtuozzoStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
