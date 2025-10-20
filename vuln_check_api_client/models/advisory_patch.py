from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPatch")


@_attrs_define
class AdvisoryPatch:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        component (Union[Unset, str]):
        link (Union[Unset, str]):
        os_sw (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    component: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    os_sw: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        component = self.component

        link = self.link

        os_sw = self.os_sw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if component is not UNSET:
            field_dict["component"] = component
        if link is not UNSET:
            field_dict["link"] = link
        if os_sw is not UNSET:
            field_dict["os_sw"] = os_sw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        component = d.pop("component", UNSET)

        link = d.pop("link", UNSET)

        os_sw = d.pop("os_sw", UNSET)

        advisory_patch = cls(
            advisory_id=advisory_id,
            component=component,
            link=link,
            os_sw=os_sw,
        )

        advisory_patch.additional_properties = d
        return advisory_patch

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
