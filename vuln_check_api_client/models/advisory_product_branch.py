from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_csaf_relationship import AdvisoryCSAFRelationship
    from ..models.advisory_product import AdvisoryProduct


T = TypeVar("T", bound="AdvisoryProductBranch")


@_attrs_define
class AdvisoryProductBranch:
    """
    Attributes:
        branches (Union[Unset, list['AdvisoryProductBranch']]):
        category (Union[Unset, str]):
        name (Union[Unset, str]):
        product (Union[Unset, AdvisoryProduct]):
        relationships (Union[Unset, list['AdvisoryCSAFRelationship']]):
    """

    branches: Union[Unset, list["AdvisoryProductBranch"]] = UNSET
    category: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    product: Union[Unset, "AdvisoryProduct"] = UNSET
    relationships: Union[Unset, list["AdvisoryCSAFRelationship"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        category = self.category

        name = self.name

        product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branches is not UNSET:
            field_dict["branches"] = branches
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if product is not UNSET:
            field_dict["product"] = product
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_csaf_relationship import AdvisoryCSAFRelationship
        from ..models.advisory_product import AdvisoryProduct

        d = dict(src_dict)
        branches = []
        _branches = d.pop("branches", UNSET)
        for branches_item_data in _branches or []:
            branches_item = AdvisoryProductBranch.from_dict(branches_item_data)

            branches.append(branches_item)

        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, AdvisoryProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AdvisoryProduct.from_dict(_product)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = AdvisoryCSAFRelationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        advisory_product_branch = cls(
            branches=branches,
            category=category,
            name=name,
            product=product,
            relationships=relationships,
        )

        advisory_product_branch.additional_properties = d
        return advisory_product_branch

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
