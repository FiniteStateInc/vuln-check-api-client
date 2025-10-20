from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVMWareAdvisory")


@_attrs_define
class AdvisoryVMWareAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        advisory_url (Union[Unset, str]):
        cvs_sv_3_range (Union[Unset, str]):
        issue_date (Union[Unset, str]):
        severity (Union[Unset, str]):
        synopsis (Union[Unset, str]):
        updated_on (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    advisory_url: Union[Unset, str] = UNSET
    cvs_sv_3_range: Union[Unset, str] = UNSET
    issue_date: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    synopsis: Union[Unset, str] = UNSET
    updated_on: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        advisory_url = self.advisory_url

        cvs_sv_3_range = self.cvs_sv_3_range

        issue_date = self.issue_date

        severity = self.severity

        synopsis = self.synopsis

        updated_on = self.updated_on

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["AdvisoryID"] = advisory_id
        if advisory_url is not UNSET:
            field_dict["AdvisoryURL"] = advisory_url
        if cvs_sv_3_range is not UNSET:
            field_dict["CVSSv3Range"] = cvs_sv_3_range
        if issue_date is not UNSET:
            field_dict["IssueDate"] = issue_date
        if severity is not UNSET:
            field_dict["Severity"] = severity
        if synopsis is not UNSET:
            field_dict["Synopsis"] = synopsis
        if updated_on is not UNSET:
            field_dict["UpdatedOn"] = updated_on
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("AdvisoryID", UNSET)

        advisory_url = d.pop("AdvisoryURL", UNSET)

        cvs_sv_3_range = d.pop("CVSSv3Range", UNSET)

        issue_date = d.pop("IssueDate", UNSET)

        severity = d.pop("Severity", UNSET)

        synopsis = d.pop("Synopsis", UNSET)

        updated_on = d.pop("UpdatedOn", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_vm_ware_advisory = cls(
            advisory_id=advisory_id,
            advisory_url=advisory_url,
            cvs_sv_3_range=cvs_sv_3_range,
            issue_date=issue_date,
            severity=severity,
            synopsis=synopsis,
            updated_on=updated_on,
            cve=cve,
            date_added=date_added,
            id=id,
            updated_at=updated_at,
        )

        advisory_vm_ware_advisory.additional_properties = d
        return advisory_vm_ware_advisory

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
