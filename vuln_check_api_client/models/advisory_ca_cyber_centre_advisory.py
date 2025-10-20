from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCACyberCentreAdvisory")


@_attrs_define
class AdvisoryCACyberCentreAdvisory:
    """
    Attributes:
        control_systems (Union[Unset, bool]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        html_url (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    control_systems: Union[Unset, bool] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_systems = self.control_systems

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        html_url = self.html_url

        serial_number = self.serial_number

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_systems is not UNSET:
            field_dict["control_systems"] = control_systems
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        control_systems = d.pop("control_systems", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        html_url = d.pop("html_url", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_ca_cyber_centre_advisory = cls(
            control_systems=control_systems,
            cve=cve,
            date_added=date_added,
            html_url=html_url,
            serial_number=serial_number,
            title=title,
            updated_at=updated_at,
        )

        advisory_ca_cyber_centre_advisory.additional_properties = d
        return advisory_ca_cyber_centre_advisory

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
