from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_vulncheck_c2_format import GetTagsVulncheckC2Format
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, GetTagsVulncheckC2Format] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tags/vulncheck-c2",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetTagsVulncheckC2Format] = UNSET,
) -> Response[str]:
    """Retrieve a list of C2 IP addresses

     Retrieve a list of IP addresses, identified as running Command & Control infrastructure

    Args:
        format_ (Union[Unset, GetTagsVulncheckC2Format]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetTagsVulncheckC2Format] = UNSET,
) -> Optional[str]:
    """Retrieve a list of C2 IP addresses

     Retrieve a list of IP addresses, identified as running Command & Control infrastructure

    Args:
        format_ (Union[Unset, GetTagsVulncheckC2Format]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetTagsVulncheckC2Format] = UNSET,
) -> Response[str]:
    """Retrieve a list of C2 IP addresses

     Retrieve a list of IP addresses, identified as running Command & Control infrastructure

    Args:
        format_ (Union[Unset, GetTagsVulncheckC2Format]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetTagsVulncheckC2Format] = UNSET,
) -> Optional[str]:
    """Retrieve a list of C2 IP addresses

     Retrieve a list of IP addresses, identified as running Command & Control infrastructure

    Args:
        format_ (Union[Unset, GetTagsVulncheckC2Format]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
        )
    ).parsed
