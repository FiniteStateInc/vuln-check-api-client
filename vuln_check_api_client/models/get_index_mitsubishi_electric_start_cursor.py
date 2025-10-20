from enum import Enum


class GetIndexMitsubishiElectricStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
