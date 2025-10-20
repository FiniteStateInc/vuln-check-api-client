from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_atlassian_products import AdvisoryAtlassianProducts


T = TypeVar("T", bound="AdvisoryAtlassianVuln")


@_attrs_define
class AdvisoryAtlassianVuln:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        products (Union[Unset, list['AdvisoryAtlassianProducts']]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    products: Union[Unset, list["AdvisoryAtlassianProducts"]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if products is not UNSET:
            field_dict["products"] = products
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_atlassian_products import AdvisoryAtlassianProducts

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = AdvisoryAtlassianProducts.from_dict(products_item_data)

            products.append(products_item)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_atlassian_vuln = cls(
            cve=cve,
            date_added=date_added,
            products=products,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_atlassian_vuln.additional_properties = d
        return advisory_atlassian_vuln

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
