from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVendorProduct")


@_attrs_define
class AdvisoryVendorProduct:
    """
    Attributes:
        product (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    product: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product = self.product

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product = d.pop("product", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_vendor_product = cls(
            product=product,
            vendor=vendor,
        )

        advisory_vendor_product.additional_properties = d
        return advisory_vendor_product

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
