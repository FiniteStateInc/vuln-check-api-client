from enum import Enum


class GetIndexWhatsappStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
