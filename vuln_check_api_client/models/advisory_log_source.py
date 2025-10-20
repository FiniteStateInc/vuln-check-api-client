from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryLogSource")


@_attrs_define
class AdvisoryLogSource:
    """
    Attributes:
        category (Union[Unset, str]):
        definition (Union[Unset, str]):
        product (Union[Unset, str]):
        service (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        definition = self.definition

        product = self.product

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if definition is not UNSET:
            field_dict["definition"] = definition
        if product is not UNSET:
            field_dict["product"] = product
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        definition = d.pop("definition", UNSET)

        product = d.pop("product", UNSET)

        service = d.pop("service", UNSET)

        advisory_log_source = cls(
            category=category,
            definition=definition,
            product=product,
            service=service,
        )

        advisory_log_source.additional_properties = d
        return advisory_log_source

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
