from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryDotCMS")


@_attrs_define
class AdvisoryDotCMS:
    """
    Attributes:
        credit (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        fixed_version (Union[Unset, str]):
        issue_id (Union[Unset, str]):
        mitigation (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    credit: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fixed_version: Union[Unset, str] = UNSET
    issue_id: Union[Unset, str] = UNSET
    mitigation: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit = self.credit

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        fixed_version = self.fixed_version

        issue_id = self.issue_id

        mitigation = self.mitigation

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        severity = self.severity

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit is not UNSET:
            field_dict["credit"] = credit
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id
        if mitigation is not UNSET:
            field_dict["mitigation"] = mitigation
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit = d.pop("credit", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        fixed_version = d.pop("fixed_version", UNSET)

        issue_id = d.pop("issue_id", UNSET)

        mitigation = d.pop("mitigation", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_dot_cms = cls(
            credit=credit,
            cve=cve,
            date_added=date_added,
            description=description,
            fixed_version=fixed_version,
            issue_id=issue_id,
            mitigation=mitigation,
            references=references,
            severity=severity,
            title=title,
            url=url,
        )

        advisory_dot_cms.additional_properties = d
        return advisory_dot_cms

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
