from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryNVD20CVECPEMatch")


@_attrs_define
class AdvisoryNVD20CVECPEMatch:
    """
    Attributes:
        criteria (Union[Unset, str]):
        match_criteria_id (Union[Unset, str]):
        version_end_excluding (Union[Unset, str]):
        version_end_including (Union[Unset, str]):
        version_start_excluding (Union[Unset, str]):
        version_start_including (Union[Unset, str]):
        vulnerable (Union[Unset, bool]):
    """

    criteria: Union[Unset, str] = UNSET
    match_criteria_id: Union[Unset, str] = UNSET
    version_end_excluding: Union[Unset, str] = UNSET
    version_end_including: Union[Unset, str] = UNSET
    version_start_excluding: Union[Unset, str] = UNSET
    version_start_including: Union[Unset, str] = UNSET
    vulnerable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria

        match_criteria_id = self.match_criteria_id

        version_end_excluding = self.version_end_excluding

        version_end_including = self.version_end_including

        version_start_excluding = self.version_start_excluding

        version_start_including = self.version_start_including

        vulnerable = self.vulnerable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if match_criteria_id is not UNSET:
            field_dict["matchCriteriaId"] = match_criteria_id
        if version_end_excluding is not UNSET:
            field_dict["versionEndExcluding"] = version_end_excluding
        if version_end_including is not UNSET:
            field_dict["versionEndIncluding"] = version_end_including
        if version_start_excluding is not UNSET:
            field_dict["versionStartExcluding"] = version_start_excluding
        if version_start_including is not UNSET:
            field_dict["versionStartIncluding"] = version_start_including
        if vulnerable is not UNSET:
            field_dict["vulnerable"] = vulnerable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criteria = d.pop("criteria", UNSET)

        match_criteria_id = d.pop("matchCriteriaId", UNSET)

        version_end_excluding = d.pop("versionEndExcluding", UNSET)

        version_end_including = d.pop("versionEndIncluding", UNSET)

        version_start_excluding = d.pop("versionStartExcluding", UNSET)

        version_start_including = d.pop("versionStartIncluding", UNSET)

        vulnerable = d.pop("vulnerable", UNSET)

        advisory_nvd20cvecpe_match = cls(
            criteria=criteria,
            match_criteria_id=match_criteria_id,
            version_end_excluding=version_end_excluding,
            version_end_including=version_end_including,
            version_start_excluding=version_start_excluding,
            version_start_including=version_start_including,
            vulnerable=vulnerable,
        )

        advisory_nvd20cvecpe_match.additional_properties = d
        return advisory_nvd20cvecpe_match

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
