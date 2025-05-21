from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInfoParametersOWD")


@_attrs_define
class DeviceInfoParametersOWD:
    """
    Attributes:
        open_window_detection (Union[Unset, bool]): Shows if the Open Window Detection feature is enabled or disabled.
            <br>**false** = disabled <br>**true** = enabled
        active_now (Union[Unset, bool]): Shows the current state of the Open Window Detection. false = No open window
            detected. true = Open window detected. Setpoint is lowered. Default: False.
        active_time (Union[Unset, int]): Seconds left until the Open Window Detection done. Default: 0. Example: 3245.
    """

    open_window_detection: Union[Unset, bool] = UNSET
    active_now: Union[Unset, bool] = False
    active_time: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_window_detection = self.open_window_detection

        active_now = self.active_now

        active_time = self.active_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_window_detection is not UNSET:
            field_dict["openWindowDetection"] = open_window_detection
        if active_now is not UNSET:
            field_dict["activeNow"] = active_now
        if active_time is not UNSET:
            field_dict["activeTime"] = active_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_window_detection = d.pop("openWindowDetection", UNSET)

        active_now = d.pop("activeNow", UNSET)

        active_time = d.pop("activeTime", UNSET)

        device_info_parameters_owd = cls(
            open_window_detection=open_window_detection,
            active_now=active_now,
            active_time=active_time,
        )

        device_info_parameters_owd.additional_properties = d
        return device_info_parameters_owd

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
