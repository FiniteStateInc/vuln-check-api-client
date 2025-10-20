from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCompassSecurity")


@_attrs_define
class AdvisoryCompassSecurity:
    """
    Attributes:
        csnc_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        effect (Union[Unset, str]):
        introduction (Union[Unset, str]):
        product (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        risk (Union[Unset, str]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    csnc_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    effect: Union[Unset, str] = UNSET
    introduction: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    risk: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csnc_id = self.csnc_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        effect = self.effect

        introduction = self.introduction

        product = self.product

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        risk = self.risk

        severity = self.severity

        title = self.title

        url = self.url

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csnc_id is not UNSET:
            field_dict["csnc_id"] = csnc_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if effect is not UNSET:
            field_dict["effect"] = effect
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if product is not UNSET:
            field_dict["product"] = product
        if references is not UNSET:
            field_dict["references"] = references
        if risk is not UNSET:
            field_dict["risk"] = risk
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csnc_id = d.pop("csnc_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        effect = d.pop("effect", UNSET)

        introduction = d.pop("introduction", UNSET)

        product = d.pop("product", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        risk = d.pop("risk", UNSET)

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_compass_security = cls(
            csnc_id=csnc_id,
            cve=cve,
            date_added=date_added,
            effect=effect,
            introduction=introduction,
            product=product,
            references=references,
            risk=risk,
            severity=severity,
            title=title,
            url=url,
            vendor=vendor,
        )

        advisory_compass_security.additional_properties = d
        return advisory_compass_security

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
