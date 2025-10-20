from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_identification_helper import AdvisoryIdentificationHelper


T = TypeVar("T", bound="AdvisoryProduct")


@_attrs_define
class AdvisoryProduct:
    """
    Attributes:
        name (Union[Unset, str]):
        product_id (Union[Unset, str]):
        product_identification_helper (Union[Unset, AdvisoryIdentificationHelper]):
    """

    name: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    product_identification_helper: Union[Unset, "AdvisoryIdentificationHelper"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        product_id = self.product_id

        product_identification_helper: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_identification_helper, Unset):
            product_identification_helper = self.product_identification_helper.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_identification_helper is not UNSET:
            field_dict["product_identification_helper"] = product_identification_helper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_identification_helper import AdvisoryIdentificationHelper

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        product_id = d.pop("product_id", UNSET)

        _product_identification_helper = d.pop("product_identification_helper", UNSET)
        product_identification_helper: Union[Unset, AdvisoryIdentificationHelper]
        if isinstance(_product_identification_helper, Unset):
            product_identification_helper = UNSET
        else:
            product_identification_helper = AdvisoryIdentificationHelper.from_dict(_product_identification_helper)

        advisory_product = cls(
            name=name,
            product_id=product_id,
            product_identification_helper=product_identification_helper,
        )

        advisory_product.additional_properties = d
        return advisory_product

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
