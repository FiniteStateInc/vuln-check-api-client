from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCommVaultImpactedProductDetails")


@_attrs_define
class AdvisoryCommVaultImpactedProductDetails:
    """
    Attributes:
        affected_versions (Union[Unset, str]):
        platforms (Union[Unset, list[str]]):
        product_name (Union[Unset, str]):
        resolved_versions (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    affected_versions: Union[Unset, str] = UNSET
    platforms: Union[Unset, list[str]] = UNSET
    product_name: Union[Unset, str] = UNSET
    resolved_versions: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_versions = self.affected_versions

        platforms: Union[Unset, list[str]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = self.platforms

        product_name = self.product_name

        resolved_versions = self.resolved_versions

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_versions is not UNSET:
            field_dict["affected_versions"] = affected_versions
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if resolved_versions is not UNSET:
            field_dict["resolved_versions"] = resolved_versions
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_versions = d.pop("affected_versions", UNSET)

        platforms = cast(list[str], d.pop("platforms", UNSET))

        product_name = d.pop("product_name", UNSET)

        resolved_versions = d.pop("resolved_versions", UNSET)

        status = d.pop("status", UNSET)

        advisory_comm_vault_impacted_product_details = cls(
            affected_versions=affected_versions,
            platforms=platforms,
            product_name=product_name,
            resolved_versions=resolved_versions,
            status=status,
        )

        advisory_comm_vault_impacted_product_details.additional_properties = d
        return advisory_comm_vault_impacted_product_details

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
