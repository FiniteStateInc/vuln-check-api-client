from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryOpenCVDB")


@_attrs_define
class AdvisoryOpenCVDB:
    """
    Attributes:
        affected_platforms (Union[Unset, list[str]]):
        affected_services (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        disclosed_at (Union[Unset, str]):
        known_itw_exploitation (Union[Unset, bool]):
        manual_remediation (Union[Unset, str]):
        published_at (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_platforms: Union[Unset, list[str]] = UNSET
    affected_services: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    disclosed_at: Union[Unset, str] = UNSET
    known_itw_exploitation: Union[Unset, bool] = UNSET
    manual_remediation: Union[Unset, str] = UNSET
    published_at: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_platforms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_platforms, Unset):
            affected_platforms = self.affected_platforms

        affected_services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_services, Unset):
            affected_services = self.affected_services

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        disclosed_at = self.disclosed_at

        known_itw_exploitation = self.known_itw_exploitation

        manual_remediation = self.manual_remediation

        published_at = self.published_at

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_platforms is not UNSET:
            field_dict["affected_platforms"] = affected_platforms
        if affected_services is not UNSET:
            field_dict["affected_services"] = affected_services
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if disclosed_at is not UNSET:
            field_dict["disclosed_at"] = disclosed_at
        if known_itw_exploitation is not UNSET:
            field_dict["known_itw_exploitation"] = known_itw_exploitation
        if manual_remediation is not UNSET:
            field_dict["manual_remediation"] = manual_remediation
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if references is not UNSET:
            field_dict["references"] = references
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_platforms = cast(list[str], d.pop("affected_platforms", UNSET))

        affected_services = cast(list[str], d.pop("affected_services", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        disclosed_at = d.pop("disclosed_at", UNSET)

        known_itw_exploitation = d.pop("known_itw_exploitation", UNSET)

        manual_remediation = d.pop("manual_remediation", UNSET)

        published_at = d.pop("published_at", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_open_cvdb = cls(
            affected_platforms=affected_platforms,
            affected_services=affected_services,
            cve=cve,
            date_added=date_added,
            disclosed_at=disclosed_at,
            known_itw_exploitation=known_itw_exploitation,
            manual_remediation=manual_remediation,
            published_at=published_at,
            references=references,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_open_cvdb.additional_properties = d
        return advisory_open_cvdb

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
