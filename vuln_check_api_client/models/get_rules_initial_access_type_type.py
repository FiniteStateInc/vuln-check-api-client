from enum import Enum


class GetRulesInitialAccessTypeType(str, Enum):
    SNORT = "snort"
    SURICATA = "suricata"

    def __str__(self) -> str:
        return str(self.value)
