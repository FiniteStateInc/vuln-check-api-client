from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_siemens_product import AdvisorySiemensProduct


T = TypeVar("T", bound="AdvisorySiemensSubSubBranch")


@_attrs_define
class AdvisorySiemensSubSubBranch:
    """
    Attributes:
        category (Union[Unset, str]):
        name (Union[Unset, str]):
        product (Union[Unset, AdvisorySiemensProduct]):
    """

    category: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    product: Union[Unset, "AdvisorySiemensProduct"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        name = self.name

        product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_siemens_product import AdvisorySiemensProduct

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, AdvisorySiemensProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AdvisorySiemensProduct.from_dict(_product)

        advisory_siemens_sub_sub_branch = cls(
            category=category,
            name=name,
            product=product,
        )

        advisory_siemens_sub_sub_branch.additional_properties = d
        return advisory_siemens_sub_sub_branch

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
