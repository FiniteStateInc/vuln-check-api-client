from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAtlassianProducts")


@_attrs_define
class AdvisoryAtlassianProducts:
    """
    Attributes:
        affected (Union[Unset, list[str]]):
        fixed (Union[Unset, list[str]]):
        name (Union[Unset, str]):
    """

    affected: Union[Unset, list[str]] = UNSET
    fixed: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = self.affected

        fixed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixed, Unset):
            fixed = self.fixed

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = cast(list[str], d.pop("affected", UNSET))

        fixed = cast(list[str], d.pop("fixed", UNSET))

        name = d.pop("name", UNSET)

        advisory_atlassian_products = cls(
            affected=affected,
            fixed=fixed,
            name=name,
        )

        advisory_atlassian_products.additional_properties = d
        return advisory_atlassian_products

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
