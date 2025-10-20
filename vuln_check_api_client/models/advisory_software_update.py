from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySoftwareUpdate")


@_attrs_define
class AdvisorySoftwareUpdate:
    """
    Attributes:
        affected_version (Union[Unset, str]):
        cves (Union[Unset, list[str]]):
        operating_system (Union[Unset, str]):
        software_product (Union[Unset, str]):
        updated_version (Union[Unset, str]):
    """

    affected_version: Union[Unset, str] = UNSET
    cves: Union[Unset, list[str]] = UNSET
    operating_system: Union[Unset, str] = UNSET
    software_product: Union[Unset, str] = UNSET
    updated_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_version = self.affected_version

        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        operating_system = self.operating_system

        software_product = self.software_product

        updated_version = self.updated_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_version is not UNSET:
            field_dict["affectedVersion"] = affected_version
        if cves is not UNSET:
            field_dict["cves"] = cves
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if software_product is not UNSET:
            field_dict["softwareProduct"] = software_product
        if updated_version is not UNSET:
            field_dict["updatedVersion"] = updated_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_version = d.pop("affectedVersion", UNSET)

        cves = cast(list[str], d.pop("cves", UNSET))

        operating_system = d.pop("operatingSystem", UNSET)

        software_product = d.pop("softwareProduct", UNSET)

        updated_version = d.pop("updatedVersion", UNSET)

        advisory_software_update = cls(
            affected_version=affected_version,
            cves=cves,
            operating_system=operating_system,
            software_product=software_product,
            updated_version=updated_version,
        )

        advisory_software_update.additional_properties = d
        return advisory_software_update

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
