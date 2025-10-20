from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySiemensProductIdentificationHelper")


@_attrs_define
class AdvisorySiemensProductIdentificationHelper:
    """
    Attributes:
        model_numbers (Union[Unset, list[str]]):
    """

    model_numbers: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.model_numbers, Unset):
            model_numbers = self.model_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_numbers is not UNSET:
            field_dict["model_numbers"] = model_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_numbers = cast(list[str], d.pop("model_numbers", UNSET))

        advisory_siemens_product_identification_helper = cls(
            model_numbers=model_numbers,
        )

        advisory_siemens_product_identification_helper.additional_properties = d
        return advisory_siemens_product_identification_helper

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
