from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_haskell_version import AdvisoryHaskellVersion


T = TypeVar("T", bound="AdvisoryHaskellAffected")


@_attrs_define
class AdvisoryHaskellAffected:
    """
    Attributes:
        affected_constraint (Union[Unset, str]):
        affected_versions (Union[Unset, list['AdvisoryHaskellVersion']]):
        arch (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        os (Union[Unset, list[str]]):
        package (Union[Unset, str]):
    """

    affected_constraint: Union[Unset, str] = UNSET
    affected_versions: Union[Unset, list["AdvisoryHaskellVersion"]] = UNSET
    arch: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    os: Union[Unset, list[str]] = UNSET
    package: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_constraint = self.affected_constraint

        affected_versions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_versions, Unset):
            affected_versions = []
            for affected_versions_item_data in self.affected_versions:
                affected_versions_item = affected_versions_item_data.to_dict()
                affected_versions.append(affected_versions_item)

        arch: Union[Unset, list[str]] = UNSET
        if not isinstance(self.arch, Unset):
            arch = self.arch

        cvss = self.cvss

        os: Union[Unset, list[str]] = UNSET
        if not isinstance(self.os, Unset):
            os = self.os

        package = self.package

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_constraint is not UNSET:
            field_dict["affected_constraint"] = affected_constraint
        if affected_versions is not UNSET:
            field_dict["affected_versions"] = affected_versions
        if arch is not UNSET:
            field_dict["arch"] = arch
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if os is not UNSET:
            field_dict["os"] = os
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_haskell_version import AdvisoryHaskellVersion

        d = dict(src_dict)
        affected_constraint = d.pop("affected_constraint", UNSET)

        affected_versions = []
        _affected_versions = d.pop("affected_versions", UNSET)
        for affected_versions_item_data in _affected_versions or []:
            affected_versions_item = AdvisoryHaskellVersion.from_dict(affected_versions_item_data)

            affected_versions.append(affected_versions_item)

        arch = cast(list[str], d.pop("arch", UNSET))

        cvss = d.pop("cvss", UNSET)

        os = cast(list[str], d.pop("os", UNSET))

        package = d.pop("package", UNSET)

        advisory_haskell_affected = cls(
            affected_constraint=affected_constraint,
            affected_versions=affected_versions,
            arch=arch,
            cvss=cvss,
            os=os,
            package=package,
        )

        advisory_haskell_affected.additional_properties = d
        return advisory_haskell_affected

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
