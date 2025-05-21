from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_info_parameters_low_temperature_protection_active_now import (
    DeviceInfoParametersLowTemperatureProtectionActiveNow,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInfoParametersLowTemperatureProtection")


@_attrs_define
class DeviceInfoParametersLowTemperatureProtection:
    """
    Attributes:
        low_temperature_protection (Union[Unset, int]): Will turn on heating if the temperature drops below the value
            set in the parameter <br>**0** = disabled (Default) <br>**1-10** = Turn on when temperature is below value in °C
        active_now (Union[Unset, DeviceInfoParametersLowTemperatureProtectionActiveNow]): Shows the current state of the
            Low Temperature Protection. <br>**disabled** = Feature is disabled <br>**Idle** = Feature is enabled but not
            active <br>**Heating** = Feature is active and heating Default:
            DeviceInfoParametersLowTemperatureProtectionActiveNow.DISABLED. Example: Idle.
    """

    low_temperature_protection: Union[Unset, int] = UNSET
    active_now: Union[Unset, DeviceInfoParametersLowTemperatureProtectionActiveNow] = (
        DeviceInfoParametersLowTemperatureProtectionActiveNow.DISABLED
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low_temperature_protection = self.low_temperature_protection

        active_now: Union[Unset, str] = UNSET
        if not isinstance(self.active_now, Unset):
            active_now = self.active_now.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if low_temperature_protection is not UNSET:
            field_dict["lowTemperatureProtection"] = low_temperature_protection
        if active_now is not UNSET:
            field_dict["activeNow"] = active_now

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low_temperature_protection = d.pop("lowTemperatureProtection", UNSET)

        _active_now = d.pop("activeNow", UNSET)
        active_now: Union[Unset, DeviceInfoParametersLowTemperatureProtectionActiveNow]
        if isinstance(_active_now, Unset):
            active_now = UNSET
        else:
            active_now = DeviceInfoParametersLowTemperatureProtectionActiveNow(_active_now)

        device_info_parameters_low_temperature_protection = cls(
            low_temperature_protection=low_temperature_protection,
            active_now=active_now,
        )

        device_info_parameters_low_temperature_protection.additional_properties = d
        return device_info_parameters_low_temperature_protection

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
