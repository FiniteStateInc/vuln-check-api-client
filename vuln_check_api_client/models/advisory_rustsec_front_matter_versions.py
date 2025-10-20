from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRustsecFrontMatterVersions")


@_attrs_define
class AdvisoryRustsecFrontMatterVersions:
    """
    Attributes:
        patched (Union[Unset, list[str]]):
        unaffected (Union[Unset, list[str]]): Versions which were never vulnerable (optional)
    """

    patched: Union[Unset, list[str]] = UNSET
    unaffected: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        patched: Union[Unset, list[str]] = UNSET
        if not isinstance(self.patched, Unset):
            patched = self.patched

        unaffected: Union[Unset, list[str]] = UNSET
        if not isinstance(self.unaffected, Unset):
            unaffected = self.unaffected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patched is not UNSET:
            field_dict["patched"] = patched
        if unaffected is not UNSET:
            field_dict["unaffected"] = unaffected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        patched = cast(list[str], d.pop("patched", UNSET))

        unaffected = cast(list[str], d.pop("unaffected", UNSET))

        advisory_rustsec_front_matter_versions = cls(
            patched=patched,
            unaffected=unaffected,
        )

        advisory_rustsec_front_matter_versions.additional_properties = d
        return advisory_rustsec_front_matter_versions

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
