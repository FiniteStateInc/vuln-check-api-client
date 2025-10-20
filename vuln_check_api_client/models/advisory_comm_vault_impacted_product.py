from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_comm_vault_impacted_product_details import AdvisoryCommVaultImpactedProductDetails


T = TypeVar("T", bound="AdvisoryCommVaultImpactedProduct")


@_attrs_define
class AdvisoryCommVaultImpactedProduct:
    """
    Attributes:
        description (Union[Unset, str]):
        impacted_product_details (Union[Unset, list['AdvisoryCommVaultImpactedProductDetails']]):
    """

    description: Union[Unset, str] = UNSET
    impacted_product_details: Union[Unset, list["AdvisoryCommVaultImpactedProductDetails"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        impacted_product_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.impacted_product_details, Unset):
            impacted_product_details = []
            for impacted_product_details_item_data in self.impacted_product_details:
                impacted_product_details_item = impacted_product_details_item_data.to_dict()
                impacted_product_details.append(impacted_product_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if impacted_product_details is not UNSET:
            field_dict["impacted_product_details"] = impacted_product_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_comm_vault_impacted_product_details import AdvisoryCommVaultImpactedProductDetails

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        impacted_product_details = []
        _impacted_product_details = d.pop("impacted_product_details", UNSET)
        for impacted_product_details_item_data in _impacted_product_details or []:
            impacted_product_details_item = AdvisoryCommVaultImpactedProductDetails.from_dict(
                impacted_product_details_item_data
            )

            impacted_product_details.append(impacted_product_details_item)

        advisory_comm_vault_impacted_product = cls(
            description=description,
            impacted_product_details=impacted_product_details,
        )

        advisory_comm_vault_impacted_product.additional_properties = d
        return advisory_comm_vault_impacted_product

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
