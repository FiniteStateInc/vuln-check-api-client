from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCISControl")


@_attrs_define
class AdvisoryCISControl:
    """
    Attributes:
        cis_control_description (Union[Unset, str]):
        cis_control_id (Union[Unset, str]):
        cis_control_name (Union[Unset, str]):
    """

    cis_control_description: Union[Unset, str] = UNSET
    cis_control_id: Union[Unset, str] = UNSET
    cis_control_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cis_control_description = self.cis_control_description

        cis_control_id = self.cis_control_id

        cis_control_name = self.cis_control_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cis_control_description is not UNSET:
            field_dict["cis_control_description"] = cis_control_description
        if cis_control_id is not UNSET:
            field_dict["cis_control_id"] = cis_control_id
        if cis_control_name is not UNSET:
            field_dict["cis_control_name"] = cis_control_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cis_control_description = d.pop("cis_control_description", UNSET)

        cis_control_id = d.pop("cis_control_id", UNSET)

        cis_control_name = d.pop("cis_control_name", UNSET)

        advisory_cis_control = cls(
            cis_control_description=cis_control_description,
            cis_control_id=cis_control_id,
            cis_control_name=cis_control_name,
        )

        advisory_cis_control.additional_properties = d
        return advisory_cis_control

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
