from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRockyVersion")


@_attrs_define
class AdvisoryRockyVersion:
    """
    Attributes:
        nvras (Union[Unset, list[str]]):
    """

    nvras: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nvras: Union[Unset, list[str]] = UNSET
        if not isinstance(self.nvras, Unset):
            nvras = self.nvras

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nvras is not UNSET:
            field_dict["nvras"] = nvras

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nvras = cast(list[str], d.pop("nvras", UNSET))

        advisory_rocky_version = cls(
            nvras=nvras,
        )

        advisory_rocky_version.additional_properties = d
        return advisory_rocky_version

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
