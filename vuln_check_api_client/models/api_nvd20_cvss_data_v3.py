from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20CvssDataV3")


@_attrs_define
class ApiNVD20CvssDataV3:
    """
    Attributes:
        attack_complexity (Union[Unset, str]):
        attack_vector (Union[Unset, str]):
        availability_impact (Union[Unset, str]):
        availability_requirement (Union[Unset, str]):
        base_score (Union[Unset, float]):
        base_severity (Union[Unset, str]):
        confidentiality_impact (Union[Unset, str]):
        confidentiality_requirement (Union[Unset, str]):
        environmental_score (Union[Unset, float]):
        environmental_severity (Union[Unset, str]):
        exploit_code_maturity (Union[Unset, str]):
        integrity_impact (Union[Unset, str]):
        integrity_requirement (Union[Unset, str]):
        modified_attack_complexity (Union[Unset, str]):
        modified_attack_vector (Union[Unset, str]):
        modified_availability_impact (Union[Unset, str]):
        modified_confidentiality_impact (Union[Unset, str]):
        modified_integrity_impact (Union[Unset, str]):
        modified_privileges_required (Union[Unset, str]):
        modified_scope (Union[Unset, str]):
        modified_user_interaction (Union[Unset, str]):
        privileges_required (Union[Unset, str]):
        remediation_level (Union[Unset, str]):
        report_confidence (Union[Unset, str]):
        scope (Union[Unset, str]):
        temporal_score (Union[Unset, float]):
        temporal_severity (Union[Unset, str]):
        user_interaction (Union[Unset, str]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    attack_complexity: Union[Unset, str] = UNSET
    attack_vector: Union[Unset, str] = UNSET
    availability_impact: Union[Unset, str] = UNSET
    availability_requirement: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    base_severity: Union[Unset, str] = UNSET
    confidentiality_impact: Union[Unset, str] = UNSET
    confidentiality_requirement: Union[Unset, str] = UNSET
    environmental_score: Union[Unset, float] = UNSET
    environmental_severity: Union[Unset, str] = UNSET
    exploit_code_maturity: Union[Unset, str] = UNSET
    integrity_impact: Union[Unset, str] = UNSET
    integrity_requirement: Union[Unset, str] = UNSET
    modified_attack_complexity: Union[Unset, str] = UNSET
    modified_attack_vector: Union[Unset, str] = UNSET
    modified_availability_impact: Union[Unset, str] = UNSET
    modified_confidentiality_impact: Union[Unset, str] = UNSET
    modified_integrity_impact: Union[Unset, str] = UNSET
    modified_privileges_required: Union[Unset, str] = UNSET
    modified_scope: Union[Unset, str] = UNSET
    modified_user_interaction: Union[Unset, str] = UNSET
    privileges_required: Union[Unset, str] = UNSET
    remediation_level: Union[Unset, str] = UNSET
    report_confidence: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    temporal_score: Union[Unset, float] = UNSET
    temporal_severity: Union[Unset, str] = UNSET
    user_interaction: Union[Unset, str] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attack_complexity = self.attack_complexity

        attack_vector = self.attack_vector

        availability_impact = self.availability_impact

        availability_requirement = self.availability_requirement

        base_score = self.base_score

        base_severity = self.base_severity

        confidentiality_impact = self.confidentiality_impact

        confidentiality_requirement = self.confidentiality_requirement

        environmental_score = self.environmental_score

        environmental_severity = self.environmental_severity

        exploit_code_maturity = self.exploit_code_maturity

        integrity_impact = self.integrity_impact

        integrity_requirement = self.integrity_requirement

        modified_attack_complexity = self.modified_attack_complexity

        modified_attack_vector = self.modified_attack_vector

        modified_availability_impact = self.modified_availability_impact

        modified_confidentiality_impact = self.modified_confidentiality_impact

        modified_integrity_impact = self.modified_integrity_impact

        modified_privileges_required = self.modified_privileges_required

        modified_scope = self.modified_scope

        modified_user_interaction = self.modified_user_interaction

        privileges_required = self.privileges_required

        remediation_level = self.remediation_level

        report_confidence = self.report_confidence

        scope = self.scope

        temporal_score = self.temporal_score

        temporal_severity = self.temporal_severity

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
        if availability_requirement is not UNSET:
            field_dict["availabilityRequirement"] = availability_requirement
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if base_severity is not UNSET:
            field_dict["baseSeverity"] = base_severity
        if confidentiality_impact is not UNSET:
            field_dict["confidentialityImpact"] = confidentiality_impact
        if confidentiality_requirement is not UNSET:
            field_dict["confidentialityRequirement"] = confidentiality_requirement
        if environmental_score is not UNSET:
            field_dict["environmentalScore"] = environmental_score
        if environmental_severity is not UNSET:
            field_dict["environmentalSeverity"] = environmental_severity
        if exploit_code_maturity is not UNSET:
            field_dict["exploitCodeMaturity"] = exploit_code_maturity
        if integrity_impact is not UNSET:
            field_dict["integrityImpact"] = integrity_impact
        if integrity_requirement is not UNSET:
            field_dict["integrityRequirement"] = integrity_requirement
        if modified_attack_complexity is not UNSET:
            field_dict["modifiedAttackComplexity"] = modified_attack_complexity
        if modified_attack_vector is not UNSET:
            field_dict["modifiedAttackVector"] = modified_attack_vector
        if modified_availability_impact is not UNSET:
            field_dict["modifiedAvailabilityImpact"] = modified_availability_impact
        if modified_confidentiality_impact is not UNSET:
            field_dict["modifiedConfidentialityImpact"] = modified_confidentiality_impact
        if modified_integrity_impact is not UNSET:
            field_dict["modifiedIntegrityImpact"] = modified_integrity_impact
        if modified_privileges_required is not UNSET:
            field_dict["modifiedPrivilegesRequired"] = modified_privileges_required
        if modified_scope is not UNSET:
            field_dict["modifiedScope"] = modified_scope
        if modified_user_interaction is not UNSET:
            field_dict["modifiedUserInteraction"] = modified_user_interaction
        if privileges_required is not UNSET:
            field_dict["privilegesRequired"] = privileges_required
        if remediation_level is not UNSET:
            field_dict["remediationLevel"] = remediation_level
        if report_confidence is not UNSET:
            field_dict["reportConfidence"] = report_confidence
        if scope is not UNSET:
            field_dict["scope"] = scope
        if temporal_score is not UNSET:
            field_dict["temporalScore"] = temporal_score
        if temporal_severity is not UNSET:
            field_dict["temporalSeverity"] = temporal_severity
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

        availability_requirement = d.pop("availabilityRequirement", UNSET)

        base_score = d.pop("baseScore", UNSET)

        base_severity = d.pop("baseSeverity", UNSET)

        confidentiality_impact = d.pop("confidentialityImpact", UNSET)

        confidentiality_requirement = d.pop("confidentialityRequirement", UNSET)

        environmental_score = d.pop("environmentalScore", UNSET)

        environmental_severity = d.pop("environmentalSeverity", UNSET)

        exploit_code_maturity = d.pop("exploitCodeMaturity", UNSET)

        integrity_impact = d.pop("integrityImpact", UNSET)

        integrity_requirement = d.pop("integrityRequirement", UNSET)

        modified_attack_complexity = d.pop("modifiedAttackComplexity", UNSET)

        modified_attack_vector = d.pop("modifiedAttackVector", UNSET)

        modified_availability_impact = d.pop("modifiedAvailabilityImpact", UNSET)

        modified_confidentiality_impact = d.pop("modifiedConfidentialityImpact", UNSET)

        modified_integrity_impact = d.pop("modifiedIntegrityImpact", UNSET)

        modified_privileges_required = d.pop("modifiedPrivilegesRequired", UNSET)

        modified_scope = d.pop("modifiedScope", UNSET)

        modified_user_interaction = d.pop("modifiedUserInteraction", UNSET)

        privileges_required = d.pop("privilegesRequired", UNSET)

        remediation_level = d.pop("remediationLevel", UNSET)

        report_confidence = d.pop("reportConfidence", UNSET)

        scope = d.pop("scope", UNSET)

        temporal_score = d.pop("temporalScore", UNSET)

        temporal_severity = d.pop("temporalSeverity", UNSET)

        user_interaction = d.pop("userInteraction", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        api_nvd20_cvss_data_v3 = cls(
            attack_complexity=attack_complexity,
            attack_vector=attack_vector,
            availability_impact=availability_impact,
            availability_requirement=availability_requirement,
            base_score=base_score,
            base_severity=base_severity,
            confidentiality_impact=confidentiality_impact,
            confidentiality_requirement=confidentiality_requirement,
            environmental_score=environmental_score,
            environmental_severity=environmental_severity,
            exploit_code_maturity=exploit_code_maturity,
            integrity_impact=integrity_impact,
            integrity_requirement=integrity_requirement,
            modified_attack_complexity=modified_attack_complexity,
            modified_attack_vector=modified_attack_vector,
            modified_availability_impact=modified_availability_impact,
            modified_confidentiality_impact=modified_confidentiality_impact,
            modified_integrity_impact=modified_integrity_impact,
            modified_privileges_required=modified_privileges_required,
            modified_scope=modified_scope,
            modified_user_interaction=modified_user_interaction,
            privileges_required=privileges_required,
            remediation_level=remediation_level,
            report_confidence=report_confidence,
            scope=scope,
            temporal_score=temporal_score,
            temporal_severity=temporal_severity,
            user_interaction=user_interaction,
            vector_string=vector_string,
            version=version,
        )

        api_nvd20_cvss_data_v3.additional_properties = d
        return api_nvd20_cvss_data_v3

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
