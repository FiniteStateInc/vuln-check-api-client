from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVendorRef")


@_attrs_define
class AdvisoryVendorRef:
    """
    Attributes:
        vendor_ref (Union[Unset, str]):
        vendor_ref_url (Union[Unset, str]):
    """

    vendor_ref: Union[Unset, str] = UNSET
    vendor_ref_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_ref = self.vendor_ref

        vendor_ref_url = self.vendor_ref_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendor_ref is not UNSET:
            field_dict["vendor_ref"] = vendor_ref
        if vendor_ref_url is not UNSET:
            field_dict["vendor_ref_url"] = vendor_ref_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vendor_ref = d.pop("vendor_ref", UNSET)

        vendor_ref_url = d.pop("vendor_ref_url", UNSET)

        advisory_vendor_ref = cls(
            vendor_ref=vendor_ref,
            vendor_ref_url=vendor_ref_url,
        )

        advisory_vendor_ref.additional_properties = d
        return advisory_vendor_ref

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
