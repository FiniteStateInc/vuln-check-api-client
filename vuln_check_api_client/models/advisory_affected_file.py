from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAffectedFile")


@_attrs_define
class AdvisoryAffectedFile:
    """
    Attributes:
        file_last_modified (Union[Unset, str]):
        file_name (Union[Unset, str]):
    """

    file_last_modified: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_last_modified = self.file_last_modified

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_last_modified is not UNSET:
            field_dict["file_last_modified"] = file_last_modified
        if file_name is not UNSET:
            field_dict["file_name"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_last_modified = d.pop("file_last_modified", UNSET)

        file_name = d.pop("file_name", UNSET)

        advisory_affected_file = cls(
            file_last_modified=file_last_modified,
            file_name=file_name,
        )

        advisory_affected_file.additional_properties = d
        return advisory_affected_file

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
