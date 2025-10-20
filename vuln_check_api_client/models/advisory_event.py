from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEvent")


@_attrs_define
class AdvisoryEvent:
    """
    Attributes:
        fixed (Union[Unset, str]):
        introduced (Union[Unset, str]):
        last_affected (Union[Unset, str]):
        limit (Union[Unset, str]):
    """

    fixed: Union[Unset, str] = UNSET
    introduced: Union[Unset, str] = UNSET
    last_affected: Union[Unset, str] = UNSET
    limit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed = self.fixed

        introduced = self.introduced

        last_affected = self.last_affected

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if introduced is not UNSET:
            field_dict["introduced"] = introduced
        if last_affected is not UNSET:
            field_dict["last_affected"] = last_affected
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixed = d.pop("fixed", UNSET)

        introduced = d.pop("introduced", UNSET)

        last_affected = d.pop("last_affected", UNSET)

        limit = d.pop("limit", UNSET)

        advisory_event = cls(
            fixed=fixed,
            introduced=introduced,
            last_affected=last_affected,
            limit=limit,
        )

        advisory_event.additional_properties = d
        return advisory_event

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
