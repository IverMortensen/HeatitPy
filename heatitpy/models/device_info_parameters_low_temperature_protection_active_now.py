from enum import Enum


class DeviceInfoParametersLowTemperatureProtectionActiveNow(str, Enum):
    DISABLED = "disabled"
    HEATING = "Heating"
    IDLE = "Idle"

    def __str__(self) -> str:
        return str(self.value)
