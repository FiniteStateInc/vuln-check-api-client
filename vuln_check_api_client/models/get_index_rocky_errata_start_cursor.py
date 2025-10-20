from enum import Enum


class GetIndexRockyErrataStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
