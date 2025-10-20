from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAppleComponent")


@_attrs_define
class AdvisoryAppleComponent:
    """
    Attributes:
        available_for (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        description (Union[Unset, str]):
        impact (Union[Unset, str]):
        itw_exploit (Union[Unset, bool]):
        name (Union[Unset, str]):
    """

    available_for: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    itw_exploit: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_for = self.available_for

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        description = self.description

        impact = self.impact

        itw_exploit = self.itw_exploit

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_for is not UNSET:
            field_dict["available_for"] = available_for
        if cve is not UNSET:
            field_dict["cve"] = cve
        if description is not UNSET:
            field_dict["description"] = description
        if impact is not UNSET:
            field_dict["impact"] = impact
        if itw_exploit is not UNSET:
            field_dict["itw_exploit"] = itw_exploit
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_for = d.pop("available_for", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        description = d.pop("description", UNSET)

        impact = d.pop("impact", UNSET)

        itw_exploit = d.pop("itw_exploit", UNSET)

        name = d.pop("name", UNSET)

        advisory_apple_component = cls(
            available_for=available_for,
            cve=cve,
            description=description,
            impact=impact,
            itw_exploit=itw_exploit,
            name=name,
        )

        advisory_apple_component.additional_properties = d
        return advisory_apple_component

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
