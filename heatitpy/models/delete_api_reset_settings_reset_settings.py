from enum import Enum


class DeleteApiResetSettingsResetSettings(str, Enum):
    RESET = "Reset"

    def __str__(self) -> str:
        return str(self.value)
