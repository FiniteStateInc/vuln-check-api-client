from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySiemensAcknowledgments")


@_attrs_define
class AdvisorySiemensAcknowledgments:
    """
    Attributes:
        names (Union[Unset, list[str]]):
        organization (Union[Unset, str]):
        summary (Union[Unset, str]):
    """

    names: Union[Unset, list[str]] = UNSET
    organization: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        organization = self.organization

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if names is not UNSET:
            field_dict["names"] = names
        if organization is not UNSET:
            field_dict["organization"] = organization
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        names = cast(list[str], d.pop("names", UNSET))

        organization = d.pop("organization", UNSET)

        summary = d.pop("summary", UNSET)

        advisory_siemens_acknowledgments = cls(
            names=names,
            organization=organization,
            summary=summary,
        )

        advisory_siemens_acknowledgments.additional_properties = d
        return advisory_siemens_acknowledgments

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
