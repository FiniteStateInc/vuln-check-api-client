from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCVSSV40")


@_attrs_define
class AdvisoryCVSSV40:
    """
    Attributes:
        automatable (Union[Unset, str]):
        recovery (Union[Unset, str]):
        safety (Union[Unset, str]):
        attack_complexity (Union[Unset, str]):
        attack_requirements (Union[Unset, str]):
        attack_vector (Union[Unset, str]):
        availability_requirement (Union[Unset, str]):
        base_score (Union[Unset, float]):
        base_severity (Union[Unset, str]):
        confidentiality_requirement (Union[Unset, str]):
        exploit_maturity (Union[Unset, str]):
        integrity_requirement (Union[Unset, str]):
        modified_attack_complexity (Union[Unset, str]):
        modified_attack_requirements (Union[Unset, str]):
        modified_attack_vector (Union[Unset, str]):
        modified_privileges_required (Union[Unset, str]):
        modified_sub_availability_impact (Union[Unset, str]):
        modified_sub_confidentiality_impact (Union[Unset, str]):
        modified_sub_integrity_impact (Union[Unset, str]):
        modified_user_interaction (Union[Unset, str]):
        modified_vuln_availability_impact (Union[Unset, str]):
        modified_vuln_confidentiality_impact (Union[Unset, str]):
        modified_vuln_integrity_impact (Union[Unset, str]):
        privileges_required (Union[Unset, str]):
        provider_urgency (Union[Unset, str]):
        sub_availability_impact (Union[Unset, str]):
        sub_confidentiality_impact (Union[Unset, str]):
        sub_integrity_impact (Union[Unset, str]):
        user_interaction (Union[Unset, str]):
        value_density (Union[Unset, str]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
        vuln_availability_impact (Union[Unset, str]):
        vuln_confidentiality_impact (Union[Unset, str]):
        vuln_integrity_impact (Union[Unset, str]):
        vulnerability_response_effort (Union[Unset, str]):
    """

    automatable: Union[Unset, str] = UNSET
    recovery: Union[Unset, str] = UNSET
    safety: Union[Unset, str] = UNSET
    attack_complexity: Union[Unset, str] = UNSET
    attack_requirements: Union[Unset, str] = UNSET
    attack_vector: Union[Unset, str] = UNSET
    availability_requirement: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    base_severity: Union[Unset, str] = UNSET
    confidentiality_requirement: Union[Unset, str] = UNSET
    exploit_maturity: Union[Unset, str] = UNSET
    integrity_requirement: Union[Unset, str] = UNSET
    modified_attack_complexity: Union[Unset, str] = UNSET
    modified_attack_requirements: Union[Unset, str] = UNSET
    modified_attack_vector: Union[Unset, str] = UNSET
    modified_privileges_required: Union[Unset, str] = UNSET
    modified_sub_availability_impact: Union[Unset, str] = UNSET
    modified_sub_confidentiality_impact: Union[Unset, str] = UNSET
    modified_sub_integrity_impact: Union[Unset, str] = UNSET
    modified_user_interaction: Union[Unset, str] = UNSET
    modified_vuln_availability_impact: Union[Unset, str] = UNSET
    modified_vuln_confidentiality_impact: Union[Unset, str] = UNSET
    modified_vuln_integrity_impact: Union[Unset, str] = UNSET
    privileges_required: Union[Unset, str] = UNSET
    provider_urgency: Union[Unset, str] = UNSET
    sub_availability_impact: Union[Unset, str] = UNSET
    sub_confidentiality_impact: Union[Unset, str] = UNSET
    sub_integrity_impact: Union[Unset, str] = UNSET
    user_interaction: Union[Unset, str] = UNSET
    value_density: Union[Unset, str] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    vuln_availability_impact: Union[Unset, str] = UNSET
    vuln_confidentiality_impact: Union[Unset, str] = UNSET
    vuln_integrity_impact: Union[Unset, str] = UNSET
    vulnerability_response_effort: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automatable = self.automatable

        recovery = self.recovery

        safety = self.safety

        attack_complexity = self.attack_complexity

        attack_requirements = self.attack_requirements

        attack_vector = self.attack_vector

        availability_requirement = self.availability_requirement

        base_score = self.base_score

        base_severity = self.base_severity

        confidentiality_requirement = self.confidentiality_requirement

        exploit_maturity = self.exploit_maturity

        integrity_requirement = self.integrity_requirement

        modified_attack_complexity = self.modified_attack_complexity

        modified_attack_requirements = self.modified_attack_requirements

        modified_attack_vector = self.modified_attack_vector

        modified_privileges_required = self.modified_privileges_required

        modified_sub_availability_impact = self.modified_sub_availability_impact

        modified_sub_confidentiality_impact = self.modified_sub_confidentiality_impact

        modified_sub_integrity_impact = self.modified_sub_integrity_impact

        modified_user_interaction = self.modified_user_interaction

        modified_vuln_availability_impact = self.modified_vuln_availability_impact

        modified_vuln_confidentiality_impact = self.modified_vuln_confidentiality_impact

        modified_vuln_integrity_impact = self.modified_vuln_integrity_impact

        privileges_required = self.privileges_required

        provider_urgency = self.provider_urgency

        sub_availability_impact = self.sub_availability_impact

        sub_confidentiality_impact = self.sub_confidentiality_impact

        sub_integrity_impact = self.sub_integrity_impact

        user_interaction = self.user_interaction

        value_density = self.value_density

        vector_string = self.vector_string

        version = self.version

        vuln_availability_impact = self.vuln_availability_impact

        vuln_confidentiality_impact = self.vuln_confidentiality_impact

        vuln_integrity_impact = self.vuln_integrity_impact

        vulnerability_response_effort = self.vulnerability_response_effort

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatable is not UNSET:
            field_dict["Automatable"] = automatable
        if recovery is not UNSET:
            field_dict["Recovery"] = recovery
        if safety is not UNSET:
            field_dict["Safety"] = safety
        if attack_complexity is not UNSET:
            field_dict["attackComplexity"] = attack_complexity
        if attack_requirements is not UNSET:
            field_dict["attackRequirements"] = attack_requirements
        if attack_vector is not UNSET:
            field_dict["attackVector"] = attack_vector
        if availability_requirement is not UNSET:
            field_dict["availabilityRequirement"] = availability_requirement
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if base_severity is not UNSET:
            field_dict["baseSeverity"] = base_severity
        if confidentiality_requirement is not UNSET:
            field_dict["confidentialityRequirement"] = confidentiality_requirement
        if exploit_maturity is not UNSET:
            field_dict["exploitMaturity"] = exploit_maturity
        if integrity_requirement is not UNSET:
            field_dict["integrityRequirement"] = integrity_requirement
        if modified_attack_complexity is not UNSET:
            field_dict["modifiedAttackComplexity"] = modified_attack_complexity
        if modified_attack_requirements is not UNSET:
            field_dict["modifiedAttackRequirements"] = modified_attack_requirements
        if modified_attack_vector is not UNSET:
            field_dict["modifiedAttackVector"] = modified_attack_vector
        if modified_privileges_required is not UNSET:
            field_dict["modifiedPrivilegesRequired"] = modified_privileges_required
        if modified_sub_availability_impact is not UNSET:
            field_dict["modifiedSubAvailabilityImpact"] = modified_sub_availability_impact
        if modified_sub_confidentiality_impact is not UNSET:
            field_dict["modifiedSubConfidentialityImpact"] = modified_sub_confidentiality_impact
        if modified_sub_integrity_impact is not UNSET:
            field_dict["modifiedSubIntegrityImpact"] = modified_sub_integrity_impact
        if modified_user_interaction is not UNSET:
            field_dict["modifiedUserInteraction"] = modified_user_interaction
        if modified_vuln_availability_impact is not UNSET:
            field_dict["modifiedVulnAvailabilityImpact"] = modified_vuln_availability_impact
        if modified_vuln_confidentiality_impact is not UNSET:
            field_dict["modifiedVulnConfidentialityImpact"] = modified_vuln_confidentiality_impact
        if modified_vuln_integrity_impact is not UNSET:
            field_dict["modifiedVulnIntegrityImpact"] = modified_vuln_integrity_impact
        if privileges_required is not UNSET:
            field_dict["privilegesRequired"] = privileges_required
        if provider_urgency is not UNSET:
            field_dict["providerUrgency"] = provider_urgency
        if sub_availability_impact is not UNSET:
            field_dict["subAvailabilityImpact"] = sub_availability_impact
        if sub_confidentiality_impact is not UNSET:
            field_dict["subConfidentialityImpact"] = sub_confidentiality_impact
        if sub_integrity_impact is not UNSET:
            field_dict["subIntegrityImpact"] = sub_integrity_impact
        if user_interaction is not UNSET:
            field_dict["userInteraction"] = user_interaction
        if value_density is not UNSET:
            field_dict["valueDensity"] = value_density
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version
        if vuln_availability_impact is not UNSET:
            field_dict["vulnAvailabilityImpact"] = vuln_availability_impact
        if vuln_confidentiality_impact is not UNSET:
            field_dict["vulnConfidentialityImpact"] = vuln_confidentiality_impact
        if vuln_integrity_impact is not UNSET:
            field_dict["vulnIntegrityImpact"] = vuln_integrity_impact
        if vulnerability_response_effort is not UNSET:
            field_dict["vulnerabilityResponseEffort"] = vulnerability_response_effort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automatable = d.pop("Automatable", UNSET)

        recovery = d.pop("Recovery", UNSET)

        safety = d.pop("Safety", UNSET)

        attack_complexity = d.pop("attackComplexity", UNSET)

        attack_requirements = d.pop("attackRequirements", UNSET)

        attack_vector = d.pop("attackVector", UNSET)

        availability_requirement = d.pop("availabilityRequirement", UNSET)

        base_score = d.pop("baseScore", UNSET)

        base_severity = d.pop("baseSeverity", UNSET)

        confidentiality_requirement = d.pop("confidentialityRequirement", UNSET)

        exploit_maturity = d.pop("exploitMaturity", UNSET)

        integrity_requirement = d.pop("integrityRequirement", UNSET)

        modified_attack_complexity = d.pop("modifiedAttackComplexity", UNSET)

        modified_attack_requirements = d.pop("modifiedAttackRequirements", UNSET)

        modified_attack_vector = d.pop("modifiedAttackVector", UNSET)

        modified_privileges_required = d.pop("modifiedPrivilegesRequired", UNSET)

        modified_sub_availability_impact = d.pop("modifiedSubAvailabilityImpact", UNSET)

        modified_sub_confidentiality_impact = d.pop("modifiedSubConfidentialityImpact", UNSET)

        modified_sub_integrity_impact = d.pop("modifiedSubIntegrityImpact", UNSET)

        modified_user_interaction = d.pop("modifiedUserInteraction", UNSET)

        modified_vuln_availability_impact = d.pop("modifiedVulnAvailabilityImpact", UNSET)

        modified_vuln_confidentiality_impact = d.pop("modifiedVulnConfidentialityImpact", UNSET)

        modified_vuln_integrity_impact = d.pop("modifiedVulnIntegrityImpact", UNSET)

        privileges_required = d.pop("privilegesRequired", UNSET)

        provider_urgency = d.pop("providerUrgency", UNSET)

        sub_availability_impact = d.pop("subAvailabilityImpact", UNSET)

        sub_confidentiality_impact = d.pop("subConfidentialityImpact", UNSET)

        sub_integrity_impact = d.pop("subIntegrityImpact", UNSET)

        user_interaction = d.pop("userInteraction", UNSET)

        value_density = d.pop("valueDensity", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        vuln_availability_impact = d.pop("vulnAvailabilityImpact", UNSET)

        vuln_confidentiality_impact = d.pop("vulnConfidentialityImpact", UNSET)

        vuln_integrity_impact = d.pop("vulnIntegrityImpact", UNSET)

        vulnerability_response_effort = d.pop("vulnerabilityResponseEffort", UNSET)

        advisory_cvssv40 = cls(
            automatable=automatable,
            recovery=recovery,
            safety=safety,
            attack_complexity=attack_complexity,
            attack_requirements=attack_requirements,
            attack_vector=attack_vector,
            availability_requirement=availability_requirement,
            base_score=base_score,
            base_severity=base_severity,
            confidentiality_requirement=confidentiality_requirement,
            exploit_maturity=exploit_maturity,
            integrity_requirement=integrity_requirement,
            modified_attack_complexity=modified_attack_complexity,
            modified_attack_requirements=modified_attack_requirements,
            modified_attack_vector=modified_attack_vector,
            modified_privileges_required=modified_privileges_required,
            modified_sub_availability_impact=modified_sub_availability_impact,
            modified_sub_confidentiality_impact=modified_sub_confidentiality_impact,
            modified_sub_integrity_impact=modified_sub_integrity_impact,
            modified_user_interaction=modified_user_interaction,
            modified_vuln_availability_impact=modified_vuln_availability_impact,
            modified_vuln_confidentiality_impact=modified_vuln_confidentiality_impact,
            modified_vuln_integrity_impact=modified_vuln_integrity_impact,
            privileges_required=privileges_required,
            provider_urgency=provider_urgency,
            sub_availability_impact=sub_availability_impact,
            sub_confidentiality_impact=sub_confidentiality_impact,
            sub_integrity_impact=sub_integrity_impact,
            user_interaction=user_interaction,
            value_density=value_density,
            vector_string=vector_string,
            version=version,
            vuln_availability_impact=vuln_availability_impact,
            vuln_confidentiality_impact=vuln_confidentiality_impact,
            vuln_integrity_impact=vuln_integrity_impact,
            vulnerability_response_effort=vulnerability_response_effort,
        )

        advisory_cvssv40.additional_properties = d
        return advisory_cvssv40

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
