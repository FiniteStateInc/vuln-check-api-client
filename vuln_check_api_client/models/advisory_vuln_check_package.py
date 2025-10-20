from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVulnCheckPackage")


@_attrs_define
class AdvisoryVulnCheckPackage:
    """
    Attributes:
        arch (Union[Unset, str]):
        distro (Union[Unset, str]):
        filename (Union[Unset, str]):
        md5 (Union[Unset, str]):
        name (Union[Unset, str]):
        purl (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    arch: Union[Unset, str] = UNSET
    distro: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    md5: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    purl: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch = self.arch

        distro = self.distro

        filename = self.filename

        md5 = self.md5

        name = self.name

        purl = self.purl

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if distro is not UNSET:
            field_dict["distro"] = distro
        if filename is not UNSET:
            field_dict["filename"] = filename
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if name is not UNSET:
            field_dict["name"] = name
        if purl is not UNSET:
            field_dict["purl"] = purl
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arch = d.pop("arch", UNSET)

        distro = d.pop("distro", UNSET)

        filename = d.pop("filename", UNSET)

        md5 = d.pop("md5", UNSET)

        name = d.pop("name", UNSET)

        purl = d.pop("purl", UNSET)

        version = d.pop("version", UNSET)

        advisory_vuln_check_package = cls(
            arch=arch,
            distro=distro,
            filename=filename,
            md5=md5,
            name=name,
            purl=purl,
            version=version,
        )

        advisory_vuln_check_package.additional_properties = d
        return advisory_vuln_check_package

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
