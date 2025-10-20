from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEnisaIDProduct")


@_attrs_define
class AdvisoryEnisaIDProduct:
    """
    Attributes:
        id (Union[Unset, str]):
        product_name (Union[Unset, str]):
        product_version (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product_name = self.product_name

        product_version = self.product_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_version is not UNSET:
            field_dict["product_version"] = product_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_version = d.pop("product_version", UNSET)

        advisory_enisa_id_product = cls(
            id=id,
            product_name=product_name,
            product_version=product_version,
        )

        advisory_enisa_id_product.additional_properties = d
        return advisory_enisa_id_product

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
