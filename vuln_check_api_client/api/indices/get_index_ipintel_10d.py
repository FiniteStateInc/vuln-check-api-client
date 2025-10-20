from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_index_ipintel_10d_start_cursor import GetIndexIpintel10DStartCursor
from ...models.render_response_with_metadata_array_advisory_ip_intel_record_paginate_pagination import (
    RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    start_cursor: Union[Unset, GetIndexIpintel10DStartCursor] = UNSET,
    cve: Union[Unset, str] = UNSET,
    alias: Union[Unset, str] = UNSET,
    iava: Union[Unset, str] = UNSET,
    threat_actor: Union[Unset, str] = UNSET,
    mitre_id: Union[Unset, str] = UNSET,
    misp_id: Union[Unset, str] = UNSET,
    ransomware: Union[Unset, str] = UNSET,
    botnet: Union[Unset, str] = UNSET,
    cidr: Union[Unset, str] = UNSET,
    asn: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    kind: Union[Unset, str] = UNSET,
    hostname: Union[Unset, str] = UNSET,
    matches: Union[Unset, str] = UNSET,
    updated_at_start_date: Union[Unset, str] = UNSET,
    updated_at_end_date: Union[Unset, str] = UNSET,
    last_mod_start_date: Union[Unset, str] = UNSET,
    last_mod_end_date: Union[Unset, str] = UNSET,
    pub_start_date: Union[Unset, str] = UNSET,
    pub_end_date: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["cursor"] = cursor

    json_start_cursor: Union[Unset, str] = UNSET
    if not isinstance(start_cursor, Unset):
        json_start_cursor = start_cursor.value

    params["start_cursor"] = json_start_cursor

    params["cve"] = cve

    params["alias"] = alias

    params["iava"] = iava

    params["threat_actor"] = threat_actor

    params["mitre_id"] = mitre_id

    params["misp_id"] = misp_id

    params["ransomware"] = ransomware

    params["botnet"] = botnet

    params["cidr"] = cidr

    params["asn"] = asn

    params["country"] = country

    params["country_code"] = country_code

    params["id"] = id

    params["kind"] = kind

    params["hostname"] = hostname

    params["matches"] = matches

    params["updatedAtStartDate"] = updated_at_start_date

    params["updatedAtEndDate"] = updated_at_end_date

    params["lastModStartDate"] = last_mod_start_date

    params["lastModEndDate"] = last_mod_end_date

    params["pubStartDate"] = pub_start_date

    params["pubEndDate"] = pub_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/index/ipintel-10d",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    if response.status_code == 200:
        response_200 = RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination.from_dict(response.json())

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
) -> Response[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    start_cursor: Union[Unset, GetIndexIpintel10DStartCursor] = UNSET,
    cve: Union[Unset, str] = UNSET,
    alias: Union[Unset, str] = UNSET,
    iava: Union[Unset, str] = UNSET,
    threat_actor: Union[Unset, str] = UNSET,
    mitre_id: Union[Unset, str] = UNSET,
    misp_id: Union[Unset, str] = UNSET,
    ransomware: Union[Unset, str] = UNSET,
    botnet: Union[Unset, str] = UNSET,
    cidr: Union[Unset, str] = UNSET,
    asn: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    kind: Union[Unset, str] = UNSET,
    hostname: Union[Unset, str] = UNSET,
    matches: Union[Unset, str] = UNSET,
    updated_at_start_date: Union[Unset, str] = UNSET,
    updated_at_end_date: Union[Unset, str] = UNSET,
    last_mod_start_date: Union[Unset, str] = UNSET,
    last_mod_end_date: Union[Unset, str] = UNSET,
    pub_start_date: Union[Unset, str] = UNSET,
    pub_end_date: Union[Unset, str] = UNSET,
) -> Response[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    r""" Return vulnerability data stored in index \"ipintel-10d\"

     ### Overview
    This endpoint allows you to retrieve a paginated list of all documents from the ipintel-10d index. \
    By default, a maximum of 100 documents are shown per page.

    **Index Description:** 10-Day IP Intelligence Index of Initial Access Targets and Command and
    Control Infrastructure

    ### Paging Over Large Data (cursor)
    In order to allow users to iterate over large index datasets, this endpoint provides a server-side
    \"cursor\" mechanism. To use the cursor, first call `GET /index/ipintel-10d?start_cursor`, the
    response will
    have a `next_cursor` id that clients will need to pass as a query parameter to the next request like
    `GET /index/ipintel-10d?cursor=<next_cursor_id>`

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        start_cursor (Union[Unset, GetIndexIpintel10DStartCursor]):
        cve (Union[Unset, str]):
        alias (Union[Unset, str]):
        iava (Union[Unset, str]):
        threat_actor (Union[Unset, str]):
        mitre_id (Union[Unset, str]):
        misp_id (Union[Unset, str]):
        ransomware (Union[Unset, str]):
        botnet (Union[Unset, str]):
        cidr (Union[Unset, str]):
        asn (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        id (Union[Unset, str]):
        kind (Union[Unset, str]):
        hostname (Union[Unset, str]):
        matches (Union[Unset, str]):
        updated_at_start_date (Union[Unset, str]):
        updated_at_end_date (Union[Unset, str]):
        last_mod_start_date (Union[Unset, str]):
        last_mod_end_date (Union[Unset, str]):
        pub_start_date (Union[Unset, str]):
        pub_end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]
     """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        cursor=cursor,
        start_cursor=start_cursor,
        cve=cve,
        alias=alias,
        iava=iava,
        threat_actor=threat_actor,
        mitre_id=mitre_id,
        misp_id=misp_id,
        ransomware=ransomware,
        botnet=botnet,
        cidr=cidr,
        asn=asn,
        country=country,
        country_code=country_code,
        id=id,
        kind=kind,
        hostname=hostname,
        matches=matches,
        updated_at_start_date=updated_at_start_date,
        updated_at_end_date=updated_at_end_date,
        last_mod_start_date=last_mod_start_date,
        last_mod_end_date=last_mod_end_date,
        pub_start_date=pub_start_date,
        pub_end_date=pub_end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    start_cursor: Union[Unset, GetIndexIpintel10DStartCursor] = UNSET,
    cve: Union[Unset, str] = UNSET,
    alias: Union[Unset, str] = UNSET,
    iava: Union[Unset, str] = UNSET,
    threat_actor: Union[Unset, str] = UNSET,
    mitre_id: Union[Unset, str] = UNSET,
    misp_id: Union[Unset, str] = UNSET,
    ransomware: Union[Unset, str] = UNSET,
    botnet: Union[Unset, str] = UNSET,
    cidr: Union[Unset, str] = UNSET,
    asn: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    kind: Union[Unset, str] = UNSET,
    hostname: Union[Unset, str] = UNSET,
    matches: Union[Unset, str] = UNSET,
    updated_at_start_date: Union[Unset, str] = UNSET,
    updated_at_end_date: Union[Unset, str] = UNSET,
    last_mod_start_date: Union[Unset, str] = UNSET,
    last_mod_end_date: Union[Unset, str] = UNSET,
    pub_start_date: Union[Unset, str] = UNSET,
    pub_end_date: Union[Unset, str] = UNSET,
) -> Optional[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    r""" Return vulnerability data stored in index \"ipintel-10d\"

     ### Overview
    This endpoint allows you to retrieve a paginated list of all documents from the ipintel-10d index. \
    By default, a maximum of 100 documents are shown per page.

    **Index Description:** 10-Day IP Intelligence Index of Initial Access Targets and Command and
    Control Infrastructure

    ### Paging Over Large Data (cursor)
    In order to allow users to iterate over large index datasets, this endpoint provides a server-side
    \"cursor\" mechanism. To use the cursor, first call `GET /index/ipintel-10d?start_cursor`, the
    response will
    have a `next_cursor` id that clients will need to pass as a query parameter to the next request like
    `GET /index/ipintel-10d?cursor=<next_cursor_id>`

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        start_cursor (Union[Unset, GetIndexIpintel10DStartCursor]):
        cve (Union[Unset, str]):
        alias (Union[Unset, str]):
        iava (Union[Unset, str]):
        threat_actor (Union[Unset, str]):
        mitre_id (Union[Unset, str]):
        misp_id (Union[Unset, str]):
        ransomware (Union[Unset, str]):
        botnet (Union[Unset, str]):
        cidr (Union[Unset, str]):
        asn (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        id (Union[Unset, str]):
        kind (Union[Unset, str]):
        hostname (Union[Unset, str]):
        matches (Union[Unset, str]):
        updated_at_start_date (Union[Unset, str]):
        updated_at_end_date (Union[Unset, str]):
        last_mod_start_date (Union[Unset, str]):
        last_mod_end_date (Union[Unset, str]):
        pub_start_date (Union[Unset, str]):
        pub_end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]
     """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        cursor=cursor,
        start_cursor=start_cursor,
        cve=cve,
        alias=alias,
        iava=iava,
        threat_actor=threat_actor,
        mitre_id=mitre_id,
        misp_id=misp_id,
        ransomware=ransomware,
        botnet=botnet,
        cidr=cidr,
        asn=asn,
        country=country,
        country_code=country_code,
        id=id,
        kind=kind,
        hostname=hostname,
        matches=matches,
        updated_at_start_date=updated_at_start_date,
        updated_at_end_date=updated_at_end_date,
        last_mod_start_date=last_mod_start_date,
        last_mod_end_date=last_mod_end_date,
        pub_start_date=pub_start_date,
        pub_end_date=pub_end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    start_cursor: Union[Unset, GetIndexIpintel10DStartCursor] = UNSET,
    cve: Union[Unset, str] = UNSET,
    alias: Union[Unset, str] = UNSET,
    iava: Union[Unset, str] = UNSET,
    threat_actor: Union[Unset, str] = UNSET,
    mitre_id: Union[Unset, str] = UNSET,
    misp_id: Union[Unset, str] = UNSET,
    ransomware: Union[Unset, str] = UNSET,
    botnet: Union[Unset, str] = UNSET,
    cidr: Union[Unset, str] = UNSET,
    asn: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    kind: Union[Unset, str] = UNSET,
    hostname: Union[Unset, str] = UNSET,
    matches: Union[Unset, str] = UNSET,
    updated_at_start_date: Union[Unset, str] = UNSET,
    updated_at_end_date: Union[Unset, str] = UNSET,
    last_mod_start_date: Union[Unset, str] = UNSET,
    last_mod_end_date: Union[Unset, str] = UNSET,
    pub_start_date: Union[Unset, str] = UNSET,
    pub_end_date: Union[Unset, str] = UNSET,
) -> Response[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    r""" Return vulnerability data stored in index \"ipintel-10d\"

     ### Overview
    This endpoint allows you to retrieve a paginated list of all documents from the ipintel-10d index. \
    By default, a maximum of 100 documents are shown per page.

    **Index Description:** 10-Day IP Intelligence Index of Initial Access Targets and Command and
    Control Infrastructure

    ### Paging Over Large Data (cursor)
    In order to allow users to iterate over large index datasets, this endpoint provides a server-side
    \"cursor\" mechanism. To use the cursor, first call `GET /index/ipintel-10d?start_cursor`, the
    response will
    have a `next_cursor` id that clients will need to pass as a query parameter to the next request like
    `GET /index/ipintel-10d?cursor=<next_cursor_id>`

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        start_cursor (Union[Unset, GetIndexIpintel10DStartCursor]):
        cve (Union[Unset, str]):
        alias (Union[Unset, str]):
        iava (Union[Unset, str]):
        threat_actor (Union[Unset, str]):
        mitre_id (Union[Unset, str]):
        misp_id (Union[Unset, str]):
        ransomware (Union[Unset, str]):
        botnet (Union[Unset, str]):
        cidr (Union[Unset, str]):
        asn (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        id (Union[Unset, str]):
        kind (Union[Unset, str]):
        hostname (Union[Unset, str]):
        matches (Union[Unset, str]):
        updated_at_start_date (Union[Unset, str]):
        updated_at_end_date (Union[Unset, str]):
        last_mod_start_date (Union[Unset, str]):
        last_mod_end_date (Union[Unset, str]):
        pub_start_date (Union[Unset, str]):
        pub_end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]
     """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        cursor=cursor,
        start_cursor=start_cursor,
        cve=cve,
        alias=alias,
        iava=iava,
        threat_actor=threat_actor,
        mitre_id=mitre_id,
        misp_id=misp_id,
        ransomware=ransomware,
        botnet=botnet,
        cidr=cidr,
        asn=asn,
        country=country,
        country_code=country_code,
        id=id,
        kind=kind,
        hostname=hostname,
        matches=matches,
        updated_at_start_date=updated_at_start_date,
        updated_at_end_date=updated_at_end_date,
        last_mod_start_date=last_mod_start_date,
        last_mod_end_date=last_mod_end_date,
        pub_start_date=pub_start_date,
        pub_end_date=pub_end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    start_cursor: Union[Unset, GetIndexIpintel10DStartCursor] = UNSET,
    cve: Union[Unset, str] = UNSET,
    alias: Union[Unset, str] = UNSET,
    iava: Union[Unset, str] = UNSET,
    threat_actor: Union[Unset, str] = UNSET,
    mitre_id: Union[Unset, str] = UNSET,
    misp_id: Union[Unset, str] = UNSET,
    ransomware: Union[Unset, str] = UNSET,
    botnet: Union[Unset, str] = UNSET,
    cidr: Union[Unset, str] = UNSET,
    asn: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
    kind: Union[Unset, str] = UNSET,
    hostname: Union[Unset, str] = UNSET,
    matches: Union[Unset, str] = UNSET,
    updated_at_start_date: Union[Unset, str] = UNSET,
    updated_at_end_date: Union[Unset, str] = UNSET,
    last_mod_start_date: Union[Unset, str] = UNSET,
    last_mod_end_date: Union[Unset, str] = UNSET,
    pub_start_date: Union[Unset, str] = UNSET,
    pub_end_date: Union[Unset, str] = UNSET,
) -> Optional[Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]]:
    r""" Return vulnerability data stored in index \"ipintel-10d\"

     ### Overview
    This endpoint allows you to retrieve a paginated list of all documents from the ipintel-10d index. \
    By default, a maximum of 100 documents are shown per page.

    **Index Description:** 10-Day IP Intelligence Index of Initial Access Targets and Command and
    Control Infrastructure

    ### Paging Over Large Data (cursor)
    In order to allow users to iterate over large index datasets, this endpoint provides a server-side
    \"cursor\" mechanism. To use the cursor, first call `GET /index/ipintel-10d?start_cursor`, the
    response will
    have a `next_cursor` id that clients will need to pass as a query parameter to the next request like
    `GET /index/ipintel-10d?cursor=<next_cursor_id>`

    Args:
        page (Union[Unset, int]):
        limit (Union[Unset, int]):
        cursor (Union[Unset, str]):
        start_cursor (Union[Unset, GetIndexIpintel10DStartCursor]):
        cve (Union[Unset, str]):
        alias (Union[Unset, str]):
        iava (Union[Unset, str]):
        threat_actor (Union[Unset, str]):
        mitre_id (Union[Unset, str]):
        misp_id (Union[Unset, str]):
        ransomware (Union[Unset, str]):
        botnet (Union[Unset, str]):
        cidr (Union[Unset, str]):
        asn (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        id (Union[Unset, str]):
        kind (Union[Unset, str]):
        hostname (Union[Unset, str]):
        matches (Union[Unset, str]):
        updated_at_start_date (Union[Unset, str]):
        updated_at_end_date (Union[Unset, str]):
        last_mod_start_date (Union[Unset, str]):
        last_mod_end_date (Union[Unset, str]):
        pub_start_date (Union[Unset, str]):
        pub_end_date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RenderResponseWithMetadataArrayAdvisoryIpIntelRecordPaginatePagination, str]
     """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            cursor=cursor,
            start_cursor=start_cursor,
            cve=cve,
            alias=alias,
            iava=iava,
            threat_actor=threat_actor,
            mitre_id=mitre_id,
            misp_id=misp_id,
            ransomware=ransomware,
            botnet=botnet,
            cidr=cidr,
            asn=asn,
            country=country,
            country_code=country_code,
            id=id,
            kind=kind,
            hostname=hostname,
            matches=matches,
            updated_at_start_date=updated_at_start_date,
            updated_at_end_date=updated_at_end_date,
            last_mod_start_date=last_mod_start_date,
            last_mod_end_date=last_mod_end_date,
            pub_start_date=pub_start_date,
            pub_end_date=pub_end_date,
        )
    ).parsed
