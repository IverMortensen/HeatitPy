from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_directlink_direct_link import PostApiDirectlinkDirectLink
from ...models.post_api_directlink_response_200 import PostApiDirectlinkResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    direct_link: PostApiDirectlinkDirectLink,
    ip_address: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_direct_link = direct_link.value
    params["directLink"] = json_direct_link

    params["ipAddress"] = ip_address

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/directlink",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostApiDirectlinkResponse200]:
    if response.status_code == 200:
        response_200 = PostApiDirectlinkResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostApiDirectlinkResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: PostApiDirectlinkDirectLink,
    ip_address: str,
) -> Response[PostApiDirectlinkResponse200]:
    """Set a Directlink connection.

     Set a DirectLink. Requires IP address of the device to connect to.

    Args:
        direct_link (PostApiDirectlinkDirectLink):
        ip_address (str):  Example: 192.168.1.100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiDirectlinkResponse200]
    """

    kwargs = _get_kwargs(
        direct_link=direct_link,
        ip_address=ip_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: PostApiDirectlinkDirectLink,
    ip_address: str,
) -> Optional[PostApiDirectlinkResponse200]:
    """Set a Directlink connection.

     Set a DirectLink. Requires IP address of the device to connect to.

    Args:
        direct_link (PostApiDirectlinkDirectLink):
        ip_address (str):  Example: 192.168.1.100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiDirectlinkResponse200
    """

    return sync_detailed(
        client=client,
        direct_link=direct_link,
        ip_address=ip_address,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: PostApiDirectlinkDirectLink,
    ip_address: str,
) -> Response[PostApiDirectlinkResponse200]:
    """Set a Directlink connection.

     Set a DirectLink. Requires IP address of the device to connect to.

    Args:
        direct_link (PostApiDirectlinkDirectLink):
        ip_address (str):  Example: 192.168.1.100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiDirectlinkResponse200]
    """

    kwargs = _get_kwargs(
        direct_link=direct_link,
        ip_address=ip_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    direct_link: PostApiDirectlinkDirectLink,
    ip_address: str,
) -> Optional[PostApiDirectlinkResponse200]:
    """Set a Directlink connection.

     Set a DirectLink. Requires IP address of the device to connect to.

    Args:
        direct_link (PostApiDirectlinkDirectLink):
        ip_address (str):  Example: 192.168.1.100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiDirectlinkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            direct_link=direct_link,
            ip_address=ip_address,
        )
    ).parsed
