from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVulnrichmentOption")


@_attrs_define
class AdvisoryVulnrichmentOption:
    """
    Attributes:
        automatable (Union[Unset, str]):
        exploitation (Union[Unset, str]):
        technical_impact (Union[Unset, str]):
    """

    automatable: Union[Unset, str] = UNSET
    exploitation: Union[Unset, str] = UNSET
    technical_impact: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automatable = self.automatable

        exploitation = self.exploitation

        technical_impact = self.technical_impact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatable is not UNSET:
            field_dict["Automatable"] = automatable
        if exploitation is not UNSET:
            field_dict["Exploitation"] = exploitation
        if technical_impact is not UNSET:
            field_dict["Technical Impact"] = technical_impact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automatable = d.pop("Automatable", UNSET)

        exploitation = d.pop("Exploitation", UNSET)

        technical_impact = d.pop("Technical Impact", UNSET)

        advisory_vulnrichment_option = cls(
            automatable=automatable,
            exploitation=exploitation,
            technical_impact=technical_impact,
        )

        advisory_vulnrichment_option.additional_properties = d
        return advisory_vulnrichment_option

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
