from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_gh_package import AdvisoryGHPackage


T = TypeVar("T", bound="AdvisoryGHNode")


@_attrs_define
class AdvisoryGHNode:
    """
    Attributes:
        package (Union[Unset, AdvisoryGHPackage]):
        severity (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        vulnerable_version_range (Union[Unset, str]):
    """

    package: Union[Unset, "AdvisoryGHPackage"] = UNSET
    severity: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vulnerable_version_range: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        severity = self.severity

        updated_at = self.updated_at

        vulnerable_version_range = self.vulnerable_version_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package is not UNSET:
            field_dict["package"] = package
        if severity is not UNSET:
            field_dict["severity"] = severity
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if vulnerable_version_range is not UNSET:
            field_dict["vulnerableVersionRange"] = vulnerable_version_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_gh_package import AdvisoryGHPackage

        d = dict(src_dict)
        _package = d.pop("package", UNSET)
        package: Union[Unset, AdvisoryGHPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AdvisoryGHPackage.from_dict(_package)

        severity = d.pop("severity", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        vulnerable_version_range = d.pop("vulnerableVersionRange", UNSET)

        advisory_gh_node = cls(
            package=package,
            severity=severity,
            updated_at=updated_at,
            vulnerable_version_range=vulnerable_version_range,
        )

        advisory_gh_node.additional_properties = d
        return advisory_gh_node

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
