from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBBraunAdvisory")


@_attrs_define
class AdvisoryBBraunAdvisory:
    """
    Attributes:
        attention (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        equipment (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vendor (Union[Unset, str]):
        vulnerabilities (Union[Unset, list[str]]):
    """

    attention: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    equipment: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    vulnerabilities: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attention = self.attention

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        equipment: Union[Unset, list[str]] = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment

        title = self.title

        updated_at = self.updated_at

        url = self.url

        vendor = self.vendor

        vulnerabilities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = self.vulnerabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attention is not UNSET:
            field_dict["attention"] = attention
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attention = d.pop("attention", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        equipment = cast(list[str], d.pop("equipment", UNSET))

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vendor = d.pop("vendor", UNSET)

        vulnerabilities = cast(list[str], d.pop("vulnerabilities", UNSET))

        advisory_b_braun_advisory = cls(
            attention=attention,
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            equipment=equipment,
            title=title,
            updated_at=updated_at,
            url=url,
            vendor=vendor,
            vulnerabilities=vulnerabilities,
        )

        advisory_b_braun_advisory.additional_properties = d
        return advisory_b_braun_advisory

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
