from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRockyPackage")


@_attrs_define
class AdvisoryRockyPackage:
    """
    Attributes:
        distro (Union[Unset, str]):
        name (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    distro: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distro = self.distro

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distro is not UNSET:
            field_dict["distro"] = distro
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        distro = d.pop("distro", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        advisory_rocky_package = cls(
            distro=distro,
            name=name,
            version=version,
        )

        advisory_rocky_package.additional_properties = d
        return advisory_rocky_package

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
