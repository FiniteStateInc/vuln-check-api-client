from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryOkta")


@_attrs_define
class AdvisoryOkta:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        cwe (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        resolution (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    cwe: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    resolution: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        cwe = self.cwe

        date_added = self.date_added

        description = self.description

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        resolution = self.resolution

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if references is not UNSET:
            field_dict["references"] = references
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_products = d.pop("affected_products", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        cwe = d.pop("cwe", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        resolution = d.pop("resolution", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_okta = cls(
            affected_products=affected_products,
            cve=cve,
            cvss=cvss,
            cwe=cwe,
            date_added=date_added,
            description=description,
            references=references,
            resolution=resolution,
            title=title,
            url=url,
        )

        advisory_okta.additional_properties = d
        return advisory_okta

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
