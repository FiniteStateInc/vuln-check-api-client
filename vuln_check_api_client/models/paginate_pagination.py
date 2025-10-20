from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paginate_match import PaginateMatch
    from ..models.paginate_pagination_opensearch_query import PaginatePaginationOpensearchQuery
    from ..models.paginate_param import PaginateParam


T = TypeVar("T", bound="PaginatePagination")


@_attrs_define
class PaginatePagination:
    """
    Attributes:
        cursor (Union[Unset, str]): Cursor for the current page
        first_item (Union[Unset, int]): First and last Item
        index (Union[Unset, str]): The requested index
        last_item (Union[Unset, int]):
        limit (Union[Unset, int]): Per-Page limit
        matches (Union[Unset, list['PaginateMatch']]):
        max_pages (Union[Unset, int]):
        next_cursor (Union[Unset, str]): Cursor for the next page
        opensearch_query (Union[Unset, PaginatePaginationOpensearchQuery]):
        order (Union[Unset, str]):
        page (Union[Unset, int]): The current Page number
        pages (Union[Unset, list[str]]):
        parameters (Union[Unset, list['PaginateParam']]):
        show_pages (Union[Unset, bool]):
        show_query (Union[Unset, bool]):
        sort (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        total_documents (Union[Unset, int]): The total number of items
        total_pages (Union[Unset, int]): The total number of pages
        warnings (Union[Unset, list[str]]):
    """

    cursor: Union[Unset, str] = UNSET
    first_item: Union[Unset, int] = UNSET
    index: Union[Unset, str] = UNSET
    last_item: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    matches: Union[Unset, list["PaginateMatch"]] = UNSET
    max_pages: Union[Unset, int] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    opensearch_query: Union[Unset, "PaginatePaginationOpensearchQuery"] = UNSET
    order: Union[Unset, str] = UNSET
    page: Union[Unset, int] = UNSET
    pages: Union[Unset, list[str]] = UNSET
    parameters: Union[Unset, list["PaginateParam"]] = UNSET
    show_pages: Union[Unset, bool] = UNSET
    show_query: Union[Unset, bool] = UNSET
    sort: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    total_documents: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    warnings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        first_item = self.first_item

        index = self.index

        last_item = self.last_item

        limit = self.limit

        matches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        max_pages = self.max_pages

        next_cursor = self.next_cursor

        opensearch_query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.opensearch_query, Unset):
            opensearch_query = self.opensearch_query.to_dict()

        order = self.order

        page = self.page

        pages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = self.pages

        parameters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        show_pages = self.show_pages

        show_query = self.show_query

        sort = self.sort

        timestamp = self.timestamp

        total_documents = self.total_documents

        total_pages = self.total_pages

        warnings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if first_item is not UNSET:
            field_dict["first_item"] = first_item
        if index is not UNSET:
            field_dict["index"] = index
        if last_item is not UNSET:
            field_dict["last_item"] = last_item
        if limit is not UNSET:
            field_dict["limit"] = limit
        if matches is not UNSET:
            field_dict["matches"] = matches
        if max_pages is not UNSET:
            field_dict["max_pages"] = max_pages
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if opensearch_query is not UNSET:
            field_dict["opensearch_query"] = opensearch_query
        if order is not UNSET:
            field_dict["order"] = order
        if page is not UNSET:
            field_dict["page"] = page
        if pages is not UNSET:
            field_dict["pages"] = pages
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if show_pages is not UNSET:
            field_dict["show_pages"] = show_pages
        if show_query is not UNSET:
            field_dict["show_query"] = show_query
        if sort is not UNSET:
            field_dict["sort"] = sort
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginate_match import PaginateMatch
        from ..models.paginate_pagination_opensearch_query import PaginatePaginationOpensearchQuery
        from ..models.paginate_param import PaginateParam

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        first_item = d.pop("first_item", UNSET)

        index = d.pop("index", UNSET)

        last_item = d.pop("last_item", UNSET)

        limit = d.pop("limit", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = PaginateMatch.from_dict(matches_item_data)

            matches.append(matches_item)

        max_pages = d.pop("max_pages", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        _opensearch_query = d.pop("opensearch_query", UNSET)
        opensearch_query: Union[Unset, PaginatePaginationOpensearchQuery]
        if isinstance(_opensearch_query, Unset):
            opensearch_query = UNSET
        else:
            opensearch_query = PaginatePaginationOpensearchQuery.from_dict(_opensearch_query)

        order = d.pop("order", UNSET)

        page = d.pop("page", UNSET)

        pages = cast(list[str], d.pop("pages", UNSET))

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = PaginateParam.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        show_pages = d.pop("show_pages", UNSET)

        show_query = d.pop("show_query", UNSET)

        sort = d.pop("sort", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        paginate_pagination = cls(
            cursor=cursor,
            first_item=first_item,
            index=index,
            last_item=last_item,
            limit=limit,
            matches=matches,
            max_pages=max_pages,
            next_cursor=next_cursor,
            opensearch_query=opensearch_query,
            order=order,
            page=page,
            pages=pages,
            parameters=parameters,
            show_pages=show_pages,
            show_query=show_query,
            sort=sort,
            timestamp=timestamp,
            total_documents=total_documents,
            total_pages=total_pages,
            warnings=warnings,
        )

        paginate_pagination.additional_properties = d
        return paginate_pagination

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
