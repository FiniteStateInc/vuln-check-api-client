from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBDUOs")


@_attrs_define
class AdvisoryBDUOs:
    """
    Attributes:
        name (Union[Unset, str]):
        platform (Union[Unset, str]):
        text (Union[Unset, str]):
        vendor (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        platform = self.platform

        text = self.text

        vendor = self.vendor

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if text is not UNSET:
            field_dict["text"] = text
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        platform = d.pop("platform", UNSET)

        text = d.pop("text", UNSET)

        vendor = d.pop("vendor", UNSET)

        version = d.pop("version", UNSET)

        advisory_bdu_os = cls(
            name=name,
            platform=platform,
            text=text,
            vendor=vendor,
            version=version,
        )

        advisory_bdu_os.additional_properties = d
        return advisory_bdu_os

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
