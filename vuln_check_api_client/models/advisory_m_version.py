from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMVersion")


@_attrs_define
class AdvisoryMVersion:
    """
    Attributes:
        less_than (Union[Unset, str]):
        less_than_or_equal (Union[Unset, str]):
        status (Union[Unset, str]):
        version (Union[Unset, str]):
        version_type (Union[Unset, str]):
    """

    less_than: Union[Unset, str] = UNSET
    less_than_or_equal: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    version_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        less_than = self.less_than

        less_than_or_equal = self.less_than_or_equal

        status = self.status

        version = self.version

        version_type = self.version_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if less_than is not UNSET:
            field_dict["lessThan"] = less_than
        if less_than_or_equal is not UNSET:
            field_dict["lessThanOrEqual"] = less_than_or_equal
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if version_type is not UNSET:
            field_dict["versionType"] = version_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        less_than = d.pop("lessThan", UNSET)

        less_than_or_equal = d.pop("lessThanOrEqual", UNSET)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        version_type = d.pop("versionType", UNSET)

        advisory_m_version = cls(
            less_than=less_than,
            less_than_or_equal=less_than_or_equal,
            status=status,
            version=version,
            version_type=version_type,
        )

        advisory_m_version.additional_properties = d
        return advisory_m_version

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
