from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHardwareUpdate")


@_attrs_define
class AdvisoryHardwareUpdate:
    """
    Attributes:
        affected_versions (Union[Unset, str]):
        cves (Union[Unset, list[str]]):
        hardware_platform (Union[Unset, str]):
        system (Union[Unset, str]):
        updated_version (Union[Unset, str]):
    """

    affected_versions: Union[Unset, str] = UNSET
    cves: Union[Unset, list[str]] = UNSET
    hardware_platform: Union[Unset, str] = UNSET
    system: Union[Unset, str] = UNSET
    updated_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_versions = self.affected_versions

        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        hardware_platform = self.hardware_platform

        system = self.system

        updated_version = self.updated_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_versions is not UNSET:
            field_dict["affectedVersions"] = affected_versions
        if cves is not UNSET:
            field_dict["cves"] = cves
        if hardware_platform is not UNSET:
            field_dict["hardwarePlatform"] = hardware_platform
        if system is not UNSET:
            field_dict["system"] = system
        if updated_version is not UNSET:
            field_dict["updatedVersion"] = updated_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_versions = d.pop("affectedVersions", UNSET)

        cves = cast(list[str], d.pop("cves", UNSET))

        hardware_platform = d.pop("hardwarePlatform", UNSET)

        system = d.pop("system", UNSET)

        updated_version = d.pop("updatedVersion", UNSET)

        advisory_hardware_update = cls(
            affected_versions=affected_versions,
            cves=cves,
            hardware_platform=hardware_platform,
            system=system,
            updated_version=updated_version,
        )

        advisory_hardware_update.additional_properties = d
        return advisory_hardware_update

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
