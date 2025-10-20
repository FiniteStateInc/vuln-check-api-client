from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVCCPEDictionary")


@_attrs_define
class AdvisoryVCCPEDictionary:
    """
    Attributes:
        base_cpe (Union[Unset, str]):
        versions (Union[Unset, list[str]]):
    """

    base_cpe: Union[Unset, str] = UNSET
    versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_cpe = self.base_cpe

        versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_cpe is not UNSET:
            field_dict["baseCPE"] = base_cpe
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_cpe = d.pop("baseCPE", UNSET)

        versions = cast(list[str], d.pop("versions", UNSET))

        advisory_vccpe_dictionary = cls(
            base_cpe=base_cpe,
            versions=versions,
        )

        advisory_vccpe_dictionary.additional_properties = d
        return advisory_vccpe_dictionary

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
