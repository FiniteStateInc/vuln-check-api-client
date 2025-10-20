from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEcoSystem")


@_attrs_define
class AdvisoryEcoSystem:
    """
    Attributes:
        severity (Union[Unset, str]):
        spl (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    severity: Union[Unset, str] = UNSET
    spl: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity

        spl = self.spl

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if spl is not UNSET:
            field_dict["spl"] = spl
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        severity = d.pop("severity", UNSET)

        spl = d.pop("spl", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_eco_system = cls(
            severity=severity,
            spl=spl,
            type_=type_,
        )

        advisory_eco_system.additional_properties = d
        return advisory_eco_system

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
