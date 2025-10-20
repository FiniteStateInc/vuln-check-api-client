from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_backup_index_index import GetBackupIndexIndex
from ...models.render_response_with_metadata_v3_controllers_backup_response_data_v3_controllers_backup_response_metadata import (
    RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata,
)
from ...types import Response


def _get_kwargs(
    index: GetBackupIndexIndex,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/backup/{index}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    if response.status_code == 200:
        response_200 = (
            RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata.from_dict(
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
) -> Response[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    index: GetBackupIndexIndex,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    """Retrieve a list of backups by index

     Retrieve a list of VulnCheck backups by index

    Args:
        index (GetBackupIndexIndex):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index: GetBackupIndexIndex,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    """Retrieve a list of backups by index

     Retrieve a list of VulnCheck backups by index

    Args:
        index (GetBackupIndexIndex):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]
    """

    return sync_detailed(
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    index: GetBackupIndexIndex,
    *,
    client: AuthenticatedClient,
) -> Response[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    """Retrieve a list of backups by index

     Retrieve a list of VulnCheck backups by index

    Args:
        index (GetBackupIndexIndex):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index: GetBackupIndexIndex,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]]:
    """Retrieve a list of backups by index

     Retrieve a list of VulnCheck backups by index

    Args:
        index (GetBackupIndexIndex):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataV3ControllersBackupResponseDataV3ControllersBackupResponseMetadata, str]
    """

    return (
        await asyncio_detailed(
            index=index,
            client=client,
        )
    ).parsed
