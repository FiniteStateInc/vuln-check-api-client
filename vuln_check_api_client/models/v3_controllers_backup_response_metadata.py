from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="V3ControllersBackupResponseMetadata")


@_attrs_define
class V3ControllersBackupResponseMetadata:
    """
    Attributes:
        index (Union[Unset, str]):
        timestamp (Union[Unset, str]):
    """

    index: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        v3_controllers_backup_response_metadata = cls(
            index=index,
            timestamp=timestamp,
        )

        v3_controllers_backup_response_metadata.additional_properties = d
        return v3_controllers_backup_response_metadata

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
