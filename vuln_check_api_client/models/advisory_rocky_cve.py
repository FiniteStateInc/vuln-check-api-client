from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRockyCve")


@_attrs_define
class AdvisoryRockyCve:
    """
    Attributes:
        cvss_3_base_score (Union[Unset, str]):
        cvss_3_scoring_vector (Union[Unset, str]):
        cwe (Union[Unset, str]):
        name (Union[Unset, str]):
        source_by (Union[Unset, str]):
        source_link (Union[Unset, str]):
    """

    cvss_3_base_score: Union[Unset, str] = UNSET
    cvss_3_scoring_vector: Union[Unset, str] = UNSET
    cwe: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    source_by: Union[Unset, str] = UNSET
    source_link: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_3_base_score = self.cvss_3_base_score

        cvss_3_scoring_vector = self.cvss_3_scoring_vector

        cwe = self.cwe

        name = self.name

        source_by = self.source_by

        source_link = self.source_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_3_base_score is not UNSET:
            field_dict["cvss3BaseScore"] = cvss_3_base_score
        if cvss_3_scoring_vector is not UNSET:
            field_dict["cvss3ScoringVector"] = cvss_3_scoring_vector
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if name is not UNSET:
            field_dict["name"] = name
        if source_by is not UNSET:
            field_dict["sourceBy"] = source_by
        if source_link is not UNSET:
            field_dict["sourceLink"] = source_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cvss_3_base_score = d.pop("cvss3BaseScore", UNSET)

        cvss_3_scoring_vector = d.pop("cvss3ScoringVector", UNSET)

        cwe = d.pop("cwe", UNSET)

        name = d.pop("name", UNSET)

        source_by = d.pop("sourceBy", UNSET)

        source_link = d.pop("sourceLink", UNSET)

        advisory_rocky_cve = cls(
            cvss_3_base_score=cvss_3_base_score,
            cvss_3_scoring_vector=cvss_3_scoring_vector,
            cwe=cwe,
            name=name,
            source_by=source_by,
            source_link=source_link,
        )

        advisory_rocky_cve.additional_properties = d
        return advisory_rocky_cve

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
