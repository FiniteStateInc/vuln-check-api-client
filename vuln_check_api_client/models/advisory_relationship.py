from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRelationship")


@_attrs_define
class AdvisoryRelationship:
    """
    Attributes:
        product_reference (Union[Unset, str]):
        relates_to_product_reference (Union[Unset, str]):
        relation_type (Union[Unset, str]):
    """

    product_reference: Union[Unset, str] = UNSET
    relates_to_product_reference: Union[Unset, str] = UNSET
    relation_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_reference = self.product_reference

        relates_to_product_reference = self.relates_to_product_reference

        relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_reference is not UNSET:
            field_dict["productReference"] = product_reference
        if relates_to_product_reference is not UNSET:
            field_dict["relatesToProductReference"] = relates_to_product_reference
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_reference = d.pop("productReference", UNSET)

        relates_to_product_reference = d.pop("relatesToProductReference", UNSET)

        relation_type = d.pop("relationType", UNSET)

        advisory_relationship = cls(
            product_reference=product_reference,
            relates_to_product_reference=relates_to_product_reference,
            relation_type=relation_type,
        )

        advisory_relationship.additional_properties = d
        return advisory_relationship

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
