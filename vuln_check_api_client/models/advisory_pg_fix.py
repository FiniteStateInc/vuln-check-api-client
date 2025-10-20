from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPGFix")


@_attrs_define
class AdvisoryPGFix:
    """
    Attributes:
        affected (Union[Unset, str]):
        fixed (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        fixed = self.fixed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if fixed is not UNSET:
            field_dict["fixed"] = fixed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        fixed = d.pop("fixed", UNSET)

        advisory_pg_fix = cls(
            affected=affected,
            fixed=fixed,
        )

        advisory_pg_fix.additional_properties = d
        return advisory_pg_fix

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
