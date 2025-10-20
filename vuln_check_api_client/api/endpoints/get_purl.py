from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.render_response_with_metadata_v3_controllers_purl_response_data_v3_controllers_purl_response_metadata import (
    RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    purl: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["purl"] = purl

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/purl",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    if response.status_code == 200:
        response_200 = (
            RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata.from_dict(
                response.json()
            )
        )

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
) -> Response[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    purl: str,
) -> Response[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    """Request vulnerabilities related to a PURL

     Based on the specified PURL, this endpoint will return a list of vulnerabilities that are related to
    the package. We currently support hex, golang, hackage, npm, and pypi

    Args:
        purl (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        purl=purl,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    purl: str,
) -> Optional[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    """Request vulnerabilities related to a PURL

     Based on the specified PURL, this endpoint will return a list of vulnerabilities that are related to
    the package. We currently support hex, golang, hackage, npm, and pypi

    Args:
        purl (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]
    """

    return sync_detailed(
        client=client,
        purl=purl,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    purl: str,
) -> Response[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    """Request vulnerabilities related to a PURL

     Based on the specified PURL, this endpoint will return a list of vulnerabilities that are related to
    the package. We currently support hex, golang, hackage, npm, and pypi

    Args:
        purl (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        purl=purl,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    purl: str,
) -> Optional[Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]]:
    """Request vulnerabilities related to a PURL

     Based on the specified PURL, this endpoint will return a list of vulnerabilities that are related to
    the package. We currently support hex, golang, hackage, npm, and pypi

    Args:
        purl (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataV3ControllersPurlResponseDataV3ControllersPurlResponseMetadata, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            purl=purl,
        )
    ).parsed
