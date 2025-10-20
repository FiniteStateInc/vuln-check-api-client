from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRustsecAffected")


@_attrs_define
class AdvisoryRustsecAffected:
    """
    Attributes:
        arch (Union[Unset, list[str]]):
        functions (Union[Unset, str]):
        os (Union[Unset, list[str]]):
    """

    arch: Union[Unset, list[str]] = UNSET
    functions: Union[Unset, str] = UNSET
    os: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch: Union[Unset, list[str]] = UNSET
        if not isinstance(self.arch, Unset):
            arch = self.arch

        functions = self.functions

        os: Union[Unset, list[str]] = UNSET
        if not isinstance(self.os, Unset):
            os = self.os

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if functions is not UNSET:
            field_dict["functions"] = functions
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arch = cast(list[str], d.pop("arch", UNSET))

        functions = d.pop("functions", UNSET)

        os = cast(list[str], d.pop("os", UNSET))

        advisory_rustsec_affected = cls(
            arch=arch,
            functions=functions,
            os=os,
        )

        advisory_rustsec_affected.additional_properties = d
        return advisory_rustsec_affected

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
