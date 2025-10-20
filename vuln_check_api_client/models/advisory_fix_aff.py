from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryFixAff")


@_attrs_define
class AdvisoryFixAff:
    """
    Attributes:
        affected_since (Union[Unset, str]):
        fixed_version (Union[Unset, str]):
        patch_url (Union[Unset, str]):
    """

    affected_since: Union[Unset, str] = UNSET
    fixed_version: Union[Unset, str] = UNSET
    patch_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_since = self.affected_since

        fixed_version = self.fixed_version

        patch_url = self.patch_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_since is not UNSET:
            field_dict["affected_since"] = affected_since
        if fixed_version is not UNSET:
            field_dict["fixed_version"] = fixed_version
        if patch_url is not UNSET:
            field_dict["patch_url"] = patch_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_since = d.pop("affected_since", UNSET)

        fixed_version = d.pop("fixed_version", UNSET)

        patch_url = d.pop("patch_url", UNSET)

        advisory_fix_aff = cls(
            affected_since=affected_since,
            fixed_version=fixed_version,
            patch_url=patch_url,
        )

        advisory_fix_aff.additional_properties = d
        return advisory_fix_aff

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
