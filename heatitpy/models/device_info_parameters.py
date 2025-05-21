from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.disable_buttons import DisableButtons
from ..models.panel_mode import PanelMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_info_parameters_low_temperature_protection import DeviceInfoParametersLowTemperatureProtection
    from ..models.device_info_parameters_owd import DeviceInfoParametersOWD


T = TypeVar("T", bound="DeviceInfoParameters")


@_attrs_define
class DeviceInfoParameters:
    """
    Attributes:
        panel_mode (Union[Unset, PanelMode]): Chooses the mode of the panel <br>**0** = Off <br>**1** = Heating
            <br>**2** = Eco
        sensor_calibration (Union[Unset, float]): Calibrate the sensor <br>**-6.0** = -6.0° (minimum) <br>**6.0** = 6.0°
            (maximum)
        temperature_display (Union[Unset, bool]): Choose what temperature to show in the display in standby mode.
            <br>**false** = Display setpoint temperature <br>**true** = Display measured temperature
        sensor_mode (Union[Unset, bool]): Choose which sensor mode the device should operate with <br>**false** =
            Internal sensor (Default) <br>**true** = External wireless sensor
        external_sensor_fallback (Union[Unset, bool]): Choose what happens if the external sensor stops reporting.
            <br>**false** = Off <br>**true** = internal sensor (Default)
        active_display_brightness (Union[Unset, int]): Set display brightness for active state <br>**1** = 10%
            <br>**10** = 100%
        standby_display_brightness (Union[Unset, int]): Set display brightness for standby state <br>**0** = 0%
            <br>**10** = 100%
        heating_setpoint (Union[Unset, float]): Desired heating temperature <br>**5.0** = 5.0° <br>**40.0** = 40.0°
        eco_setpoint (Union[Unset, float]): Desired ECO temperature <br>**5.0** = 5.0° <br>**40.0** = 40.0°
        minimum_temperature_limit (Union[Unset, float]): Set lowest temperature <br>**5.0** = 5.0° <br>**40.0** = 40.0°
        maximum_temperature_limit (Union[Unset, float]): Set highest temperature <br>**5.0** = 5.0° <br>**40.0** = 40.0°
        low_temperature_protection (Union[Unset, DeviceInfoParametersLowTemperatureProtection]):
        owd (Union[Unset, DeviceInfoParametersOWD]):
        load_limit (Union[Unset, int]): The power the Panel should operate at. **1**=100W, **2**=200W, etc.
        max_load (Union[Unset, int]): Maximum load the device can handle. Varies on the model of the device. Default:
            15.
        disable_buttons (Union[Unset, DisableButtons]): Disable device buttons <br>**0** = Buttons are not disabled
            <br>**1** = Buttons are disabled <br>**2** = lock menu
    """

    panel_mode: Union[Unset, PanelMode] = UNSET
    sensor_calibration: Union[Unset, float] = UNSET
    temperature_display: Union[Unset, bool] = UNSET
    sensor_mode: Union[Unset, bool] = UNSET
    external_sensor_fallback: Union[Unset, bool] = UNSET
    active_display_brightness: Union[Unset, int] = UNSET
    standby_display_brightness: Union[Unset, int] = UNSET
    heating_setpoint: Union[Unset, float] = UNSET
    eco_setpoint: Union[Unset, float] = UNSET
    minimum_temperature_limit: Union[Unset, float] = UNSET
    maximum_temperature_limit: Union[Unset, float] = UNSET
    low_temperature_protection: Union[Unset, "DeviceInfoParametersLowTemperatureProtection"] = UNSET
    owd: Union[Unset, "DeviceInfoParametersOWD"] = UNSET
    load_limit: Union[Unset, int] = UNSET
    max_load: Union[Unset, int] = 15
    disable_buttons: Union[Unset, DisableButtons] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        panel_mode: Union[Unset, int] = UNSET
        if not isinstance(self.panel_mode, Unset):
            panel_mode = self.panel_mode.value

        sensor_calibration = self.sensor_calibration

        temperature_display = self.temperature_display

        sensor_mode = self.sensor_mode

        external_sensor_fallback = self.external_sensor_fallback

        active_display_brightness = self.active_display_brightness

        standby_display_brightness = self.standby_display_brightness

        heating_setpoint = self.heating_setpoint

        eco_setpoint = self.eco_setpoint

        minimum_temperature_limit = self.minimum_temperature_limit

        maximum_temperature_limit = self.maximum_temperature_limit

        low_temperature_protection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.low_temperature_protection, Unset):
            low_temperature_protection = self.low_temperature_protection.to_dict()

        owd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.owd, Unset):
            owd = self.owd.to_dict()

        load_limit = self.load_limit

        max_load = self.max_load

        disable_buttons: Union[Unset, int] = UNSET
        if not isinstance(self.disable_buttons, Unset):
            disable_buttons = self.disable_buttons.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if panel_mode is not UNSET:
            field_dict["panelMode"] = panel_mode
        if sensor_calibration is not UNSET:
            field_dict["sensorCalibration"] = sensor_calibration
        if temperature_display is not UNSET:
            field_dict["temperatureDisplay"] = temperature_display
        if sensor_mode is not UNSET:
            field_dict["sensorMode"] = sensor_mode
        if external_sensor_fallback is not UNSET:
            field_dict["externalSensorFallback"] = external_sensor_fallback
        if active_display_brightness is not UNSET:
            field_dict["activeDisplayBrightness"] = active_display_brightness
        if standby_display_brightness is not UNSET:
            field_dict["standbyDisplayBrightness"] = standby_display_brightness
        if heating_setpoint is not UNSET:
            field_dict["heatingSetpoint"] = heating_setpoint
        if eco_setpoint is not UNSET:
            field_dict["ecoSetpoint"] = eco_setpoint
        if minimum_temperature_limit is not UNSET:
            field_dict["minimumTemperatureLimit"] = minimum_temperature_limit
        if maximum_temperature_limit is not UNSET:
            field_dict["maximumTemperatureLimit"] = maximum_temperature_limit
        if low_temperature_protection is not UNSET:
            field_dict["lowTemperatureProtection"] = low_temperature_protection
        if owd is not UNSET:
            field_dict["OWD"] = owd
        if load_limit is not UNSET:
            field_dict["loadLimit"] = load_limit
        if max_load is not UNSET:
            field_dict["maxLoad"] = max_load
        if disable_buttons is not UNSET:
            field_dict["disableButtons"] = disable_buttons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_info_parameters_low_temperature_protection import (
            DeviceInfoParametersLowTemperatureProtection,
        )
        from ..models.device_info_parameters_owd import DeviceInfoParametersOWD

        d = dict(src_dict)
        _panel_mode = d.pop("panelMode", UNSET)
        panel_mode: Union[Unset, PanelMode]
        if isinstance(_panel_mode, Unset):
            panel_mode = UNSET
        else:
            panel_mode = PanelMode(_panel_mode)

        sensor_calibration = d.pop("sensorCalibration", UNSET)

        temperature_display = d.pop("temperatureDisplay", UNSET)

        sensor_mode = d.pop("sensorMode", UNSET)

        external_sensor_fallback = d.pop("externalSensorFallback", UNSET)

        active_display_brightness = d.pop("activeDisplayBrightness", UNSET)

        standby_display_brightness = d.pop("standbyDisplayBrightness", UNSET)

        heating_setpoint = d.pop("heatingSetpoint", UNSET)

        eco_setpoint = d.pop("ecoSetpoint", UNSET)

        minimum_temperature_limit = d.pop("minimumTemperatureLimit", UNSET)

        maximum_temperature_limit = d.pop("maximumTemperatureLimit", UNSET)

        _low_temperature_protection = d.pop("lowTemperatureProtection", UNSET)
        low_temperature_protection: Union[Unset, DeviceInfoParametersLowTemperatureProtection]
        if isinstance(_low_temperature_protection, Unset):
            low_temperature_protection = UNSET
        else:
            low_temperature_protection = DeviceInfoParametersLowTemperatureProtection.from_dict(
                _low_temperature_protection
            )

        _owd = d.pop("OWD", UNSET)
        owd: Union[Unset, DeviceInfoParametersOWD]
        if isinstance(_owd, Unset):
            owd = UNSET
        else:
            owd = DeviceInfoParametersOWD.from_dict(_owd)

        load_limit = d.pop("loadLimit", UNSET)

        max_load = d.pop("maxLoad", UNSET)

        _disable_buttons = d.pop("disableButtons", UNSET)
        disable_buttons: Union[Unset, DisableButtons]
        if isinstance(_disable_buttons, Unset):
            disable_buttons = UNSET
        else:
            disable_buttons = DisableButtons(_disable_buttons)

        device_info_parameters = cls(
            panel_mode=panel_mode,
            sensor_calibration=sensor_calibration,
            temperature_display=temperature_display,
            sensor_mode=sensor_mode,
            external_sensor_fallback=external_sensor_fallback,
            active_display_brightness=active_display_brightness,
            standby_display_brightness=standby_display_brightness,
            heating_setpoint=heating_setpoint,
            eco_setpoint=eco_setpoint,
            minimum_temperature_limit=minimum_temperature_limit,
            maximum_temperature_limit=maximum_temperature_limit,
            low_temperature_protection=low_temperature_protection,
            owd=owd,
            load_limit=load_limit,
            max_load=max_load,
            disable_buttons=disable_buttons,
        )

        device_info_parameters.additional_properties = d
        return device_info_parameters

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
