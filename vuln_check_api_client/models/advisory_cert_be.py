from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCertBE")


@_attrs_define
class AdvisoryCertBE:
    """
    Attributes:
        affected_software (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        mitigation (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        risk (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerability_type (Union[Unset, list[str]]):
    """

    affected_software: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mitigation: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    risk: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerability_type: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_software: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_software, Unset):
            affected_software = self.affected_software

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        mitigation = self.mitigation

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        risk = self.risk

        summary = self.summary

        title = self.title

        updated_at = self.updated_at

        url = self.url

        vulnerability_type: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerability_type, Unset):
            vulnerability_type = self.vulnerability_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_software is not UNSET:
            field_dict["affected_software"] = affected_software
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if references is not UNSET:
            field_dict["references"] = references
        if risk is not UNSET:
            field_dict["risk"] = risk
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerability_type is not UNSET:
            field_dict["vulnerability_type"] = vulnerability_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_software = cast(list[str], d.pop("affected_software", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        risk = d.pop("risk", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vulnerability_type = cast(list[str], d.pop("vulnerability_type", UNSET))

        advisory_cert_be = cls(
            affected_software=affected_software,
            cve=cve,
            date_added=date_added,
            id=id,
            mitigation=mitigation,
            references=references,
            risk=risk,
            summary=summary,
            title=title,
            updated_at=updated_at,
            url=url,
            vulnerability_type=vulnerability_type,
        )

        advisory_cert_be.additional_properties = d
        return advisory_cert_be

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
