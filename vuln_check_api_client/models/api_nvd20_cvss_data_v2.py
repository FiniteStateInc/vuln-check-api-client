from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20CvssDataV2")


@_attrs_define
class ApiNVD20CvssDataV2:
    """
    Attributes:
        access_complexity (Union[Unset, str]):
        access_vector (Union[Unset, str]):
        authentication (Union[Unset, str]):
        availability_impact (Union[Unset, str]):
        availability_requirement (Union[Unset, str]):
        base_score (Union[Unset, float]):
        collateral_damage_potential (Union[Unset, str]):
        confidentiality_impact (Union[Unset, str]):
        confidentiality_requirement (Union[Unset, str]):
        environmental_score (Union[Unset, float]):
        exploitability (Union[Unset, str]):
        integrity_impact (Union[Unset, str]):
        integrity_requirement (Union[Unset, str]):
        remediation_level (Union[Unset, str]):
        report_confidence (Union[Unset, str]):
        target_distribution (Union[Unset, str]):
        temporal_score (Union[Unset, float]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    access_complexity: Union[Unset, str] = UNSET
    access_vector: Union[Unset, str] = UNSET
    authentication: Union[Unset, str] = UNSET
    availability_impact: Union[Unset, str] = UNSET
    availability_requirement: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    collateral_damage_potential: Union[Unset, str] = UNSET
    confidentiality_impact: Union[Unset, str] = UNSET
    confidentiality_requirement: Union[Unset, str] = UNSET
    environmental_score: Union[Unset, float] = UNSET
    exploitability: Union[Unset, str] = UNSET
    integrity_impact: Union[Unset, str] = UNSET
    integrity_requirement: Union[Unset, str] = UNSET
    remediation_level: Union[Unset, str] = UNSET
    report_confidence: Union[Unset, str] = UNSET
    target_distribution: Union[Unset, str] = UNSET
    temporal_score: Union[Unset, float] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_complexity = self.access_complexity

        access_vector = self.access_vector

        authentication = self.authentication

        availability_impact = self.availability_impact

        availability_requirement = self.availability_requirement

        base_score = self.base_score

        collateral_damage_potential = self.collateral_damage_potential

        confidentiality_impact = self.confidentiality_impact

        confidentiality_requirement = self.confidentiality_requirement

        environmental_score = self.environmental_score

        exploitability = self.exploitability

        integrity_impact = self.integrity_impact

        integrity_requirement = self.integrity_requirement

        remediation_level = self.remediation_level

        report_confidence = self.report_confidence

        target_distribution = self.target_distribution

        temporal_score = self.temporal_score

        vector_string = self.vector_string

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_complexity is not UNSET:
            field_dict["accessComplexity"] = access_complexity
        if access_vector is not UNSET:
            field_dict["accessVector"] = access_vector
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if availability_impact is not UNSET:
            field_dict["availabilityImpact"] = availability_impact
        if availability_requirement is not UNSET:
            field_dict["availabilityRequirement"] = availability_requirement
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if collateral_damage_potential is not UNSET:
            field_dict["collateralDamagePotential"] = collateral_damage_potential
        if confidentiality_impact is not UNSET:
            field_dict["confidentialityImpact"] = confidentiality_impact
        if confidentiality_requirement is not UNSET:
            field_dict["confidentialityRequirement"] = confidentiality_requirement
        if environmental_score is not UNSET:
            field_dict["environmentalScore"] = environmental_score
        if exploitability is not UNSET:
            field_dict["exploitability"] = exploitability
        if integrity_impact is not UNSET:
            field_dict["integrityImpact"] = integrity_impact
        if integrity_requirement is not UNSET:
            field_dict["integrityRequirement"] = integrity_requirement
        if remediation_level is not UNSET:
            field_dict["remediationLevel"] = remediation_level
        if report_confidence is not UNSET:
            field_dict["reportConfidence"] = report_confidence
        if target_distribution is not UNSET:
            field_dict["targetDistribution"] = target_distribution
        if temporal_score is not UNSET:
            field_dict["temporalScore"] = temporal_score
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_complexity = d.pop("accessComplexity", UNSET)

        access_vector = d.pop("accessVector", UNSET)

        authentication = d.pop("authentication", UNSET)

        availability_impact = d.pop("availabilityImpact", UNSET)

        availability_requirement = d.pop("availabilityRequirement", UNSET)

        base_score = d.pop("baseScore", UNSET)

        collateral_damage_potential = d.pop("collateralDamagePotential", UNSET)

        confidentiality_impact = d.pop("confidentialityImpact", UNSET)

        confidentiality_requirement = d.pop("confidentialityRequirement", UNSET)

        environmental_score = d.pop("environmentalScore", UNSET)

        exploitability = d.pop("exploitability", UNSET)

        integrity_impact = d.pop("integrityImpact", UNSET)

        integrity_requirement = d.pop("integrityRequirement", UNSET)

        remediation_level = d.pop("remediationLevel", UNSET)

        report_confidence = d.pop("reportConfidence", UNSET)

        target_distribution = d.pop("targetDistribution", UNSET)

        temporal_score = d.pop("temporalScore", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        api_nvd20_cvss_data_v2 = cls(
            access_complexity=access_complexity,
            access_vector=access_vector,
            authentication=authentication,
            availability_impact=availability_impact,
            availability_requirement=availability_requirement,
            base_score=base_score,
            collateral_damage_potential=collateral_damage_potential,
            confidentiality_impact=confidentiality_impact,
            confidentiality_requirement=confidentiality_requirement,
            environmental_score=environmental_score,
            exploitability=exploitability,
            integrity_impact=integrity_impact,
            integrity_requirement=integrity_requirement,
            remediation_level=remediation_level,
            report_confidence=report_confidence,
            target_distribution=target_distribution,
            temporal_score=temporal_score,
            vector_string=vector_string,
            version=version,
        )

        api_nvd20_cvss_data_v2.additional_properties = d
        return api_nvd20_cvss_data_v2

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
