from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.render_response_with_metadata_array_string_v3_controllers_response_metadata import (
    RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cpe: str,
    is_vulnerable: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cpe"] = cpe

    params["isVulnerable"] = is_vulnerable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cpe",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    if response.status_code == 200:
        response_200 = RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata.from_dict(response.json())

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cpe: str,
    is_vulnerable: Union[Unset, str] = UNSET,
) -> Response[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    """Return CVE 's associated with a specific NIST CPE

     Based on the specified CPE (Common Platform Enumeration) URI string, this endpoint will return a
    list of vulnerabilities that are related to the package. We support v2.2 and v2.3

    Args:
        cpe (str):
        is_vulnerable (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        cpe=cpe,
        is_vulnerable=is_vulnerable,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cpe: str,
    is_vulnerable: Union[Unset, str] = UNSET,
) -> Optional[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    """Return CVE 's associated with a specific NIST CPE

     Based on the specified CPE (Common Platform Enumeration) URI string, this endpoint will return a
    list of vulnerabilities that are related to the package. We support v2.2 and v2.3

    Args:
        cpe (str):
        is_vulnerable (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]
    """

    return sync_detailed(
        client=client,
        cpe=cpe,
        is_vulnerable=is_vulnerable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cpe: str,
    is_vulnerable: Union[Unset, str] = UNSET,
) -> Response[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    """Return CVE 's associated with a specific NIST CPE

     Based on the specified CPE (Common Platform Enumeration) URI string, this endpoint will return a
    list of vulnerabilities that are related to the package. We support v2.2 and v2.3

    Args:
        cpe (str):
        is_vulnerable (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        cpe=cpe,
        is_vulnerable=is_vulnerable,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cpe: str,
    is_vulnerable: Union[Unset, str] = UNSET,
) -> Optional[Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]]:
    """Return CVE 's associated with a specific NIST CPE

     Based on the specified CPE (Common Platform Enumeration) URI string, this endpoint will return a
    list of vulnerabilities that are related to the package. We support v2.2 and v2.3

    Args:
        cpe (str):
        is_vulnerable (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataArrayStringV3ControllersResponseMetadata, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            cpe=cpe,
            is_vulnerable=is_vulnerable,
        )
    ).parsed
