from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMEProduct")


@_attrs_define
class AdvisoryMEProduct:
    """
    Attributes:
        id (Union[Unset, str]):
        display_value (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    display_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_value = self.display_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["ID"] = id
        if display_value is not UNSET:
            field_dict["display_value"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("ID", UNSET)

        display_value = d.pop("display_value", UNSET)

        advisory_me_product = cls(
            id=id,
            display_value=display_value,
        )

        advisory_me_product.additional_properties = d
        return advisory_me_product

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
