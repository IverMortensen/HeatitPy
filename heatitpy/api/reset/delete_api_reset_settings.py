from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_reset_settings_reset_settings import DeleteApiResetSettingsResetSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    reset_settings: Union[Unset, DeleteApiResetSettingsResetSettings] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_reset_settings: Union[Unset, str] = UNSET
    if not isinstance(reset_settings, Unset):
        json_reset_settings = reset_settings.value

    params["resetSettings"] = json_reset_settings

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/reset/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    reset_settings: Union[Unset, DeleteApiResetSettingsResetSettings] = UNSET,
) -> Response[Any]:
    """Reset settings on the device to factory default.

     Reset settings on the device to factory defaults. This will not reset network settings or remove the
    device from the app.

    Args:
        reset_settings (Union[Unset, DeleteApiResetSettingsResetSettings]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reset_settings=reset_settings,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    reset_settings: Union[Unset, DeleteApiResetSettingsResetSettings] = UNSET,
) -> Response[Any]:
    """Reset settings on the device to factory default.

     Reset settings on the device to factory defaults. This will not reset network settings or remove the
    device from the app.

    Args:
        reset_settings (Union[Unset, DeleteApiResetSettingsResetSettings]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reset_settings=reset_settings,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
