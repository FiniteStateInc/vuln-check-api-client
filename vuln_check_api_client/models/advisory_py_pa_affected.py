from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_py_pa_package import AdvisoryPyPAPackage
    from ..models.advisory_py_pa_range import AdvisoryPyPARange


T = TypeVar("T", bound="AdvisoryPyPAAffected")


@_attrs_define
class AdvisoryPyPAAffected:
    """
    Attributes:
        package (Union[Unset, AdvisoryPyPAPackage]):
        ranges (Union[Unset, list['AdvisoryPyPARange']]):
        versions (Union[Unset, list[str]]):
    """

    package: Union[Unset, "AdvisoryPyPAPackage"] = UNSET
    ranges: Union[Unset, list["AdvisoryPyPARange"]] = UNSET
    versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        if package is not UNSET:
            field_dict["package"] = package
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_py_pa_package import AdvisoryPyPAPackage
        from ..models.advisory_py_pa_range import AdvisoryPyPARange

        d = dict(src_dict)
        _package = d.pop("package", UNSET)
        package: Union[Unset, AdvisoryPyPAPackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AdvisoryPyPAPackage.from_dict(_package)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = AdvisoryPyPARange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        versions = cast(list[str], d.pop("versions", UNSET))

        advisory_py_pa_affected = cls(
            package=package,
            ranges=ranges,
            versions=versions,
        )

        advisory_py_pa_affected.additional_properties = d
        return advisory_py_pa_affected

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
