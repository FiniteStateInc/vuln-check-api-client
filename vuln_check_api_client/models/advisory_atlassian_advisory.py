from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAtlassianAdvisory")


@_attrs_define
class AdvisoryAtlassianAdvisory:
    """
    Attributes:
        affected_version (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        detailed_summary (Union[Unset, str]): overloading in places with 'RiskAssessment' and other places with
            'Description'
        fixed_version (Union[Unset, str]):
        link (Union[Unset, str]):
        products (Union[Unset, list[str]]):
        references (Union[Unset, list[str]]):
        release_date (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    affected_version: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    detailed_summary: Union[Unset, str] = UNSET
    fixed_version: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    products: Union[Unset, list[str]] = UNSET
    references: Union[Unset, list[str]] = UNSET
    release_date: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_version: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_version, Unset):
            affected_version = self.affected_version

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        detailed_summary = self.detailed_summary

        fixed_version = self.fixed_version

        link = self.link

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        release_date = self.release_date

        severity = self.severity

        summary = self.summary

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_version is not UNSET:
            field_dict["affected_version"] = affected_version
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if detailed_summary is not UNSET:
            field_dict["detailed_summary"] = detailed_summary
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if link is not UNSET:
            field_dict["link"] = link
        if products is not UNSET:
            field_dict["products"] = products
        if references is not UNSET:
            field_dict["references"] = references
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_version = cast(list[str], d.pop("affected_version", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        detailed_summary = d.pop("detailed_summary", UNSET)

        fixed_version = d.pop("fixed_version", UNSET)

        link = d.pop("link", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        references = cast(list[str], d.pop("references", UNSET))

        release_date = d.pop("release_date", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_atlassian_advisory = cls(
            affected_version=affected_version,
            cve=cve,
            date_added=date_added,
            detailed_summary=detailed_summary,
            fixed_version=fixed_version,
            link=link,
            products=products,
            references=references,
            release_date=release_date,
            severity=severity,
            summary=summary,
            title=title,
            updated_at=updated_at,
        )

        advisory_atlassian_advisory.additional_properties = d
        return advisory_atlassian_advisory

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
