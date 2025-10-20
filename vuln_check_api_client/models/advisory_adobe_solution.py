from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAdobeSolution")


@_attrs_define
class AdvisoryAdobeSolution:
    """
    Attributes:
        platform (Union[Unset, str]):
        product (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    platform: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        product = self.product

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if product is not UNSET:
            field_dict["product"] = product
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        product = d.pop("product", UNSET)

        version = d.pop("version", UNSET)

        advisory_adobe_solution = cls(
            platform=platform,
            product=product,
            version=version,
        )

        advisory_adobe_solution.additional_properties = d
        return advisory_adobe_solution

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
