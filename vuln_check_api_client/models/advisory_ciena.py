from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_vulnerable_product import AdvisoryVulnerableProduct


T = TypeVar("T", bound="AdvisoryCiena")


@_attrs_define
class AdvisoryCiena:
    """
    Attributes:
        cves (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        issue_no (Union[Unset, int]):
        security_advisory_number (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerable_products (Union[Unset, list['AdvisoryVulnerableProduct']]):
    """

    cves: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    issue_no: Union[Unset, int] = UNSET
    security_advisory_number: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerable_products: Union[Unset, list["AdvisoryVulnerableProduct"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        date_added = self.date_added

        issue_no = self.issue_no

        security_advisory_number = self.security_advisory_number

        summary = self.summary

        title = self.title

        url = self.url

        vulnerable_products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerable_products, Unset):
            vulnerable_products = []
            for vulnerable_products_item_data in self.vulnerable_products:
                vulnerable_products_item = vulnerable_products_item_data.to_dict()
                vulnerable_products.append(vulnerable_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cves is not UNSET:
            field_dict["cves"] = cves
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if issue_no is not UNSET:
            field_dict["issue_no"] = issue_no
        if security_advisory_number is not UNSET:
            field_dict["security_advisory_number"] = security_advisory_number
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerable_products is not UNSET:
            field_dict["vulnerable_products"] = vulnerable_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_vulnerable_product import AdvisoryVulnerableProduct

        d = dict(src_dict)
        cves = cast(list[str], d.pop("cves", UNSET))

        date_added = d.pop("date_added", UNSET)

        issue_no = d.pop("issue_no", UNSET)

        security_advisory_number = d.pop("security_advisory_number", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vulnerable_products = []
        _vulnerable_products = d.pop("vulnerable_products", UNSET)
        for vulnerable_products_item_data in _vulnerable_products or []:
            vulnerable_products_item = AdvisoryVulnerableProduct.from_dict(vulnerable_products_item_data)

            vulnerable_products.append(vulnerable_products_item)

        advisory_ciena = cls(
            cves=cves,
            date_added=date_added,
            issue_no=issue_no,
            security_advisory_number=security_advisory_number,
            summary=summary,
            title=title,
            url=url,
            vulnerable_products=vulnerable_products,
        )

        advisory_ciena.additional_properties = d
        return advisory_ciena

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
