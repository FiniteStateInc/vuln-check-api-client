from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySonicWallAdvisory")


@_attrs_define
class AdvisorySonicWallAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        affected_products (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        cvss_vector (Union[Unset, str]):
        cvss_version (Union[Unset, float]):
        cwe (Union[Unset, str]):
        date_added (Union[Unset, str]):
        impact (Union[Unset, str]):
        is_workaround_available (Union[Unset, bool]):
        last_updated_when (Union[Unset, str]):
        published_when (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
        vuln_status (Union[Unset, str]):
        vulnerable_products_list (Union[Unset, list[str]]):
    """

    advisory_id: Union[Unset, str] = UNSET
    affected_products: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    cvss_version: Union[Unset, float] = UNSET
    cwe: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    is_workaround_available: Union[Unset, bool] = UNSET
    last_updated_when: Union[Unset, str] = UNSET
    published_when: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vuln_status: Union[Unset, str] = UNSET
    vulnerable_products_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        affected_products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_products, Unset):
            affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        cvss_vector = self.cvss_vector

        cvss_version = self.cvss_version

        cwe = self.cwe

        date_added = self.date_added

        impact = self.impact

        is_workaround_available = self.is_workaround_available

        last_updated_when = self.last_updated_when

        published_when = self.published_when

        summary = self.summary

        title = self.title

        url = self.url

        vuln_status = self.vuln_status

        vulnerable_products_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerable_products_list, Unset):
            vulnerable_products_list = self.vulnerable_products_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector
        if cvss_version is not UNSET:
            field_dict["cvss_version"] = cvss_version
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if impact is not UNSET:
            field_dict["impact"] = impact
        if is_workaround_available is not UNSET:
            field_dict["is_workaround_available"] = is_workaround_available
        if last_updated_when is not UNSET:
            field_dict["last_updated_when"] = last_updated_when
        if published_when is not UNSET:
            field_dict["published_when"] = published_when
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if vuln_status is not UNSET:
            field_dict["vuln_status"] = vuln_status
        if vulnerable_products_list is not UNSET:
            field_dict["vulnerable_products_list"] = vulnerable_products_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        affected_products = cast(list[str], d.pop("affected_products", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        cvss_version = d.pop("cvss_version", UNSET)

        cwe = d.pop("cwe", UNSET)

        date_added = d.pop("date_added", UNSET)

        impact = d.pop("impact", UNSET)

        is_workaround_available = d.pop("is_workaround_available", UNSET)

        last_updated_when = d.pop("last_updated_when", UNSET)

        published_when = d.pop("published_when", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        vuln_status = d.pop("vuln_status", UNSET)

        vulnerable_products_list = cast(list[str], d.pop("vulnerable_products_list", UNSET))

        advisory_sonic_wall_advisory = cls(
            advisory_id=advisory_id,
            affected_products=affected_products,
            cve=cve,
            cvss=cvss,
            cvss_vector=cvss_vector,
            cvss_version=cvss_version,
            cwe=cwe,
            date_added=date_added,
            impact=impact,
            is_workaround_available=is_workaround_available,
            last_updated_when=last_updated_when,
            published_when=published_when,
            summary=summary,
            title=title,
            url=url,
            vuln_status=vuln_status,
            vulnerable_products_list=vulnerable_products_list,
        )

        advisory_sonic_wall_advisory.additional_properties = d
        return advisory_sonic_wall_advisory

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
