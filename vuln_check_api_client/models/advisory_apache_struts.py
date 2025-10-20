from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryApacheStruts")


@_attrs_define
class AdvisoryApacheStruts:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        impact (Union[Unset, str]):
        rating (Union[Unset, str]):
        remediation (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerable_version (Union[Unset, list[str]]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    rating: Union[Unset, str] = UNSET
    remediation: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerable_version: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        impact = self.impact

        rating = self.rating

        remediation = self.remediation

        summary = self.summary

        title = self.title

        url = self.url

        vulnerable_version: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerable_version, Unset):
            vulnerable_version = self.vulnerable_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if impact is not UNSET:
            field_dict["impact"] = impact
        if rating is not UNSET:
            field_dict["rating"] = rating
        if remediation is not UNSET:
            field_dict["remediation"] = remediation
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerable_version is not UNSET:
            field_dict["vulnerable_version"] = vulnerable_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        impact = d.pop("impact", UNSET)

        rating = d.pop("rating", UNSET)

        remediation = d.pop("remediation", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vulnerable_version = cast(list[str], d.pop("vulnerable_version", UNSET))

        advisory_apache_struts = cls(
            cve=cve,
            date_added=date_added,
            id=id,
            impact=impact,
            rating=rating,
            remediation=remediation,
            summary=summary,
            title=title,
            url=url,
            vulnerable_version=vulnerable_version,
        )

        advisory_apache_struts.additional_properties = d
        return advisory_apache_struts

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
