from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRockyFix")


@_attrs_define
class AdvisoryRockyFix:
    """
    Attributes:
        description (Union[Unset, str]):
        source_by (Union[Unset, str]):
        source_link (Union[Unset, str]):
        ticket (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    source_by: Union[Unset, str] = UNSET
    source_link: Union[Unset, str] = UNSET
    ticket: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        source_by = self.source_by

        source_link = self.source_link

        ticket = self.ticket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if source_by is not UNSET:
            field_dict["sourceBy"] = source_by
        if source_link is not UNSET:
            field_dict["sourceLink"] = source_link
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        source_by = d.pop("sourceBy", UNSET)

        source_link = d.pop("sourceLink", UNSET)

        ticket = d.pop("ticket", UNSET)

        advisory_rocky_fix = cls(
            description=description,
            source_by=source_by,
            source_link=source_link,
            ticket=ticket,
        )

        advisory_rocky_fix.additional_properties = d
        return advisory_rocky_fix

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
