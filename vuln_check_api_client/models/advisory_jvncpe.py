from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryJVNCPE")


@_attrs_define
class AdvisoryJVNCPE:
    """
    Attributes:
        cpe (Union[Unset, str]):
        product (Union[Unset, str]):
        vendor (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    cpe: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe = self.cpe

        product = self.product

        vendor = self.vendor

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if product is not UNSET:
            field_dict["product"] = product
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpe = d.pop("cpe", UNSET)

        product = d.pop("product", UNSET)

        vendor = d.pop("vendor", UNSET)

        version = d.pop("version", UNSET)

        advisory_jvncpe = cls(
            cpe=cpe,
            product=product,
            vendor=vendor,
            version=version,
        )

        advisory_jvncpe.additional_properties = d
        return advisory_jvncpe

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
