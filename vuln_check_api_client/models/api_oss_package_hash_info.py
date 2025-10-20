from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiOSSPackageHashInfo")


@_attrs_define
class ApiOSSPackageHashInfo:
    """
    Attributes:
        algorithm (Union[Unset, str]): See OSSPackageHashInfoAlgo* consts
        type_ (Union[Unset, str]): See OSSPackageHashInfoType* consts
        value (Union[Unset, str]): hex string digest or link to hash
    """

    algorithm: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm = d.pop("algorithm", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        api_oss_package_hash_info = cls(
            algorithm=algorithm,
            type_=type_,
            value=value,
        )

        api_oss_package_hash_info.additional_properties = d
        return api_oss_package_hash_info

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
