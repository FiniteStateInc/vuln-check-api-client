from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNVDCPEDictionary")


@_attrs_define
class AdvisoryNVDCPEDictionary:
    """
    Attributes:
        backup_only (Union[Unset, str]):
    """

    backup_only: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_only = self.backup_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_only is not UNSET:
            field_dict["backupOnly"] = backup_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_only = d.pop("backupOnly", UNSET)

        advisory_nvdcpe_dictionary = cls(
            backup_only=backup_only,
        )

        advisory_nvdcpe_dictionary.additional_properties = d
        return advisory_nvdcpe_dictionary

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
