from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryThreatData")


@_attrs_define
class AdvisoryThreatData:
    """
    Attributes:
        category (Union[Unset, str]):
        details (Union[Unset, str]):
        product_ids (Union[Unset, list[str]]):
    """

    category: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    product_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        details = self.details

        product_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if details is not UNSET:
            field_dict["details"] = details
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        details = d.pop("details", UNSET)

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        advisory_threat_data = cls(
            category=category,
            details=details,
            product_ids=product_ids,
        )

        advisory_threat_data.additional_properties = d
        return advisory_threat_data

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
