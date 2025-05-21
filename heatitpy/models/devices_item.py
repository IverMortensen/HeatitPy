from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicesItem")


@_attrs_define
class DevicesItem:
    """
    Attributes:
        id (Union[Unset, str]): Unique id for each device Example: sdf87g4bnfc87a523rbsdf4.
        name (Union[Unset, str]): Device name used in the MyHeatit app. Example: BLE-Temp3 hall.
        device (Union[Unset, str]): What type of product the device is. Example: BLE-Temp3.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    device: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        device = self.device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if device is not UNSET:
            field_dict["device"] = device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        device = d.pop("device", UNSET)

        devices_item = cls(
            id=id,
            name=name,
            device=device,
        )

        devices_item.additional_properties = d
        return devices_item

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
