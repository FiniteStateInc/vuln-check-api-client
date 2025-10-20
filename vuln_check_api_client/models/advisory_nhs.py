from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNHS")


@_attrs_define
class AdvisoryNHS:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        threat_id (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    threat_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        severity = self.severity

        summary = self.summary

        threat_id = self.threat_id

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if threat_id is not UNSET:
            field_dict["threat_id"] = threat_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        threat_id = d.pop("threat_id", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_nhs = cls(
            cve=cve,
            date_added=date_added,
            references=references,
            severity=severity,
            summary=summary,
            threat_id=threat_id,
            title=title,
            url=url,
        )

        advisory_nhs.additional_properties = d
        return advisory_nhs

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
