from enum import Enum


class ResetInfoStatusFailed(str, Enum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
