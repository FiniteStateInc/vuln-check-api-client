from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAffectedChrome")


@_attrs_define
class AdvisoryAffectedChrome:
    """
    Attributes:
        fixed_version (Union[Unset, str]):
        product (Union[Unset, str]):
    """

    fixed_version: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed_version = self.fixed_version

        product = self.product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixed_version = d.pop("fixed_version", UNSET)

        product = d.pop("product", UNSET)

        advisory_affected_chrome = cls(
            fixed_version=fixed_version,
            product=product,
        )

        advisory_affected_chrome.additional_properties = d
        return advisory_affected_chrome

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
