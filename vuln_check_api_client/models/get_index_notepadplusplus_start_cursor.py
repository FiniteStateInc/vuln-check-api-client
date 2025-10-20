from enum import Enum


class GetIndexNotepadplusplusStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
