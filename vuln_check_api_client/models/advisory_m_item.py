from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMItem")


@_attrs_define
class AdvisoryMItem:
    """
    Attributes:
        items (Union[Unset, list['AdvisoryMItem']]):
        name (Union[Unset, str]):
        product_id (Union[Unset, str]):
        type_ (Union[Unset, int]): diff
        value (Union[Unset, str]):
    """

    items: Union[Unset, list["AdvisoryMItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        name = self.name

        product_id = self.product_id

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if name is not UNSET:
            field_dict["Name"] = name
        if product_id is not UNSET:
            field_dict["ProductID"] = product_id
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = AdvisoryMItem.from_dict(items_item_data)

            items.append(items_item)

        name = d.pop("Name", UNSET)

        product_id = d.pop("ProductID", UNSET)

        type_ = d.pop("Type", UNSET)

        value = d.pop("Value", UNSET)

        advisory_m_item = cls(
            items=items,
            name=name,
            product_id=product_id,
            type_=type_,
            value=value,
        )

        advisory_m_item.additional_properties = d
        return advisory_m_item

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
