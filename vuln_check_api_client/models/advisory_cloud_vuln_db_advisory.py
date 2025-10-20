from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCloudVulnDBAdvisory")


@_attrs_define
class AdvisoryCloudVulnDBAdvisory:
    """
    Attributes:
        affected_services (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        link (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
    """

    affected_services: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_services = self.affected_services

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        link = self.link

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_services is not UNSET:
            field_dict["affectedServices"] = affected_services
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if link is not UNSET:
            field_dict["link"] = link
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_services = d.pop("affectedServices", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        link = d.pop("link", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        advisory_cloud_vuln_db_advisory = cls(
            affected_services=affected_services,
            cve=cve,
            date_added=date_added,
            link=link,
            references=references,
            title=title,
        )

        advisory_cloud_vuln_db_advisory.additional_properties = d
        return advisory_cloud_vuln_db_advisory

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
