from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySAAdvisory")


@_attrs_define
class AdvisorySAAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        link (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        threats (Union[Unset, str]):
        vendor (Union[Unset, str]):
        warning_date (Union[Unset, str]):
        warning_number (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    threats: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    warning_date: Union[Unset, str] = UNSET
    warning_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        link = self.link

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        severity = self.severity

        threats = self.threats

        vendor = self.vendor

        warning_date = self.warning_date

        warning_number = self.warning_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if threats is not UNSET:
            field_dict["threats"] = threats
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if warning_date is not UNSET:
            field_dict["warningDate"] = warning_date
        if warning_number is not UNSET:
            field_dict["warningNumber"] = warning_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        link = d.pop("link", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        severity = d.pop("severity", UNSET)

        threats = d.pop("threats", UNSET)

        vendor = d.pop("vendor", UNSET)

        warning_date = d.pop("warningDate", UNSET)

        warning_number = d.pop("warningNumber", UNSET)

        advisory_sa_advisory = cls(
            cve=cve,
            date_added=date_added,
            description=description,
            link=link,
            references=references,
            severity=severity,
            threats=threats,
            vendor=vendor,
            warning_date=warning_date,
            warning_number=warning_number,
        )

        advisory_sa_advisory.additional_properties = d
        return advisory_sa_advisory

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
