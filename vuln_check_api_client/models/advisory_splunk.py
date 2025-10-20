from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_splunk_product import AdvisorySplunkProduct


T = TypeVar("T", bound="AdvisorySplunk")


@_attrs_define
class AdvisorySplunk:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        affected_products (Union[Unset, list['AdvisorySplunkProduct']]):
        bug_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    affected_products: Union[Unset, list["AdvisorySplunkProduct"]] = UNSET
    bug_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        affected_products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_products, Unset):
            affected_products = []
            for affected_products_item_data in self.affected_products:
                affected_products_item = affected_products_item_data.to_dict()
                affected_products.append(affected_products_item)

        bug_id = self.bug_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if bug_id is not UNSET:
            field_dict["bug_id"] = bug_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_splunk_product import AdvisorySplunkProduct

        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        affected_products = []
        _affected_products = d.pop("affected_products", UNSET)
        for affected_products_item_data in _affected_products or []:
            affected_products_item = AdvisorySplunkProduct.from_dict(affected_products_item_data)

            affected_products.append(affected_products_item)

        bug_id = d.pop("bug_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_splunk = cls(
            advisory_id=advisory_id,
            affected_products=affected_products,
            bug_id=bug_id,
            cve=cve,
            date_added=date_added,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_splunk.additional_properties = d
        return advisory_splunk

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
