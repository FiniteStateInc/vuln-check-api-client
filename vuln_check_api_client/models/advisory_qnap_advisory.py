from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryQNAPAdvisory")


@_attrs_define
class AdvisoryQNAPAdvisory:
    """
    Attributes:
        affected (Union[Unset, str]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        last_update_date (Union[Unset, str]):
        link (Union[Unset, str]):
        severity (Union[Unset, str]):
        severity_number (Union[Unset, str]):
        status (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    last_update_date: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    severity_number: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        last_update_date = self.last_update_date

        link = self.link

        severity = self.severity

        severity_number = self.severity_number

        status = self.status

        summary = self.summary

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if bulletin_id is not UNSET:
            field_dict["bulletin_id"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if last_update_date is not UNSET:
            field_dict["last_update_date"] = last_update_date
        if link is not UNSET:
            field_dict["link"] = link
        if severity is not UNSET:
            field_dict["severity"] = severity
        if severity_number is not UNSET:
            field_dict["severity_number"] = severity_number
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        bulletin_id = d.pop("bulletin_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        last_update_date = d.pop("last_update_date", UNSET)

        link = d.pop("link", UNSET)

        severity = d.pop("severity", UNSET)

        severity_number = d.pop("severity_number", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        advisory_qnap_advisory = cls(
            affected=affected,
            bulletin_id=bulletin_id,
            cve=cve,
            date_added=date_added,
            last_update_date=last_update_date,
            link=link,
            severity=severity,
            severity_number=severity_number,
            status=status,
            summary=summary,
            title=title,
        )

        advisory_qnap_advisory.additional_properties = d
        return advisory_qnap_advisory

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
