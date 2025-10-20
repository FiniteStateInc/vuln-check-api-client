from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryFlag")


@_attrs_define
class AdvisoryFlag:
    """
    Attributes:
        date (Union[Unset, str]):
        group_ids (Union[Unset, list[str]]):
        label (Union[Unset, str]):
        product_ids (Union[Unset, list[str]]):
    """

    date: Union[Unset, str] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    label: Union[Unset, str] = UNSET
    product_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        label = self.label

        product_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if label is not UNSET:
            field_dict["label"] = label
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        label = d.pop("label", UNSET)

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        advisory_flag = cls(
            date=date,
            group_ids=group_ids,
            label=label,
            product_ids=product_ids,
        )

        advisory_flag.additional_properties = d
        return advisory_flag

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
