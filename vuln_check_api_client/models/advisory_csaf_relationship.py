from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_product import AdvisoryProduct


T = TypeVar("T", bound="AdvisoryCSAFRelationship")


@_attrs_define
class AdvisoryCSAFRelationship:
    """
    Attributes:
        category (Union[Unset, str]):
        full_product_name (Union[Unset, AdvisoryProduct]):
        product_reference (Union[Unset, str]):
        relates_to_product_reference (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    full_product_name: Union[Unset, "AdvisoryProduct"] = UNSET
    product_reference: Union[Unset, str] = UNSET
    relates_to_product_reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        full_product_name: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_product_name, Unset):
            full_product_name = self.full_product_name.to_dict()

        product_reference = self.product_reference

        relates_to_product_reference = self.relates_to_product_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if full_product_name is not UNSET:
            field_dict["full_product_name"] = full_product_name
        if product_reference is not UNSET:
            field_dict["product_reference"] = product_reference
        if relates_to_product_reference is not UNSET:
            field_dict["relates_to_product_reference"] = relates_to_product_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_product import AdvisoryProduct

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        _full_product_name = d.pop("full_product_name", UNSET)
        full_product_name: Union[Unset, AdvisoryProduct]
        if isinstance(_full_product_name, Unset):
            full_product_name = UNSET
        else:
            full_product_name = AdvisoryProduct.from_dict(_full_product_name)

        product_reference = d.pop("product_reference", UNSET)

        relates_to_product_reference = d.pop("relates_to_product_reference", UNSET)

        advisory_csaf_relationship = cls(
            category=category,
            full_product_name=full_product_name,
            product_reference=product_reference,
            relates_to_product_reference=relates_to_product_reference,
        )

        advisory_csaf_relationship.additional_properties = d
        return advisory_csaf_relationship

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
