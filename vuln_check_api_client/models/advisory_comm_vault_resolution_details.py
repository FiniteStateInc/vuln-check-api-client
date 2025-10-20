from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCommVaultResolutionDetails")


@_attrs_define
class AdvisoryCommVaultResolutionDetails:
    """
    Attributes:
        feature_release (Union[Unset, str]):
        maintenance_release (Union[Unset, str]):
    """

    feature_release: Union[Unset, str] = UNSET
    maintenance_release: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_release = self.feature_release

        maintenance_release = self.maintenance_release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_release is not UNSET:
            field_dict["feature_release"] = feature_release
        if maintenance_release is not UNSET:
            field_dict["maintenance_release"] = maintenance_release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature_release = d.pop("feature_release", UNSET)

        maintenance_release = d.pop("maintenance_release", UNSET)

        advisory_comm_vault_resolution_details = cls(
            feature_release=feature_release,
            maintenance_release=maintenance_release,
        )

        advisory_comm_vault_resolution_details.additional_properties = d
        return advisory_comm_vault_resolution_details

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
