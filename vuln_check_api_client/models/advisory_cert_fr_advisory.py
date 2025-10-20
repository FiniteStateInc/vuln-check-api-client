from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCertFRAdvisory")


@_attrs_define
class AdvisoryCertFRAdvisory:
    """
    Attributes:
        affected_systems_fr (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        reference (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        resume_fr (Union[Unset, str]):
        risks_fr (Union[Unset, str]):
        solution_fr (Union[Unset, str]):
        source_fr (Union[Unset, str]):
        title_fr (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_systems_fr: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    resume_fr: Union[Unset, str] = UNSET
    risks_fr: Union[Unset, str] = UNSET
    solution_fr: Union[Unset, str] = UNSET
    source_fr: Union[Unset, str] = UNSET
    title_fr: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_systems_fr = self.affected_systems_fr

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        reference = self.reference

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        resume_fr = self.resume_fr

        risks_fr = self.risks_fr

        solution_fr = self.solution_fr

        source_fr = self.source_fr

        title_fr = self.title_fr

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_systems_fr is not UNSET:
            field_dict["affected_systems_fr"] = affected_systems_fr
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if reference is not UNSET:
            field_dict["reference"] = reference
        if references is not UNSET:
            field_dict["references"] = references
        if resume_fr is not UNSET:
            field_dict["resume_fr"] = resume_fr
        if risks_fr is not UNSET:
            field_dict["risks_fr"] = risks_fr
        if solution_fr is not UNSET:
            field_dict["solution_fr"] = solution_fr
        if source_fr is not UNSET:
            field_dict["source_fr"] = source_fr
        if title_fr is not UNSET:
            field_dict["title_fr"] = title_fr
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_systems_fr = d.pop("affected_systems_fr", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        reference = d.pop("reference", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        resume_fr = d.pop("resume_fr", UNSET)

        risks_fr = d.pop("risks_fr", UNSET)

        solution_fr = d.pop("solution_fr", UNSET)

        source_fr = d.pop("source_fr", UNSET)

        title_fr = d.pop("title_fr", UNSET)

        url = d.pop("url", UNSET)

        advisory_cert_fr_advisory = cls(
            affected_systems_fr=affected_systems_fr,
            cve=cve,
            date_added=date_added,
            reference=reference,
            references=references,
            resume_fr=resume_fr,
            risks_fr=risks_fr,
            solution_fr=solution_fr,
            source_fr=source_fr,
            title_fr=title_fr,
            url=url,
        )

        advisory_cert_fr_advisory.additional_properties = d
        return advisory_cert_fr_advisory

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
