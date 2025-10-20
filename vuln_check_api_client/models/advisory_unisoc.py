from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryUnisoc")


@_attrs_define
class AdvisoryUnisoc:
    """
    Attributes:
        access_vector (Union[Unset, str]):
        affected_chipsets (Union[Unset, str]):
        affected_software (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        rating (Union[Unset, str]):
        score (Union[Unset, str]):
        severity (Union[Unset, str]):
        technology (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerability (Union[Unset, str]):
    """

    access_vector: Union[Unset, str] = UNSET
    affected_chipsets: Union[Unset, str] = UNSET
    affected_software: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    rating: Union[Unset, str] = UNSET
    score: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    technology: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerability: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_vector = self.access_vector

        affected_chipsets = self.affected_chipsets

        affected_software = self.affected_software

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        rating = self.rating

        score = self.score

        severity = self.severity

        technology = self.technology

        title = self.title

        updated_at = self.updated_at

        url = self.url

        vulnerability = self.vulnerability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_vector is not UNSET:
            field_dict["access_vector"] = access_vector
        if affected_chipsets is not UNSET:
            field_dict["affected_chipsets"] = affected_chipsets
        if affected_software is not UNSET:
            field_dict["affected_software"] = affected_software
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if rating is not UNSET:
            field_dict["rating"] = rating
        if score is not UNSET:
            field_dict["score"] = score
        if severity is not UNSET:
            field_dict["severity"] = severity
        if technology is not UNSET:
            field_dict["technology"] = technology
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerability is not UNSET:
            field_dict["vulnerability"] = vulnerability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_vector = d.pop("access_vector", UNSET)

        affected_chipsets = d.pop("affected_chipsets", UNSET)

        affected_software = d.pop("affected_software", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        rating = d.pop("rating", UNSET)

        score = d.pop("score", UNSET)

        severity = d.pop("severity", UNSET)

        technology = d.pop("technology", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vulnerability = d.pop("vulnerability", UNSET)

        advisory_unisoc = cls(
            access_vector=access_vector,
            affected_chipsets=affected_chipsets,
            affected_software=affected_software,
            cve=cve,
            date_added=date_added,
            description=description,
            rating=rating,
            score=score,
            severity=severity,
            technology=technology,
            title=title,
            updated_at=updated_at,
            url=url,
            vulnerability=vulnerability,
        )

        advisory_unisoc.additional_properties = d
        return advisory_unisoc

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
