from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCiscoAdvisory")


@_attrs_define
class AdvisoryCiscoAdvisory:
    """
    Attributes:
        cisco_bug_id (Union[Unset, str]): multiple
        csaf (Union[Unset, str]):
        cve (Union[Unset, list[str]]): multiple
        cvrf (Union[Unset, str]):
        cwe (Union[Unset, str]): multiple
        date_added (Union[Unset, str]):
        id (Union[Unset, int]):
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        related_resources (Union[Unset, str]):
        severity (Union[Unset, str]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        total_count (Union[Unset, int]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        version (Union[Unset, str]):
        workarounds (Union[Unset, str]):
        workflow_status (Union[Unset, str]):
    """

    cisco_bug_id: Union[Unset, str] = UNSET
    csaf: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvrf: Union[Unset, str] = UNSET
    cwe: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    related_resources: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    workarounds: Union[Unset, str] = UNSET
    workflow_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cisco_bug_id = self.cisco_bug_id

        csaf = self.csaf

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvrf = self.cvrf

        cwe = self.cwe

        date_added = self.date_added

        id = self.id

        identifier = self.identifier

        name = self.name

        related_resources = self.related_resources

        severity = self.severity

        status = self.status

        summary = self.summary

        title = self.title

        total_count = self.total_count

        updated_at = self.updated_at

        url = self.url

        version = self.version

        workarounds = self.workarounds

        workflow_status = self.workflow_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cisco_bug_id is not UNSET:
            field_dict["ciscoBugId"] = cisco_bug_id
        if csaf is not UNSET:
            field_dict["csaf"] = csaf
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvrf is not UNSET:
            field_dict["cvrf"] = cvrf
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if related_resources is not UNSET:
            field_dict["related_resources"] = related_resources
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version
        if workarounds is not UNSET:
            field_dict["workarounds"] = workarounds
        if workflow_status is not UNSET:
            field_dict["workflowStatus"] = workflow_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cisco_bug_id = d.pop("ciscoBugId", UNSET)

        csaf = d.pop("csaf", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvrf = d.pop("cvrf", UNSET)

        cwe = d.pop("cwe", UNSET)

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        related_resources = d.pop("related_resources", UNSET)

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        total_count = d.pop("totalCount", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        workarounds = d.pop("workarounds", UNSET)

        workflow_status = d.pop("workflowStatus", UNSET)

        advisory_cisco_advisory = cls(
            cisco_bug_id=cisco_bug_id,
            csaf=csaf,
            cve=cve,
            cvrf=cvrf,
            cwe=cwe,
            date_added=date_added,
            id=id,
            identifier=identifier,
            name=name,
            related_resources=related_resources,
            severity=severity,
            status=status,
            summary=summary,
            title=title,
            total_count=total_count,
            updated_at=updated_at,
            url=url,
            version=version,
            workarounds=workarounds,
            workflow_status=workflow_status,
        )

        advisory_cisco_advisory.additional_properties = d
        return advisory_cisco_advisory

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
