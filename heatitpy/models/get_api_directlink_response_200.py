from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_directlink_response_200_master_thermostat_item import (
        GetApiDirectlinkResponse200MasterThermostatItem,
    )
    from ..models.get_api_directlink_response_200_relay_control_item import GetApiDirectlinkResponse200RelayControlItem


T = TypeVar("T", bound="GetApiDirectlinkResponse200")


@_attrs_define
class GetApiDirectlinkResponse200:
    """
    Attributes:
        relay_control (Union[Unset, list['GetApiDirectlinkResponse200RelayControlItem']]):
        master_thermostat (Union[Unset, list['GetApiDirectlinkResponse200MasterThermostatItem']]):
    """

    relay_control: Union[Unset, list["GetApiDirectlinkResponse200RelayControlItem"]] = UNSET
    master_thermostat: Union[Unset, list["GetApiDirectlinkResponse200MasterThermostatItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relay_control: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relay_control, Unset):
            relay_control = []
            for relay_control_item_data in self.relay_control:
                relay_control_item = relay_control_item_data.to_dict()
                relay_control.append(relay_control_item)

        master_thermostat: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.master_thermostat, Unset):
            master_thermostat = []
            for master_thermostat_item_data in self.master_thermostat:
                master_thermostat_item = master_thermostat_item_data.to_dict()
                master_thermostat.append(master_thermostat_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relay_control is not UNSET:
            field_dict["relayControl"] = relay_control
        if master_thermostat is not UNSET:
            field_dict["masterThermostat"] = master_thermostat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_directlink_response_200_master_thermostat_item import (
            GetApiDirectlinkResponse200MasterThermostatItem,
        )
        from ..models.get_api_directlink_response_200_relay_control_item import (
            GetApiDirectlinkResponse200RelayControlItem,
        )

        d = dict(src_dict)
        relay_control = []
        _relay_control = d.pop("relayControl", UNSET)
        for relay_control_item_data in _relay_control or []:
            relay_control_item = GetApiDirectlinkResponse200RelayControlItem.from_dict(relay_control_item_data)

            relay_control.append(relay_control_item)

        master_thermostat = []
        _master_thermostat = d.pop("masterThermostat", UNSET)
        for master_thermostat_item_data in _master_thermostat or []:
            master_thermostat_item = GetApiDirectlinkResponse200MasterThermostatItem.from_dict(
                master_thermostat_item_data
            )

            master_thermostat.append(master_thermostat_item)

        get_api_directlink_response_200 = cls(
            relay_control=relay_control,
            master_thermostat=master_thermostat,
        )

        get_api_directlink_response_200.additional_properties = d
        return get_api_directlink_response_200

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
