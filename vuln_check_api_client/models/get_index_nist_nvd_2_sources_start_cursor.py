from enum import Enum


class GetIndexNistNvd2SourcesStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
