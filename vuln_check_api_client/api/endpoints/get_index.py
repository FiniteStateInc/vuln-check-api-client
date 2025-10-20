from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.render_response_array_params_index_list import RenderResponseArrayParamsIndexList
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/index",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RenderResponseArrayParamsIndexList, str]]:
    if response.status_code == 200:
        response_200 = RenderResponseArrayParamsIndexList.from_dict(response.json())

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
) -> Response[Union[RenderResponseArrayParamsIndexList, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RenderResponseArrayParamsIndexList, str]]:
    """Return a list of available indexes with endpoint links

     Return a list of available indexes with endpoint links that the user has access to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseArrayParamsIndexList, str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RenderResponseArrayParamsIndexList, str]]:
    """Return a list of available indexes with endpoint links

     Return a list of available indexes with endpoint links that the user has access to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseArrayParamsIndexList, str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[RenderResponseArrayParamsIndexList, str]]:
    """Return a list of available indexes with endpoint links

     Return a list of available indexes with endpoint links that the user has access to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseArrayParamsIndexList, str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[RenderResponseArrayParamsIndexList, str]]:
    """Return a list of available indexes with endpoint links

     Return a list of available indexes with endpoint links that the user has access to

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseArrayParamsIndexList, str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
