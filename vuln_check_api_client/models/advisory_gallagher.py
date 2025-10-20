from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryGallagher")


@_attrs_define
class AdvisoryGallagher:
    """
    Attributes:
        active_exploitation (Union[Unset, bool]):
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        fixes (Union[Unset, str]):
        reported_by (Union[Unset, str]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    active_exploitation: Union[Unset, bool] = UNSET
    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fixes: Union[Unset, str] = UNSET
    reported_by: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_exploitation = self.active_exploitation

        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        fixes = self.fixes

        reported_by = self.reported_by

        severity = self.severity

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_exploitation is not UNSET:
            field_dict["activeExploitation"] = active_exploitation
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if fixes is not UNSET:
            field_dict["fixes"] = fixes
        if reported_by is not UNSET:
            field_dict["reportedBy"] = reported_by
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
        active_exploitation = d.pop("activeExploitation", UNSET)

        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        fixes = d.pop("fixes", UNSET)

        reported_by = d.pop("reportedBy", UNSET)

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_gallagher = cls(
            active_exploitation=active_exploitation,
            affected=affected,
            cve=cve,
            date_added=date_added,
            description=description,
            fixes=fixes,
            reported_by=reported_by,
            severity=severity,
            title=title,
            url=url,
        )

        advisory_gallagher.additional_properties = d
        return advisory_gallagher

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
