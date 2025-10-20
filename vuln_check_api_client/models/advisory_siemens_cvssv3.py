from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySiemensCVSSV3")


@_attrs_define
class AdvisorySiemensCVSSV3:
    """
    Attributes:
        base_score (Union[Unset, float]):
        base_severity (Union[Unset, str]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    base_score: Union[Unset, float] = UNSET
    base_severity: Union[Unset, str] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        base_severity = self.base_severity

        vector_string = self.vector_string

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if base_severity is not UNSET:
            field_dict["baseSeverity"] = base_severity
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_score = d.pop("baseScore", UNSET)

        base_severity = d.pop("baseSeverity", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        advisory_siemens_cvssv3 = cls(
            base_score=base_score,
            base_severity=base_severity,
            vector_string=vector_string,
            version=version,
        )

        advisory_siemens_cvssv3.additional_properties = d
        return advisory_siemens_cvssv3

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
