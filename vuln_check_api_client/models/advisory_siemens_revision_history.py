from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySiemensRevisionHistory")


@_attrs_define
class AdvisorySiemensRevisionHistory:
    """
    Attributes:
        date (Union[Unset, str]):
        legacy_version (Union[Unset, str]):
        number (Union[Unset, str]):
        summary (Union[Unset, str]):
    """

    date: Union[Unset, str] = UNSET
    legacy_version: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        legacy_version = self.legacy_version

        number = self.number

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if legacy_version is not UNSET:
            field_dict["legacy_version"] = legacy_version
        if number is not UNSET:
            field_dict["number"] = number
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        legacy_version = d.pop("legacy_version", UNSET)

        number = d.pop("number", UNSET)

        summary = d.pop("summary", UNSET)

        advisory_siemens_revision_history = cls(
            date=date,
            legacy_version=legacy_version,
            number=number,
            summary=summary,
        )

        advisory_siemens_revision_history.additional_properties = d
        return advisory_siemens_revision_history

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
