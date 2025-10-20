from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_alma_package import AdvisoryAlmaPackage


T = TypeVar("T", bound="AdvisoryAlmaPackageList")


@_attrs_define
class AdvisoryAlmaPackageList:
    """
    Attributes:
        name (Union[Unset, str]):
        packages (Union[Unset, list['AdvisoryAlmaPackage']]):
        shortname (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    packages: Union[Unset, list["AdvisoryAlmaPackage"]] = UNSET
    shortname: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        shortname = self.shortname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if packages is not UNSET:
            field_dict["packages"] = packages
        if shortname is not UNSET:
            field_dict["shortname"] = shortname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_alma_package import AdvisoryAlmaPackage

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = AdvisoryAlmaPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        shortname = d.pop("shortname", UNSET)

        advisory_alma_package_list = cls(
            name=name,
            packages=packages,
            shortname=shortname,
        )

        advisory_alma_package_list.additional_properties = d
        return advisory_alma_package_list

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
