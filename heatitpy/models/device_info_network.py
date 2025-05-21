from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceInfoNetwork")


@_attrs_define
class DeviceInfoNetwork:
    """
    Attributes:
        ssid (Union[Unset, str]): SSID of the connected wifi network Example: Home WiFi.
        mac (Union[Unset, str]): Mac address of the device Example: aa:bb:cc:11:22:33.
        ip_address (Union[Unset, str]): IP address of the device on the local network. Example: 192.168.1.10.
        wifi_signal_strength (Union[Unset, str]): Wifi signal strength Example: 65dBm.
        status (Union[Unset, str]): status of the connection. Example: ok.
    """

    ssid: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    wifi_signal_strength: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid = self.ssid

        mac = self.mac

        ip_address = self.ip_address

        wifi_signal_strength = self.wifi_signal_strength

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid is not UNSET:
            field_dict["SSID"] = ssid
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if wifi_signal_strength is not UNSET:
            field_dict["wifiSignalStrength"] = wifi_signal_strength
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssid = d.pop("SSID", UNSET)

        mac = d.pop("mac", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        wifi_signal_strength = d.pop("wifiSignalStrength", UNSET)

        status = d.pop("status", UNSET)

        device_info_network = cls(
            ssid=ssid,
            mac=mac,
            ip_address=ip_address,
            wifi_signal_strength=wifi_signal_strength,
            status=status,
        )

        device_info_network.additional_properties = d
        return device_info_network

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
