from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryKbThreatDescription")


@_attrs_define
class AdvisoryKbThreatDescription:
    """
    Attributes:
        dos (Union[Unset, str]):
        exploited (Union[Unset, str]):
        latest_software_release (Union[Unset, str]):
        level (Union[Unset, list[str]]):
        older_software_release (Union[Unset, str]):
        publicly_disclosed (Union[Unset, str]):
        type_ (Union[Unset, list[str]]):
    """

    dos: Union[Unset, str] = UNSET
    exploited: Union[Unset, str] = UNSET
    latest_software_release: Union[Unset, str] = UNSET
    level: Union[Unset, list[str]] = UNSET
    older_software_release: Union[Unset, str] = UNSET
    publicly_disclosed: Union[Unset, str] = UNSET
    type_: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dos = self.dos

        exploited = self.exploited

        latest_software_release = self.latest_software_release

        level: Union[Unset, list[str]] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level

        older_software_release = self.older_software_release

        publicly_disclosed = self.publicly_disclosed

        type_: Union[Unset, list[str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dos is not UNSET:
            field_dict["dos"] = dos
        if exploited is not UNSET:
            field_dict["exploited"] = exploited
        if latest_software_release is not UNSET:
            field_dict["latest_software_release"] = latest_software_release
        if level is not UNSET:
            field_dict["level"] = level
        if older_software_release is not UNSET:
            field_dict["older_software_release"] = older_software_release
        if publicly_disclosed is not UNSET:
            field_dict["publicly_disclosed"] = publicly_disclosed
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dos = d.pop("dos", UNSET)

        exploited = d.pop("exploited", UNSET)

        latest_software_release = d.pop("latest_software_release", UNSET)

        level = cast(list[str], d.pop("level", UNSET))

        older_software_release = d.pop("older_software_release", UNSET)

        publicly_disclosed = d.pop("publicly_disclosed", UNSET)

        type_ = cast(list[str], d.pop("type", UNSET))

        advisory_kb_threat_description = cls(
            dos=dos,
            exploited=exploited,
            latest_software_release=latest_software_release,
            level=level,
            older_software_release=older_software_release,
            publicly_disclosed=publicly_disclosed,
            type_=type_,
        )

        advisory_kb_threat_description.additional_properties = d
        return advisory_kb_threat_description

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
