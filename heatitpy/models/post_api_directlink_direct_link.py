from enum import Enum


class PostApiDirectlinkDirectLink(str, Enum):
    MASTERTHERMOSTAT = "masterThermostat"
    RELAYCONTROL = "relayControl"

    def __str__(self) -> str:
        return str(self.value)
