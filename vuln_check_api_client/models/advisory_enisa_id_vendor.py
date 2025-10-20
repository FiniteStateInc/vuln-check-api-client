from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEnisaIDVendor")


@_attrs_define
class AdvisoryEnisaIDVendor:
    """
    Attributes:
        id (Union[Unset, str]):
        vendor_name (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vendor_name = self.vendor_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if vendor_name is not UNSET:
            field_dict["vendor_name"] = vendor_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        vendor_name = d.pop("vendor_name", UNSET)

        advisory_enisa_id_vendor = cls(
            id=id,
            vendor_name=vendor_name,
        )

        advisory_enisa_id_vendor.additional_properties = d
        return advisory_enisa_id_vendor

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
