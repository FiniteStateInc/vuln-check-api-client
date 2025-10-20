from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVulnCheck")


@_attrs_define
class AdvisoryVulnCheck:
    """
    Attributes:
        affecting (Union[Unset, list[str]]):
        credit (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        cvss_v3_vector (Union[Unset, str]):
        date_added (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affecting: Union[Unset, list[str]] = UNSET
    credit: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    cvss_v3_vector: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affecting: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affecting, Unset):
            affecting = self.affecting

        credit: Union[Unset, list[str]] = UNSET
        if not isinstance(self.credit, Unset):
            credit = self.credit

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        cvss_v3_vector = self.cvss_v3_vector

        date_added = self.date_added

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        severity = self.severity

        title = self.title

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affecting is not UNSET:
            field_dict["affecting"] = affecting
        if credit is not UNSET:
            field_dict["credit"] = credit
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if cvss_v3_vector is not UNSET:
            field_dict["cvss_v3_vector"] = cvss_v3_vector
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affecting = cast(list[str], d.pop("affecting", UNSET))

        credit = cast(list[str], d.pop("credit", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        cvss_v3_vector = d.pop("cvss_v3_vector", UNSET)

        date_added = d.pop("date_added", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        advisory_vuln_check = cls(
            affecting=affecting,
            credit=credit,
            cve=cve,
            cvss=cvss,
            cvss_v3_vector=cvss_v3_vector,
            date_added=date_added,
            references=references,
            severity=severity,
            title=title,
            type_=type_,
            url=url,
        )

        advisory_vuln_check.additional_properties = d
        return advisory_vuln_check

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
