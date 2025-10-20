from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCNNVDEntryJSON")


@_attrs_define
class AdvisoryCNNVDEntryJSON:
    """
    Attributes:
        bugtraq_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        modified_date (Union[Unset, str]):
        name_cn (Union[Unset, str]):
        published_date (Union[Unset, str]):
        severity_cn (Union[Unset, str]):
        severity_en (Union[Unset, str]):
        source (Union[Unset, str]):
        url (Union[Unset, str]):
        vuln_description_cn (Union[Unset, str]):
        vuln_solution (Union[Unset, str]):
        vuln_type_cn (Union[Unset, str]):
        vuln_type_en (Union[Unset, str]):
    """

    bugtraq_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    modified_date: Union[Unset, str] = UNSET
    name_cn: Union[Unset, str] = UNSET
    published_date: Union[Unset, str] = UNSET
    severity_cn: Union[Unset, str] = UNSET
    severity_en: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vuln_description_cn: Union[Unset, str] = UNSET
    vuln_solution: Union[Unset, str] = UNSET
    vuln_type_cn: Union[Unset, str] = UNSET
    vuln_type_en: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bugtraq_id = self.bugtraq_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        modified_date = self.modified_date

        name_cn = self.name_cn

        published_date = self.published_date

        severity_cn = self.severity_cn

        severity_en = self.severity_en

        source = self.source

        url = self.url

        vuln_description_cn = self.vuln_description_cn

        vuln_solution = self.vuln_solution

        vuln_type_cn = self.vuln_type_cn

        vuln_type_en = self.vuln_type_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bugtraq_id is not UNSET:
            field_dict["bugtraq-id"] = bugtraq_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if modified_date is not UNSET:
            field_dict["modified-date"] = modified_date
        if name_cn is not UNSET:
            field_dict["name_cn"] = name_cn
        if published_date is not UNSET:
            field_dict["published-date"] = published_date
        if severity_cn is not UNSET:
            field_dict["severity_cn"] = severity_cn
        if severity_en is not UNSET:
            field_dict["severity_en"] = severity_en
        if source is not UNSET:
            field_dict["source"] = source
        if url is not UNSET:
            field_dict["url"] = url
        if vuln_description_cn is not UNSET:
            field_dict["vuln-description_cn"] = vuln_description_cn
        if vuln_solution is not UNSET:
            field_dict["vuln-solution"] = vuln_solution
        if vuln_type_cn is not UNSET:
            field_dict["vuln-type_cn"] = vuln_type_cn
        if vuln_type_en is not UNSET:
            field_dict["vuln-type_en"] = vuln_type_en

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bugtraq_id = d.pop("bugtraq-id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        modified_date = d.pop("modified-date", UNSET)

        name_cn = d.pop("name_cn", UNSET)

        published_date = d.pop("published-date", UNSET)

        severity_cn = d.pop("severity_cn", UNSET)

        severity_en = d.pop("severity_en", UNSET)

        source = d.pop("source", UNSET)

        url = d.pop("url", UNSET)

        vuln_description_cn = d.pop("vuln-description_cn", UNSET)

        vuln_solution = d.pop("vuln-solution", UNSET)

        vuln_type_cn = d.pop("vuln-type_cn", UNSET)

        vuln_type_en = d.pop("vuln-type_en", UNSET)

        advisory_cnnvd_entry_json = cls(
            bugtraq_id=bugtraq_id,
            cve=cve,
            date_added=date_added,
            id=id,
            modified_date=modified_date,
            name_cn=name_cn,
            published_date=published_date,
            severity_cn=severity_cn,
            severity_en=severity_en,
            source=source,
            url=url,
            vuln_description_cn=vuln_description_cn,
            vuln_solution=vuln_solution,
            vuln_type_cn=vuln_type_cn,
            vuln_type_en=vuln_type_en,
        )

        advisory_cnnvd_entry_json.additional_properties = d
        return advisory_cnnvd_entry_json

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
