from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMCvssV20")


@_attrs_define
class AdvisoryMCvssV20:
    """
    Attributes:
        access_vector (Union[Unset, str]):
        attack_complexity (Union[Unset, str]):
        authentication (Union[Unset, str]):
        availability_impact (Union[Unset, str]):
        base_score (Union[Unset, float]):
        confidentiality_impact (Union[Unset, str]):
        integrity_impact (Union[Unset, str]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    access_vector: Union[Unset, str] = UNSET
    attack_complexity: Union[Unset, str] = UNSET
    authentication: Union[Unset, str] = UNSET
    availability_impact: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    confidentiality_impact: Union[Unset, str] = UNSET
    integrity_impact: Union[Unset, str] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_vector = self.access_vector

        attack_complexity = self.attack_complexity

        authentication = self.authentication

        availability_impact = self.availability_impact

        base_score = self.base_score

        confidentiality_impact = self.confidentiality_impact

        integrity_impact = self.integrity_impact

        vector_string = self.vector_string

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_vector is not UNSET:
            field_dict["accessVector"] = access_vector
        if attack_complexity is not UNSET:
            field_dict["attackComplexity"] = attack_complexity
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if availability_impact is not UNSET:
            field_dict["availabilityImpact"] = availability_impact
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if confidentiality_impact is not UNSET:
            field_dict["confidentialityImpact"] = confidentiality_impact
        if integrity_impact is not UNSET:
            field_dict["integrityImpact"] = integrity_impact
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_vector = d.pop("accessVector", UNSET)

        attack_complexity = d.pop("attackComplexity", UNSET)

        authentication = d.pop("authentication", UNSET)

        availability_impact = d.pop("availabilityImpact", UNSET)

        base_score = d.pop("baseScore", UNSET)

        confidentiality_impact = d.pop("confidentialityImpact", UNSET)

        integrity_impact = d.pop("integrityImpact", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        advisory_m_cvss_v20 = cls(
            access_vector=access_vector,
            attack_complexity=attack_complexity,
            authentication=authentication,
            availability_impact=availability_impact,
            base_score=base_score,
            confidentiality_impact=confidentiality_impact,
            integrity_impact=integrity_impact,
            vector_string=vector_string,
            version=version,
        )

        advisory_m_cvss_v20.additional_properties = d
        return advisory_m_cvss_v20

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
