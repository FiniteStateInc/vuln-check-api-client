from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMFullProductName")


@_attrs_define
class AdvisoryMFullProductName:
    """
    Attributes:
        cpe (Union[Unset, str]):
        product_id (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    cpe: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        product_id = self.product_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["CPE"] = cpe
        if product_id is not UNSET:
            field_dict["ProductID"] = product_id
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe = d.pop("CPE", UNSET)

        product_id = d.pop("ProductID", UNSET)

        value = d.pop("Value", UNSET)

        advisory_m_full_product_name = cls(
            cpe=cpe,
            product_id=product_id,
            value=value,
        )

        advisory_m_full_product_name.additional_properties = d
        return advisory_m_full_product_name

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
