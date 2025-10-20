from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryDistroVersion")


@_attrs_define
class AdvisoryDistroVersion:
    """
    Attributes:
        arch (Union[Unset, str]):
        published_date (Union[Unset, str]):
        release (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    arch: Union[Unset, str] = UNSET
    published_date: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch = self.arch

        published_date = self.published_date

        release = self.release

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if published_date is not UNSET:
            field_dict["published_date"] = published_date
        if release is not UNSET:
            field_dict["release"] = release
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arch = d.pop("arch", UNSET)

        published_date = d.pop("published_date", UNSET)

        release = d.pop("release", UNSET)

        version = d.pop("version", UNSET)

        advisory_distro_version = cls(
            arch=arch,
            published_date=published_date,
            release=release,
            version=version,
        )

        advisory_distro_version.additional_properties = d
        return advisory_distro_version

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
