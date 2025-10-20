from enum import Enum


class GetIndexCnvdFlawsStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
