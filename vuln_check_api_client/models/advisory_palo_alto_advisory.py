from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPaloAltoAdvisory")


@_attrs_define
class AdvisoryPaloAltoAdvisory:
    """
    Attributes:
        affected (Union[Unset, str]):
        applicable_versions (Union[Unset, str]):
        attack_complexity (Union[Unset, str]):
        attack_requirements (Union[Unset, str]):
        attack_vector (Union[Unset, str]):
        availability_impact (Union[Unset, str]):
        confidentiality_impact (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvssbase_score (Union[Unset, str]):
        date_published (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        integrity_impact (Union[Unset, str]):
        privileges_required (Union[Unset, str]):
        problem (Union[Unset, str]):
        product (Union[Unset, str]):
        scope (Union[Unset, str]):
        severity (Union[Unset, str]):
        solution (Union[Unset, str]):
        title (Union[Unset, str]):
        unaffected (Union[Unset, str]):
        url (Union[Unset, str]):
        user_interaction (Union[Unset, str]):
        workaround (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    applicable_versions: Union[Unset, str] = UNSET
    attack_complexity: Union[Unset, str] = UNSET
    attack_requirements: Union[Unset, str] = UNSET
    attack_vector: Union[Unset, str] = UNSET
    availability_impact: Union[Unset, str] = UNSET
    confidentiality_impact: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvssbase_score: Union[Unset, str] = UNSET
    date_published: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    integrity_impact: Union[Unset, str] = UNSET
    privileges_required: Union[Unset, str] = UNSET
    problem: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    solution: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    unaffected: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_interaction: Union[Unset, str] = UNSET
    workaround: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        applicable_versions = self.applicable_versions

        attack_complexity = self.attack_complexity

        attack_requirements = self.attack_requirements

        attack_vector = self.attack_vector

        availability_impact = self.availability_impact

        confidentiality_impact = self.confidentiality_impact

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvssbase_score = self.cvssbase_score

        date_published = self.date_published

        date_updated = self.date_updated

        date_added = self.date_added

        id = self.id

        integrity_impact = self.integrity_impact

        privileges_required = self.privileges_required

        problem = self.problem

        product = self.product

        scope = self.scope

        severity = self.severity

        solution = self.solution

        title = self.title

        unaffected = self.unaffected

        url = self.url

        user_interaction = self.user_interaction

        workaround = self.workaround

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if applicable_versions is not UNSET:
            field_dict["applicableVersions"] = applicable_versions
        if attack_complexity is not UNSET:
            field_dict["attackComplexity"] = attack_complexity
        if attack_requirements is not UNSET:
            field_dict["attackRequirements"] = attack_requirements
        if attack_vector is not UNSET:
            field_dict["attackVector"] = attack_vector
        if availability_impact is not UNSET:
            field_dict["availabilityImpact"] = availability_impact
        if confidentiality_impact is not UNSET:
            field_dict["confidentialityImpact"] = confidentiality_impact
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvssbase_score is not UNSET:
            field_dict["cvssbaseScore"] = cvssbase_score
        if date_published is not UNSET:
            field_dict["datePublished"] = date_published
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if integrity_impact is not UNSET:
            field_dict["integrityImpact"] = integrity_impact
        if privileges_required is not UNSET:
            field_dict["privilegesRequired"] = privileges_required
        if problem is not UNSET:
            field_dict["problem"] = problem
        if product is not UNSET:
            field_dict["product"] = product
        if scope is not UNSET:
            field_dict["scope"] = scope
        if severity is not UNSET:
            field_dict["severity"] = severity
        if solution is not UNSET:
            field_dict["solution"] = solution
        if title is not UNSET:
            field_dict["title"] = title
        if unaffected is not UNSET:
            field_dict["unaffected"] = unaffected
        if url is not UNSET:
            field_dict["url"] = url
        if user_interaction is not UNSET:
            field_dict["userInteraction"] = user_interaction
        if workaround is not UNSET:
            field_dict["workaround"] = workaround

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        applicable_versions = d.pop("applicableVersions", UNSET)

        attack_complexity = d.pop("attackComplexity", UNSET)

        attack_requirements = d.pop("attackRequirements", UNSET)

        attack_vector = d.pop("attackVector", UNSET)

        availability_impact = d.pop("availabilityImpact", UNSET)

        confidentiality_impact = d.pop("confidentialityImpact", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvssbase_score = d.pop("cvssbaseScore", UNSET)

        date_published = d.pop("datePublished", UNSET)

        date_updated = d.pop("dateUpdated", UNSET)

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        integrity_impact = d.pop("integrityImpact", UNSET)

        privileges_required = d.pop("privilegesRequired", UNSET)

        problem = d.pop("problem", UNSET)

        product = d.pop("product", UNSET)

        scope = d.pop("scope", UNSET)

        severity = d.pop("severity", UNSET)

        solution = d.pop("solution", UNSET)

        title = d.pop("title", UNSET)

        unaffected = d.pop("unaffected", UNSET)

        url = d.pop("url", UNSET)

        user_interaction = d.pop("userInteraction", UNSET)

        workaround = d.pop("workaround", UNSET)

        advisory_palo_alto_advisory = cls(
            affected=affected,
            applicable_versions=applicable_versions,
            attack_complexity=attack_complexity,
            attack_requirements=attack_requirements,
            attack_vector=attack_vector,
            availability_impact=availability_impact,
            confidentiality_impact=confidentiality_impact,
            cve=cve,
            cvssbase_score=cvssbase_score,
            date_published=date_published,
            date_updated=date_updated,
            date_added=date_added,
            id=id,
            integrity_impact=integrity_impact,
            privileges_required=privileges_required,
            problem=problem,
            product=product,
            scope=scope,
            severity=severity,
            solution=solution,
            title=title,
            unaffected=unaffected,
            url=url,
            user_interaction=user_interaction,
            workaround=workaround,
        )

        advisory_palo_alto_advisory.additional_properties = d
        return advisory_palo_alto_advisory

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
