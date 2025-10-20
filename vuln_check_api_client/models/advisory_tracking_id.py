from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryTrackingID")


@_attrs_define
class AdvisoryTrackingID:
    """
    Attributes:
        system_name (Union[Unset, str]):
        text (Union[Unset, str]):
    """

    system_name: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_name = self.system_name

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_name = d.pop("system_name", UNSET)

        text = d.pop("text", UNSET)

        advisory_tracking_id = cls(
            system_name=system_name,
            text=text,
        )

        advisory_tracking_id.additional_properties = d
        return advisory_tracking_id

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
