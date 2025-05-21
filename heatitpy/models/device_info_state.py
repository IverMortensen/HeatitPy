from enum import Enum


class DeviceInfoState(str, Enum):
    HEATING = "Heating"
    IDLE = "Idle"

    def __str__(self) -> str:
        return str(self.value)
