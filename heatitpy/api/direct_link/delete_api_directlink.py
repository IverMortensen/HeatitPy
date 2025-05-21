from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_directlink_direct_link import DeleteApiDirectlinkDirectLink
from ...models.delete_api_directlink_response_200 import DeleteApiDirectlinkResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    direct_link: Union[Unset, DeleteApiDirectlinkDirectLink] = UNSET,
    device: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_direct_link: Union[Unset, str] = UNSET
    if not isinstance(direct_link, Unset):
        json_direct_link = direct_link.value

    params["directLink"] = json_direct_link

    params["device"] = device

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/directlink",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteApiDirectlinkResponse200]:
    if response.status_code == 200:
        response_200 = DeleteApiDirectlinkResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteApiDirectlinkResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: Union[Unset, DeleteApiDirectlinkDirectLink] = UNSET,
    device: Union[Unset, str] = UNSET,
) -> Response[DeleteApiDirectlinkResponse200]:
    """Delete a DirectLink connection.

     Removes a DirectLink connection.

    Args:
        direct_link (Union[Unset, DeleteApiDirectlinkDirectLink]):
        device (Union[Unset, str]):  Example: sdf87g4bnfc87a523rbsdf4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiDirectlinkResponse200]
    """

    kwargs = _get_kwargs(
        direct_link=direct_link,
        device=device,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: Union[Unset, DeleteApiDirectlinkDirectLink] = UNSET,
    device: Union[Unset, str] = UNSET,
) -> Optional[DeleteApiDirectlinkResponse200]:
    """Delete a DirectLink connection.

     Removes a DirectLink connection.

    Args:
        direct_link (Union[Unset, DeleteApiDirectlinkDirectLink]):
        device (Union[Unset, str]):  Example: sdf87g4bnfc87a523rbsdf4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiDirectlinkResponse200
    """

    return sync_detailed(
        client=client,
        direct_link=direct_link,
        device=device,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: Union[Unset, DeleteApiDirectlinkDirectLink] = UNSET,
    device: Union[Unset, str] = UNSET,
) -> Response[DeleteApiDirectlinkResponse200]:
    """Delete a DirectLink connection.

     Removes a DirectLink connection.

    Args:
        direct_link (Union[Unset, DeleteApiDirectlinkDirectLink]):
        device (Union[Unset, str]):  Example: sdf87g4bnfc87a523rbsdf4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiDirectlinkResponse200]
    """

    kwargs = _get_kwargs(
        direct_link=direct_link,
        device=device,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: Union[Unset, DeleteApiDirectlinkDirectLink] = UNSET,
    device: Union[Unset, str] = UNSET,
) -> Optional[DeleteApiDirectlinkResponse200]:
    """Delete a DirectLink connection.

     Removes a DirectLink connection.

    Args:
        direct_link (Union[Unset, DeleteApiDirectlinkDirectLink]):
        device (Union[Unset, str]):  Example: sdf87g4bnfc87a523rbsdf4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiDirectlinkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            direct_link=direct_link,
            device=device,
        )
    ).parsed
