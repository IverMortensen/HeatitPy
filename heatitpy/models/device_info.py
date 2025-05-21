from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_info_state import DeviceInfoState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_info_network import DeviceInfoNetwork
    from ..models.device_info_parameters import DeviceInfoParameters


T = TypeVar("T", bound="DeviceInfo")


@_attrs_define
class DeviceInfo:
    """
    Attributes:
        id (Union[Unset, str]): Unique id for each device Example: sdf87g4bnfc87a523rbsdf4.
        name (Union[Unset, str]): Device name used in the MyHeatit app. Example: Panel hall.
        room (Union[Unset, str]): The room the device is assigned to in the MyHeatit app. Example: hall.
        state (Union[Unset, DeviceInfoState]): The current state for heating. Is the heating element currently on?
            Example: Idle.
        current_power (Union[Unset, int]): Power consumption in W Example: 1500.
        total_consumption (Union[Unset, float]): Total consumption in kWh Example: 624.25.
        room_temperature (Union[Unset, float]): Current temperature measurement Example: 22.2.
        parameters (Union[Unset, DeviceInfoParameters]):
        network (Union[Unset, DeviceInfoNetwork]):
        firmware (Union[Unset, str]):  Example: 1.2.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    room: Union[Unset, str] = UNSET
    state: Union[Unset, DeviceInfoState] = UNSET
    current_power: Union[Unset, int] = UNSET
    total_consumption: Union[Unset, float] = UNSET
    room_temperature: Union[Unset, float] = UNSET
    parameters: Union[Unset, "DeviceInfoParameters"] = UNSET
    network: Union[Unset, "DeviceInfoNetwork"] = UNSET
    firmware: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        room = self.room

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        current_power = self.current_power

        total_consumption = self.total_consumption

        room_temperature = self.room_temperature

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        firmware = self.firmware

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if room is not UNSET:
            field_dict["room"] = room
        if state is not UNSET:
            field_dict["state"] = state
        if current_power is not UNSET:
            field_dict["currentPower"] = current_power
        if total_consumption is not UNSET:
            field_dict["totalConsumption"] = total_consumption
        if room_temperature is not UNSET:
            field_dict["roomTemperature"] = room_temperature
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if network is not UNSET:
            field_dict["Network"] = network
        if firmware is not UNSET:
            field_dict["firmware"] = firmware

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_info_network import DeviceInfoNetwork
        from ..models.device_info_parameters import DeviceInfoParameters

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        room = d.pop("room", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DeviceInfoState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DeviceInfoState(_state)

        current_power = d.pop("currentPower", UNSET)

        total_consumption = d.pop("totalConsumption", UNSET)

        room_temperature = d.pop("roomTemperature", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, DeviceInfoParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = DeviceInfoParameters.from_dict(_parameters)

        _network = d.pop("Network", UNSET)
        network: Union[Unset, DeviceInfoNetwork]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = DeviceInfoNetwork.from_dict(_network)

        firmware = d.pop("firmware", UNSET)

        device_info = cls(
            id=id,
            name=name,
            room=room,
            state=state,
            current_power=current_power,
            total_consumption=total_consumption,
            room_temperature=room_temperature,
            parameters=parameters,
            network=network,
            firmware=firmware,
        )

        device_info.additional_properties = d
        return device_info

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
