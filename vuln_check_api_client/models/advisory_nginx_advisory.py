from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNginxAdvisory")


@_attrs_define
class AdvisoryNginxAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        not_vuln_versions (Union[Unset, list[str]]):
        patch_pgp (Union[Unset, str]):
        patch_url (Union[Unset, str]):
        severity (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vuln_versions (Union[Unset, list[str]]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    not_vuln_versions: Union[Unset, list[str]] = UNSET
    patch_pgp: Union[Unset, str] = UNSET
    patch_url: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vuln_versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        not_vuln_versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.not_vuln_versions, Unset):
            not_vuln_versions = self.not_vuln_versions

        patch_pgp = self.patch_pgp

        patch_url = self.patch_url

        severity = self.severity

        updated_at = self.updated_at

        url = self.url

        vuln_versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vuln_versions, Unset):
            vuln_versions = self.vuln_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if not_vuln_versions is not UNSET:
            field_dict["not_vuln_versions"] = not_vuln_versions
        if patch_pgp is not UNSET:
            field_dict["patch_pgp"] = patch_pgp
        if patch_url is not UNSET:
            field_dict["patch_url"] = patch_url
        if severity is not UNSET:
            field_dict["severity"] = severity
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vuln_versions is not UNSET:
            field_dict["vuln_versions"] = vuln_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        not_vuln_versions = cast(list[str], d.pop("not_vuln_versions", UNSET))

        patch_pgp = d.pop("patch_pgp", UNSET)

        patch_url = d.pop("patch_url", UNSET)

        severity = d.pop("severity", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vuln_versions = cast(list[str], d.pop("vuln_versions", UNSET))

        advisory_nginx_advisory = cls(
            cve=cve,
            date_added=date_added,
            description=description,
            not_vuln_versions=not_vuln_versions,
            patch_pgp=patch_pgp,
            patch_url=patch_url,
            severity=severity,
            updated_at=updated_at,
            url=url,
            vuln_versions=vuln_versions,
        )

        advisory_nginx_advisory.additional_properties = d
        return advisory_nginx_advisory

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
