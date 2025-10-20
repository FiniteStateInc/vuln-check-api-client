from enum import Enum


class GetPdnsVulncheckC2Format(str, Enum):
    JSON = "json"
    TEXT = "text"
    TXT = "txt"

    def __str__(self) -> str:
        return str(self.value)
