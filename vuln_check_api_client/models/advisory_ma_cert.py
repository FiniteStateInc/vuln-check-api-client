from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMACert")


@_attrs_define
class AdvisoryMACert:
    """
    Attributes:
        affected_systems_fr (Union[Unset, str]):
        assessment_fr (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        impact_fr (Union[Unset, str]):
        reference (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        risk_fr (Union[Unset, str]):
        risks_fr (Union[Unset, str]):
        solution_fr (Union[Unset, str]):
        title_fr (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_systems_fr: Union[Unset, str] = UNSET
    assessment_fr: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    impact_fr: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    risk_fr: Union[Unset, str] = UNSET
    risks_fr: Union[Unset, str] = UNSET
    solution_fr: Union[Unset, str] = UNSET
    title_fr: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_systems_fr = self.affected_systems_fr

        assessment_fr = self.assessment_fr

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        impact_fr = self.impact_fr

        reference = self.reference

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        risk_fr = self.risk_fr

        risks_fr = self.risks_fr

        solution_fr = self.solution_fr

        title_fr = self.title_fr

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_systems_fr is not UNSET:
            field_dict["affected_systems_fr"] = affected_systems_fr
        if assessment_fr is not UNSET:
            field_dict["assessment_fr"] = assessment_fr
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if impact_fr is not UNSET:
            field_dict["impact_fr"] = impact_fr
        if reference is not UNSET:
            field_dict["reference"] = reference
        if references is not UNSET:
            field_dict["references"] = references
        if risk_fr is not UNSET:
            field_dict["risk_fr"] = risk_fr
        if risks_fr is not UNSET:
            field_dict["risks_fr"] = risks_fr
        if solution_fr is not UNSET:
            field_dict["solution_fr"] = solution_fr
        if title_fr is not UNSET:
            field_dict["title_fr"] = title_fr
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_systems_fr = d.pop("affected_systems_fr", UNSET)

        assessment_fr = d.pop("assessment_fr", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        impact_fr = d.pop("impact_fr", UNSET)

        reference = d.pop("reference", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        risk_fr = d.pop("risk_fr", UNSET)

        risks_fr = d.pop("risks_fr", UNSET)

        solution_fr = d.pop("solution_fr", UNSET)

        title_fr = d.pop("title_fr", UNSET)

        url = d.pop("url", UNSET)

        advisory_ma_cert = cls(
            affected_systems_fr=affected_systems_fr,
            assessment_fr=assessment_fr,
            cve=cve,
            date_added=date_added,
            impact_fr=impact_fr,
            reference=reference,
            references=references,
            risk_fr=risk_fr,
            risks_fr=risks_fr,
            solution_fr=solution_fr,
            title_fr=title_fr,
            url=url,
        )

        advisory_ma_cert.additional_properties = d
        return advisory_ma_cert

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
