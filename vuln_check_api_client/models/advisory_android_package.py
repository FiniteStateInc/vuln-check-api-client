from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAndroidPackage")


@_attrs_define
class AdvisoryAndroidPackage:
    """
    Attributes:
        ecosystem (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    ecosystem: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ecosystem = self.ecosystem

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ecosystem is not UNSET:
            field_dict["ecosystem"] = ecosystem
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem = d.pop("ecosystem", UNSET)

        name = d.pop("name", UNSET)

        advisory_android_package = cls(
            ecosystem=ecosystem,
            name=name,
        )

        advisory_android_package.additional_properties = d
        return advisory_android_package

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
