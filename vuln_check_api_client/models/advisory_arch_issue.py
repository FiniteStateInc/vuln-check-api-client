from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryArchIssue")


@_attrs_define
class AdvisoryArchIssue:
    """
    Attributes:
        advisories (Union[Unset, list[str]]):
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        fixed (Union[Unset, str]):
        issues (Union[Unset, list[str]]): cves
        name (Union[Unset, str]):
        packages (Union[Unset, list[str]]):
        references (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        status (Union[Unset, str]):
        ticket (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    advisories: Union[Unset, list[str]] = UNSET
    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    issues: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    packages: Union[Unset, list[str]] = UNSET
    references: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    ticket: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.advisories, Unset):
            advisories = self.advisories

        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        fixed = self.fixed

        issues: Union[Unset, list[str]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues

        name = self.name

        packages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        severity = self.severity

        status = self.status

        ticket = self.ticket

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisories is not UNSET:
            field_dict["advisories"] = advisories
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if issues is not UNSET:
            field_dict["issues"] = issues
        if name is not UNSET:
            field_dict["name"] = name
        if packages is not UNSET:
            field_dict["packages"] = packages
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisories = cast(list[str], d.pop("advisories", UNSET))

        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        fixed = d.pop("fixed", UNSET)

        issues = cast(list[str], d.pop("issues", UNSET))

        name = d.pop("name", UNSET)

        packages = cast(list[str], d.pop("packages", UNSET))

        references = cast(list[str], d.pop("references", UNSET))

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        ticket = d.pop("ticket", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_arch_issue = cls(
            advisories=advisories,
            affected=affected,
            cve=cve,
            date_added=date_added,
            fixed=fixed,
            issues=issues,
            name=name,
            packages=packages,
            references=references,
            severity=severity,
            status=status,
            ticket=ticket,
            type_=type_,
        )

        advisory_arch_issue.additional_properties = d
        return advisory_arch_issue

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
