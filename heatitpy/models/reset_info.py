from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reset_info_status_failed import ResetInfoStatusFailed
from ..models.reset_info_status_success import ResetInfoStatusSuccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetInfo")


@_attrs_define
class ResetInfo:
    """
    Attributes:
        status_success (Union[Unset, ResetInfoStatusSuccess]):  Example: success.
        status_failed (Union[Unset, ResetInfoStatusFailed]):  Example: failed.
    """

    status_success: Union[Unset, ResetInfoStatusSuccess] = UNSET
    status_failed: Union[Unset, ResetInfoStatusFailed] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_success: Union[Unset, str] = UNSET
        if not isinstance(self.status_success, Unset):
            status_success = self.status_success.value

        status_failed: Union[Unset, str] = UNSET
        if not isinstance(self.status_failed, Unset):
            status_failed = self.status_failed.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_success is not UNSET:
            field_dict["statusSuccess"] = status_success
        if status_failed is not UNSET:
            field_dict["statusFailed"] = status_failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status_success = d.pop("statusSuccess", UNSET)
        status_success: Union[Unset, ResetInfoStatusSuccess]
        if isinstance(_status_success, Unset):
            status_success = UNSET
        else:
            status_success = ResetInfoStatusSuccess(_status_success)

        _status_failed = d.pop("statusFailed", UNSET)
        status_failed: Union[Unset, ResetInfoStatusFailed]
        if isinstance(_status_failed, Unset):
            status_failed = UNSET
        else:
            status_failed = ResetInfoStatusFailed(_status_failed)

        reset_info = cls(
            status_success=status_success,
            status_failed=status_failed,
        )

        reset_info.additional_properties = d
        return reset_info

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
