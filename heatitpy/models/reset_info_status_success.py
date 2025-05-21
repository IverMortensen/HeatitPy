from enum import Enum


class ResetInfoStatusSuccess(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
