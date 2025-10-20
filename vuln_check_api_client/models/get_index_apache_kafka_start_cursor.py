from enum import Enum


class GetIndexApacheKafkaStartCursor(str, Enum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
