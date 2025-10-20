from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySolarWindsAdvisory")


@_attrs_define
class AdvisorySolarWindsAdvisory:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss_score (Union[Unset, str]):
        date_added (Union[Unset, str]):
        fixed_version (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    fixed_version: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_score = self.cvss_score

        date_added = self.date_added

        fixed_version = self.fixed_version

        severity = self.severity

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if severity is not UNSET:
            field_dict["severity"] = severity
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
        affected_products = d.pop("affected_products", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_score = d.pop("cvss_score", UNSET)

        date_added = d.pop("date_added", UNSET)

        fixed_version = d.pop("fixed_version", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_solar_winds_advisory = cls(
            affected_products=affected_products,
            cve=cve,
            cvss_score=cvss_score,
            date_added=date_added,
            fixed_version=fixed_version,
            severity=severity,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_solar_winds_advisory.additional_properties = d
        return advisory_solar_winds_advisory

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
