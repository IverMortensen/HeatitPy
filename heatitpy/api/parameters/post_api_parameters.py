from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disable_buttons import DisableButtons
from ...models.panel_mode import PanelMode
from ...models.post_api_parameters_response_400 import PostApiParametersResponse400
from ...models.post_api_parameters_response_422 import PostApiParametersResponse422
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    panel_mode: Union[Unset, PanelMode] = UNSET,
    sensor_calibration: Union[Unset, float] = UNSET,
    temperature_display: Union[Unset, bool] = UNSET,
    sensor_mode: Union[Unset, bool] = UNSET,
    external_sensor_fallback: Union[Unset, bool] = UNSET,
    active_display_brightness: Union[Unset, int] = UNSET,
    standby_display_brightness: Union[Unset, int] = UNSET,
    heating_setpoint: Union[Unset, float] = UNSET,
    eco_setpoint: Union[Unset, float] = UNSET,
    minimum_temperature_limit: Union[Unset, float] = UNSET,
    maximum_temperature_limit: Union[Unset, float] = UNSET,
    open_window_detection: Union[Unset, bool] = UNSET,
    load_limit: Union[Unset, int] = UNSET,
    disable_buttons: Union[Unset, DisableButtons] = UNSET,
    low_temperature_protection: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_panel_mode: Union[Unset, int] = UNSET
    if not isinstance(panel_mode, Unset):
        json_panel_mode = panel_mode.value

    params["panelMode"] = json_panel_mode

    params["sensorCalibration"] = sensor_calibration

    params["temperatureDisplay"] = temperature_display

    params["sensorMode"] = sensor_mode

    params["externalSensorFallback"] = external_sensor_fallback

    params["activeDisplayBrightness"] = active_display_brightness

    params["standbyDisplayBrightness"] = standby_display_brightness

    params["heatingSetpoint"] = heating_setpoint

    params["ecoSetpoint"] = eco_setpoint

    params["minimumTemperatureLimit"] = minimum_temperature_limit

    params["maximumTemperatureLimit"] = maximum_temperature_limit

    params["openWindowDetection"] = open_window_detection

    params["loadLimit"] = load_limit

    json_disable_buttons: Union[Unset, int] = UNSET
    if not isinstance(disable_buttons, Unset):
        json_disable_buttons = disable_buttons.value

    params["disableButtons"] = json_disable_buttons

    params["lowTemperatureProtection"] = low_temperature_protection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/parameters",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[DisableButtons, PanelMode, bool, float, int]:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                response_200_type_0 = PanelMode(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                response_200_type_13 = DisableButtons(data)

                return response_200_type_13
            except:  # noqa: E722
                pass
            return cast(Union[DisableButtons, PanelMode, bool, float, int], data)

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PostApiParametersResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 422:
        response_422 = PostApiParametersResponse422.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    panel_mode: Union[Unset, PanelMode] = UNSET,
    sensor_calibration: Union[Unset, float] = UNSET,
    temperature_display: Union[Unset, bool] = UNSET,
    sensor_mode: Union[Unset, bool] = UNSET,
    external_sensor_fallback: Union[Unset, bool] = UNSET,
    active_display_brightness: Union[Unset, int] = UNSET,
    standby_display_brightness: Union[Unset, int] = UNSET,
    heating_setpoint: Union[Unset, float] = UNSET,
    eco_setpoint: Union[Unset, float] = UNSET,
    minimum_temperature_limit: Union[Unset, float] = UNSET,
    maximum_temperature_limit: Union[Unset, float] = UNSET,
    open_window_detection: Union[Unset, bool] = UNSET,
    load_limit: Union[Unset, int] = UNSET,
    disable_buttons: Union[Unset, DisableButtons] = UNSET,
    low_temperature_protection: Union[Unset, int] = UNSET,
) -> Response[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    """Set parameters on the device.

     Change parameters on the device. At least one parameter is required.

    Args:
        panel_mode (Union[Unset, PanelMode]): Chooses the mode of the panel <br>**0** = Off
            <br>**1** = Heating <br>**2** = Eco
        sensor_calibration (Union[Unset, float]): Calibrate the sensor <br>**-6.0** = -6.0°
            (minimum) <br>**6.0** = 6.0° (maximum)
        temperature_display (Union[Unset, bool]): Choose what temperature to show in the display
            in standby mode. <br>**false** = Display setpoint temperature <br>**true** = Display
            measured temperature
        sensor_mode (Union[Unset, bool]): Choose which sensor mode the device should operate with
            <br>**false** = Internal sensor (Default) <br>**true** = External wireless sensor
        external_sensor_fallback (Union[Unset, bool]): Choose what happens if the external sensor
            stops reporting. <br>**false** = Off <br>**true** = internal sensor (Default)
        active_display_brightness (Union[Unset, int]): Set display brightness for active state
            <br>**1** = 10% <br>**10** = 100%
        standby_display_brightness (Union[Unset, int]): Set display brightness for standby state
            <br>**0** = 0% <br>**10** = 100%
        heating_setpoint (Union[Unset, float]): Desired heating temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        eco_setpoint (Union[Unset, float]): Desired ECO temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        minimum_temperature_limit (Union[Unset, float]): Set lowest temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        maximum_temperature_limit (Union[Unset, float]): Set highest temperature <br>**5.0** =
            5.0° <br>**40.0** = 40.0°
        open_window_detection (Union[Unset, bool]): Shows if the Open Window Detection feature is
            enabled or disabled. <br>**false** = disabled <br>**true** = enabled
        load_limit (Union[Unset, int]): The power the Panel should operate at. **1**=100W,
            **2**=200W, etc.
        disable_buttons (Union[Unset, DisableButtons]): Disable device buttons <br>**0** = Buttons
            are not disabled <br>**1** = Buttons are disabled <br>**2** = lock menu
        low_temperature_protection (Union[Unset, int]): Will turn on heating if the temperature
            drops below the value set in the parameter <br>**0** = disabled (Default) <br>**1-10** =
            Turn on when temperature is below value in °C

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]]]
    """

    kwargs = _get_kwargs(
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
        open_window_detection=open_window_detection,
        load_limit=load_limit,
        disable_buttons=disable_buttons,
        low_temperature_protection=low_temperature_protection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    panel_mode: Union[Unset, PanelMode] = UNSET,
    sensor_calibration: Union[Unset, float] = UNSET,
    temperature_display: Union[Unset, bool] = UNSET,
    sensor_mode: Union[Unset, bool] = UNSET,
    external_sensor_fallback: Union[Unset, bool] = UNSET,
    active_display_brightness: Union[Unset, int] = UNSET,
    standby_display_brightness: Union[Unset, int] = UNSET,
    heating_setpoint: Union[Unset, float] = UNSET,
    eco_setpoint: Union[Unset, float] = UNSET,
    minimum_temperature_limit: Union[Unset, float] = UNSET,
    maximum_temperature_limit: Union[Unset, float] = UNSET,
    open_window_detection: Union[Unset, bool] = UNSET,
    load_limit: Union[Unset, int] = UNSET,
    disable_buttons: Union[Unset, DisableButtons] = UNSET,
    low_temperature_protection: Union[Unset, int] = UNSET,
) -> Optional[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    """Set parameters on the device.

     Change parameters on the device. At least one parameter is required.

    Args:
        panel_mode (Union[Unset, PanelMode]): Chooses the mode of the panel <br>**0** = Off
            <br>**1** = Heating <br>**2** = Eco
        sensor_calibration (Union[Unset, float]): Calibrate the sensor <br>**-6.0** = -6.0°
            (minimum) <br>**6.0** = 6.0° (maximum)
        temperature_display (Union[Unset, bool]): Choose what temperature to show in the display
            in standby mode. <br>**false** = Display setpoint temperature <br>**true** = Display
            measured temperature
        sensor_mode (Union[Unset, bool]): Choose which sensor mode the device should operate with
            <br>**false** = Internal sensor (Default) <br>**true** = External wireless sensor
        external_sensor_fallback (Union[Unset, bool]): Choose what happens if the external sensor
            stops reporting. <br>**false** = Off <br>**true** = internal sensor (Default)
        active_display_brightness (Union[Unset, int]): Set display brightness for active state
            <br>**1** = 10% <br>**10** = 100%
        standby_display_brightness (Union[Unset, int]): Set display brightness for standby state
            <br>**0** = 0% <br>**10** = 100%
        heating_setpoint (Union[Unset, float]): Desired heating temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        eco_setpoint (Union[Unset, float]): Desired ECO temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        minimum_temperature_limit (Union[Unset, float]): Set lowest temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        maximum_temperature_limit (Union[Unset, float]): Set highest temperature <br>**5.0** =
            5.0° <br>**40.0** = 40.0°
        open_window_detection (Union[Unset, bool]): Shows if the Open Window Detection feature is
            enabled or disabled. <br>**false** = disabled <br>**true** = enabled
        load_limit (Union[Unset, int]): The power the Panel should operate at. **1**=100W,
            **2**=200W, etc.
        disable_buttons (Union[Unset, DisableButtons]): Disable device buttons <br>**0** = Buttons
            are not disabled <br>**1** = Buttons are disabled <br>**2** = lock menu
        low_temperature_protection (Union[Unset, int]): Will turn on heating if the temperature
            drops below the value set in the parameter <br>**0** = disabled (Default) <br>**1-10** =
            Turn on when temperature is below value in °C

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]]
    """

    return sync_detailed(
        client=client,
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
        open_window_detection=open_window_detection,
        load_limit=load_limit,
        disable_buttons=disable_buttons,
        low_temperature_protection=low_temperature_protection,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    panel_mode: Union[Unset, PanelMode] = UNSET,
    sensor_calibration: Union[Unset, float] = UNSET,
    temperature_display: Union[Unset, bool] = UNSET,
    sensor_mode: Union[Unset, bool] = UNSET,
    external_sensor_fallback: Union[Unset, bool] = UNSET,
    active_display_brightness: Union[Unset, int] = UNSET,
    standby_display_brightness: Union[Unset, int] = UNSET,
    heating_setpoint: Union[Unset, float] = UNSET,
    eco_setpoint: Union[Unset, float] = UNSET,
    minimum_temperature_limit: Union[Unset, float] = UNSET,
    maximum_temperature_limit: Union[Unset, float] = UNSET,
    open_window_detection: Union[Unset, bool] = UNSET,
    load_limit: Union[Unset, int] = UNSET,
    disable_buttons: Union[Unset, DisableButtons] = UNSET,
    low_temperature_protection: Union[Unset, int] = UNSET,
) -> Response[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    """Set parameters on the device.

     Change parameters on the device. At least one parameter is required.

    Args:
        panel_mode (Union[Unset, PanelMode]): Chooses the mode of the panel <br>**0** = Off
            <br>**1** = Heating <br>**2** = Eco
        sensor_calibration (Union[Unset, float]): Calibrate the sensor <br>**-6.0** = -6.0°
            (minimum) <br>**6.0** = 6.0° (maximum)
        temperature_display (Union[Unset, bool]): Choose what temperature to show in the display
            in standby mode. <br>**false** = Display setpoint temperature <br>**true** = Display
            measured temperature
        sensor_mode (Union[Unset, bool]): Choose which sensor mode the device should operate with
            <br>**false** = Internal sensor (Default) <br>**true** = External wireless sensor
        external_sensor_fallback (Union[Unset, bool]): Choose what happens if the external sensor
            stops reporting. <br>**false** = Off <br>**true** = internal sensor (Default)
        active_display_brightness (Union[Unset, int]): Set display brightness for active state
            <br>**1** = 10% <br>**10** = 100%
        standby_display_brightness (Union[Unset, int]): Set display brightness for standby state
            <br>**0** = 0% <br>**10** = 100%
        heating_setpoint (Union[Unset, float]): Desired heating temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        eco_setpoint (Union[Unset, float]): Desired ECO temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        minimum_temperature_limit (Union[Unset, float]): Set lowest temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        maximum_temperature_limit (Union[Unset, float]): Set highest temperature <br>**5.0** =
            5.0° <br>**40.0** = 40.0°
        open_window_detection (Union[Unset, bool]): Shows if the Open Window Detection feature is
            enabled or disabled. <br>**false** = disabled <br>**true** = enabled
        load_limit (Union[Unset, int]): The power the Panel should operate at. **1**=100W,
            **2**=200W, etc.
        disable_buttons (Union[Unset, DisableButtons]): Disable device buttons <br>**0** = Buttons
            are not disabled <br>**1** = Buttons are disabled <br>**2** = lock menu
        low_temperature_protection (Union[Unset, int]): Will turn on heating if the temperature
            drops below the value set in the parameter <br>**0** = disabled (Default) <br>**1-10** =
            Turn on when temperature is below value in °C

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]]]
    """

    kwargs = _get_kwargs(
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
        open_window_detection=open_window_detection,
        load_limit=load_limit,
        disable_buttons=disable_buttons,
        low_temperature_protection=low_temperature_protection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    panel_mode: Union[Unset, PanelMode] = UNSET,
    sensor_calibration: Union[Unset, float] = UNSET,
    temperature_display: Union[Unset, bool] = UNSET,
    sensor_mode: Union[Unset, bool] = UNSET,
    external_sensor_fallback: Union[Unset, bool] = UNSET,
    active_display_brightness: Union[Unset, int] = UNSET,
    standby_display_brightness: Union[Unset, int] = UNSET,
    heating_setpoint: Union[Unset, float] = UNSET,
    eco_setpoint: Union[Unset, float] = UNSET,
    minimum_temperature_limit: Union[Unset, float] = UNSET,
    maximum_temperature_limit: Union[Unset, float] = UNSET,
    open_window_detection: Union[Unset, bool] = UNSET,
    load_limit: Union[Unset, int] = UNSET,
    disable_buttons: Union[Unset, DisableButtons] = UNSET,
    low_temperature_protection: Union[Unset, int] = UNSET,
) -> Optional[
    Union[
        PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]
    ]
]:
    """Set parameters on the device.

     Change parameters on the device. At least one parameter is required.

    Args:
        panel_mode (Union[Unset, PanelMode]): Chooses the mode of the panel <br>**0** = Off
            <br>**1** = Heating <br>**2** = Eco
        sensor_calibration (Union[Unset, float]): Calibrate the sensor <br>**-6.0** = -6.0°
            (minimum) <br>**6.0** = 6.0° (maximum)
        temperature_display (Union[Unset, bool]): Choose what temperature to show in the display
            in standby mode. <br>**false** = Display setpoint temperature <br>**true** = Display
            measured temperature
        sensor_mode (Union[Unset, bool]): Choose which sensor mode the device should operate with
            <br>**false** = Internal sensor (Default) <br>**true** = External wireless sensor
        external_sensor_fallback (Union[Unset, bool]): Choose what happens if the external sensor
            stops reporting. <br>**false** = Off <br>**true** = internal sensor (Default)
        active_display_brightness (Union[Unset, int]): Set display brightness for active state
            <br>**1** = 10% <br>**10** = 100%
        standby_display_brightness (Union[Unset, int]): Set display brightness for standby state
            <br>**0** = 0% <br>**10** = 100%
        heating_setpoint (Union[Unset, float]): Desired heating temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        eco_setpoint (Union[Unset, float]): Desired ECO temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        minimum_temperature_limit (Union[Unset, float]): Set lowest temperature <br>**5.0** = 5.0°
            <br>**40.0** = 40.0°
        maximum_temperature_limit (Union[Unset, float]): Set highest temperature <br>**5.0** =
            5.0° <br>**40.0** = 40.0°
        open_window_detection (Union[Unset, bool]): Shows if the Open Window Detection feature is
            enabled or disabled. <br>**false** = disabled <br>**true** = enabled
        load_limit (Union[Unset, int]): The power the Panel should operate at. **1**=100W,
            **2**=200W, etc.
        disable_buttons (Union[Unset, DisableButtons]): Disable device buttons <br>**0** = Buttons
            are not disabled <br>**1** = Buttons are disabled <br>**2** = lock menu
        low_temperature_protection (Union[Unset, int]): Will turn on heating if the temperature
            drops below the value set in the parameter <br>**0** = disabled (Default) <br>**1-10** =
            Turn on when temperature is below value in °C

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiParametersResponse400, PostApiParametersResponse422, Union[DisableButtons, PanelMode, bool, float, int]]
    """

    return (
        await asyncio_detailed(
            client=client,
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
            open_window_detection=open_window_detection,
            load_limit=load_limit,
            disable_buttons=disable_buttons,
            low_temperature_protection=low_temperature_protection,
        )
    ).parsed
