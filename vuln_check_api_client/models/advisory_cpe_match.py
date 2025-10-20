from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCPEMatch")


@_attrs_define
class AdvisoryCPEMatch:
    """
    Attributes:
        criteria (Union[Unset, str]):
        match_criteria_id (Union[Unset, str]):
        vulnerable (Union[Unset, bool]):
    """

    criteria: Union[Unset, str] = UNSET
    match_criteria_id: Union[Unset, str] = UNSET
    vulnerable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria

        match_criteria_id = self.match_criteria_id

        vulnerable = self.vulnerable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if match_criteria_id is not UNSET:
            field_dict["matchCriteriaId"] = match_criteria_id
        if vulnerable is not UNSET:
            field_dict["vulnerable"] = vulnerable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criteria = d.pop("criteria", UNSET)

        match_criteria_id = d.pop("matchCriteriaId", UNSET)

        vulnerable = d.pop("vulnerable", UNSET)

        advisory_cpe_match = cls(
            criteria=criteria,
            match_criteria_id=match_criteria_id,
            vulnerable=vulnerable,
        )

        advisory_cpe_match.additional_properties = d
        return advisory_cpe_match

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
