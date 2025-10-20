from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAlmaPackage")


@_attrs_define
class AdvisoryAlmaPackage:
    """
    Attributes:
        arch (Union[Unset, str]):
        epoch (Union[Unset, str]):
        filename (Union[Unset, str]):
        name (Union[Unset, str]):
        reboot_suggested (Union[Unset, int]):
        release (Union[Unset, str]):
        source (Union[Unset, str]):
        sum_ (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    arch: Union[Unset, str] = UNSET
    epoch: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    reboot_suggested: Union[Unset, int] = UNSET
    release: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    sum_: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arch = self.arch

        epoch = self.epoch

        filename = self.filename

        name = self.name

        reboot_suggested = self.reboot_suggested

        release = self.release

        source = self.source

        sum_ = self.sum_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arch is not UNSET:
            field_dict["arch"] = arch
        if epoch is not UNSET:
            field_dict["epoch"] = epoch
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name
        if reboot_suggested is not UNSET:
            field_dict["reboot_suggested"] = reboot_suggested
        if release is not UNSET:
            field_dict["release"] = release
        if source is not UNSET:
            field_dict["source"] = source
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arch = d.pop("arch", UNSET)

        epoch = d.pop("epoch", UNSET)

        filename = d.pop("filename", UNSET)

        name = d.pop("name", UNSET)

        reboot_suggested = d.pop("reboot_suggested", UNSET)

        release = d.pop("release", UNSET)

        source = d.pop("source", UNSET)

        sum_ = d.pop("sum", UNSET)

        version = d.pop("version", UNSET)

        advisory_alma_package = cls(
            arch=arch,
            epoch=epoch,
            filename=filename,
            name=name,
            reboot_suggested=reboot_suggested,
            release=release,
            source=source,
            sum_=sum_,
            version=version,
        )

        advisory_alma_package.additional_properties = d
        return advisory_alma_package

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
