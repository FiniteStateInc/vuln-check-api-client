from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMitreAttackTechnique")


@_attrs_define
class AdvisoryMitreAttackTechnique:
    """
    Attributes:
        sub_technique (Union[Unset, str]):
        sub_technique_name (Union[Unset, str]):
        tactic (Union[Unset, list[str]]):
        technique_id (Union[Unset, str]):
        technique_name (Union[Unset, str]):
    """

    sub_technique: Union[Unset, str] = UNSET
    sub_technique_name: Union[Unset, str] = UNSET
    tactic: Union[Unset, list[str]] = UNSET
    technique_id: Union[Unset, str] = UNSET
    technique_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_technique = self.sub_technique

        sub_technique_name = self.sub_technique_name

        tactic: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tactic, Unset):
            tactic = self.tactic

        technique_id = self.technique_id

        technique_name = self.technique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_technique is not UNSET:
            field_dict["sub_technique"] = sub_technique
        if sub_technique_name is not UNSET:
            field_dict["sub_technique_name"] = sub_technique_name
        if tactic is not UNSET:
            field_dict["tactic"] = tactic
        if technique_id is not UNSET:
            field_dict["technique_id"] = technique_id
        if technique_name is not UNSET:
            field_dict["technique_name"] = technique_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_technique = d.pop("sub_technique", UNSET)

        sub_technique_name = d.pop("sub_technique_name", UNSET)

        tactic = cast(list[str], d.pop("tactic", UNSET))

        technique_id = d.pop("technique_id", UNSET)

        technique_name = d.pop("technique_name", UNSET)

        advisory_mitre_attack_technique = cls(
            sub_technique=sub_technique,
            sub_technique_name=sub_technique_name,
            tactic=tactic,
            technique_id=technique_id,
            technique_name=technique_name,
        )

        advisory_mitre_attack_technique.additional_properties = d
        return advisory_mitre_attack_technique

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
