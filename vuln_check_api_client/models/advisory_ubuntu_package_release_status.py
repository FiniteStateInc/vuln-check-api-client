from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryUbuntuPackageReleaseStatus")


@_attrs_define
class AdvisoryUbuntuPackageReleaseStatus:
    """
    Attributes:
        affected (Union[Unset, bool]):
        fixed (Union[Unset, bool]):
        fixed_version (Union[Unset, str]):
        lts (Union[Unset, bool]):
        release (Union[Unset, str]):
        release_long (Union[Unset, str]):
        release_version (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    affected: Union[Unset, bool] = UNSET
    fixed: Union[Unset, bool] = UNSET
    fixed_version: Union[Unset, str] = UNSET
    lts: Union[Unset, bool] = UNSET
    release: Union[Unset, str] = UNSET
    release_long: Union[Unset, str] = UNSET
    release_version: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        fixed = self.fixed

        fixed_version = self.fixed_version

        lts = self.lts

        release = self.release

        release_long = self.release_long

        release_version = self.release_version

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if lts is not UNSET:
            field_dict["lts"] = lts
        if release is not UNSET:
            field_dict["release"] = release
        if release_long is not UNSET:
            field_dict["release_long"] = release_long
        if release_version is not UNSET:
            field_dict["release_version"] = release_version
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        fixed = d.pop("fixed", UNSET)

        fixed_version = d.pop("fixed_version", UNSET)

        lts = d.pop("lts", UNSET)

        release = d.pop("release", UNSET)

        release_long = d.pop("release_long", UNSET)

        release_version = d.pop("release_version", UNSET)

        status = d.pop("status", UNSET)

        advisory_ubuntu_package_release_status = cls(
            affected=affected,
            fixed=fixed,
            fixed_version=fixed_version,
            lts=lts,
            release=release,
            release_long=release_long,
            release_version=release_version,
            status=status,
        )

        advisory_ubuntu_package_release_status.additional_properties = d
        return advisory_ubuntu_package_release_status

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
