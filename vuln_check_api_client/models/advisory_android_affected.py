from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_android_package import AdvisoryAndroidPackage
    from ..models.advisory_android_range import AdvisoryAndroidRange
    from ..models.advisory_eco_system import AdvisoryEcoSystem


T = TypeVar("T", bound="AdvisoryAndroidAffected")


@_attrs_define
class AdvisoryAndroidAffected:
    """
    Attributes:
        ecosystem_specific (Union[Unset, AdvisoryEcoSystem]):
        package (Union[Unset, AdvisoryAndroidPackage]):
        ranges (Union[Unset, list['AdvisoryAndroidRange']]):
        versions (Union[Unset, list[str]]):
    """

    ecosystem_specific: Union[Unset, "AdvisoryEcoSystem"] = UNSET
    package: Union[Unset, "AdvisoryAndroidPackage"] = UNSET
    ranges: Union[Unset, list["AdvisoryAndroidRange"]] = UNSET
    versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ecosystem_specific: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ecosystem_specific, Unset):
            ecosystem_specific = self.ecosystem_specific.to_dict()

        package: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ecosystem_specific is not UNSET:
            field_dict["ecosystem_specific"] = ecosystem_specific
        if package is not UNSET:
            field_dict["package"] = package
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_android_package import AdvisoryAndroidPackage
        from ..models.advisory_android_range import AdvisoryAndroidRange
        from ..models.advisory_eco_system import AdvisoryEcoSystem

        d = dict(src_dict)
        _ecosystem_specific = d.pop("ecosystem_specific", UNSET)
        ecosystem_specific: Union[Unset, AdvisoryEcoSystem]
        if isinstance(_ecosystem_specific, Unset):
            ecosystem_specific = UNSET
        else:
            ecosystem_specific = AdvisoryEcoSystem.from_dict(_ecosystem_specific)

        _package = d.pop("package", UNSET)
        package: Union[Unset, AdvisoryAndroidPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AdvisoryAndroidPackage.from_dict(_package)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = AdvisoryAndroidRange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        versions = cast(list[str], d.pop("versions", UNSET))

        advisory_android_affected = cls(
            ecosystem_specific=ecosystem_specific,
            package=package,
            ranges=ranges,
            versions=versions,
        )

        advisory_android_affected.additional_properties = d
        return advisory_android_affected

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
