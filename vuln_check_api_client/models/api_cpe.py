from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCPE")


@_attrs_define
class ApiCPE:
    """
    Attributes:
        edition (Union[Unset, str]):
        language (Union[Unset, str]):
        other (Union[Unset, str]):
        part (Union[Unset, str]):
        product (Union[Unset, str]):
        sw_edition (Union[Unset, str]):
        target_hw (Union[Unset, str]):
        target_sw (Union[Unset, str]):
        update (Union[Unset, str]):
        vendor (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    edition: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    other: Union[Unset, str] = UNSET
    part: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    sw_edition: Union[Unset, str] = UNSET
    target_hw: Union[Unset, str] = UNSET
    target_sw: Union[Unset, str] = UNSET
    update: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edition = self.edition

        language = self.language

        other = self.other

        part = self.part

        product = self.product

        sw_edition = self.sw_edition

        target_hw = self.target_hw

        target_sw = self.target_sw

        update = self.update

        vendor = self.vendor

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edition is not UNSET:
            field_dict["edition"] = edition
        if language is not UNSET:
            field_dict["language"] = language
        if other is not UNSET:
            field_dict["other"] = other
        if part is not UNSET:
            field_dict["part"] = part
        if product is not UNSET:
            field_dict["product"] = product
        if sw_edition is not UNSET:
            field_dict["sw_edition"] = sw_edition
        if target_hw is not UNSET:
            field_dict["target_hw"] = target_hw
        if target_sw is not UNSET:
            field_dict["target_sw"] = target_sw
        if update is not UNSET:
            field_dict["update"] = update
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edition = d.pop("edition", UNSET)

        language = d.pop("language", UNSET)

        other = d.pop("other", UNSET)

        part = d.pop("part", UNSET)

        product = d.pop("product", UNSET)

        sw_edition = d.pop("sw_edition", UNSET)

        target_hw = d.pop("target_hw", UNSET)

        target_sw = d.pop("target_sw", UNSET)

        update = d.pop("update", UNSET)

        vendor = d.pop("vendor", UNSET)

        version = d.pop("version", UNSET)

        api_cpe = cls(
            edition=edition,
            language=language,
            other=other,
            part=part,
            product=product,
            sw_edition=sw_edition,
            target_hw=target_hw,
            target_sw=target_sw,
            update=update,
            vendor=vendor,
            version=version,
        )

        api_cpe.additional_properties = d
        return api_cpe

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
