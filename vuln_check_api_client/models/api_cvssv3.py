from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCVSSV3")


@_attrs_define
class ApiCVSSV3:
    """
    Attributes:
        attack_complexity (Union[Unset, str]):
        attack_vector (Union[Unset, str]):
        availability_impact (Union[Unset, str]):
        base_score (Union[Unset, float]):
        base_severity (Union[Unset, str]):
        confidentiality_impact (Union[Unset, str]):
        integrity_impact (Union[Unset, str]):
        privileges_required (Union[Unset, str]):
        scope (Union[Unset, str]):
        user_interaction (Union[Unset, str]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    attack_complexity: Union[Unset, str] = UNSET
    attack_vector: Union[Unset, str] = UNSET
    availability_impact: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    base_severity: Union[Unset, str] = UNSET
    confidentiality_impact: Union[Unset, str] = UNSET
    integrity_impact: Union[Unset, str] = UNSET
    privileges_required: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    user_interaction: Union[Unset, str] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attack_complexity = self.attack_complexity

        attack_vector = self.attack_vector

        availability_impact = self.availability_impact

        base_score = self.base_score

        base_severity = self.base_severity

        confidentiality_impact = self.confidentiality_impact

        integrity_impact = self.integrity_impact

        privileges_required = self.privileges_required

        scope = self.scope

        user_interaction = self.user_interaction

        vector_string = self.vector_string

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attack_complexity is not UNSET:
            field_dict["attackComplexity"] = attack_complexity
        if attack_vector is not UNSET:
            field_dict["attackVector"] = attack_vector
        if availability_impact is not UNSET:
            field_dict["availabilityImpact"] = availability_impact
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if base_severity is not UNSET:
            field_dict["baseSeverity"] = base_severity
        if confidentiality_impact is not UNSET:
            field_dict["confidentialityImpact"] = confidentiality_impact
        if integrity_impact is not UNSET:
            field_dict["integrityImpact"] = integrity_impact
        if privileges_required is not UNSET:
            field_dict["privilegesRequired"] = privileges_required
        if scope is not UNSET:
            field_dict["scope"] = scope
        if user_interaction is not UNSET:
            field_dict["userInteraction"] = user_interaction
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attack_complexity = d.pop("attackComplexity", UNSET)

        attack_vector = d.pop("attackVector", UNSET)

        availability_impact = d.pop("availabilityImpact", UNSET)

        base_score = d.pop("baseScore", UNSET)

        base_severity = d.pop("baseSeverity", UNSET)

        confidentiality_impact = d.pop("confidentialityImpact", UNSET)

        integrity_impact = d.pop("integrityImpact", UNSET)

        privileges_required = d.pop("privilegesRequired", UNSET)

        scope = d.pop("scope", UNSET)

        user_interaction = d.pop("userInteraction", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        api_cvssv3 = cls(
            attack_complexity=attack_complexity,
            attack_vector=attack_vector,
            availability_impact=availability_impact,
            base_score=base_score,
            base_severity=base_severity,
            confidentiality_impact=confidentiality_impact,
            integrity_impact=integrity_impact,
            privileges_required=privileges_required,
            scope=scope,
            user_interaction=user_interaction,
            vector_string=vector_string,
            version=version,
        )

        api_cvssv3.additional_properties = d
        return api_cvssv3

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
