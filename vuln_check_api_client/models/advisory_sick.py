from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySick")


@_attrs_define
class AdvisorySick:
    """
    Attributes:
        csaf_url (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        products (Union[Unset, list[str]]):
        title (Union[Unset, str]):
    """

    csaf_url: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    products: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csaf_url = self.csaf_url

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        id = self.id

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csaf_url is not UNSET:
            field_dict["csaf_url"] = csaf_url
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if products is not UNSET:
            field_dict["products"] = products
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csaf_url = d.pop("csaf_url", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        title = d.pop("title", UNSET)

        advisory_sick = cls(
            csaf_url=csaf_url,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            id=id,
            products=products,
            title=title,
        )

        advisory_sick.additional_properties = d
        return advisory_sick

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
