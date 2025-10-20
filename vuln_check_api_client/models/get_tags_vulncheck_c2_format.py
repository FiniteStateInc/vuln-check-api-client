from enum import Enum


class GetTagsVulncheckC2Format(str, Enum):
    JSON = "json"
    TEXT = "text"
    TXT = "txt"

    def __str__(self) -> str:
        return str(self.value)
