from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPackage")


@_attrs_define
class ApiPackage:
    """
    Attributes:
        filename (Union[Unset, str]):
        name (Union[Unset, str]): sort
        release (Union[Unset, str]):
        src (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    filename: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    src: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        name = self.name

        release = self.release

        src = self.src

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name
        if release is not UNSET:
            field_dict["release"] = release
        if src is not UNSET:
            field_dict["src"] = src
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename", UNSET)

        name = d.pop("name", UNSET)

        release = d.pop("release", UNSET)

        src = d.pop("src", UNSET)

        version = d.pop("version", UNSET)

        api_package = cls(
            filename=filename,
            name=name,
            release=release,
            src=src,
            version=version,
        )

        api_package.additional_properties = d
        return api_package

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
