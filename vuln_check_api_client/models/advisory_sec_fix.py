from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySecFix")


@_attrs_define
class AdvisorySecFix:
    """
    Attributes:
        arch (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        release (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    arch: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    release: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch = self.arch

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        release = self.release

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if cve is not UNSET:
            field_dict["cve"] = cve
        if release is not UNSET:
            field_dict["release"] = release
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arch = d.pop("arch", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        release = d.pop("release", UNSET)

        version = d.pop("version", UNSET)

        advisory_sec_fix = cls(
            arch=arch,
            cve=cve,
            release=release,
            version=version,
        )

        advisory_sec_fix.additional_properties = d
        return advisory_sec_fix

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
