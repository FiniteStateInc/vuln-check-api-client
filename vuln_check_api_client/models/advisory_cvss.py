from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCVSS")


@_attrs_define
class AdvisoryCVSS:
    """
    Attributes:
        score (Union[Unset, str]):
        severity (Union[Unset, str]):
        type_ (Union[Unset, str]):
        vector (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    score: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    vector: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        severity = self.severity

        type_ = self.type_

        vector = self.vector

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vector is not UNSET:
            field_dict["vector"] = vector
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score", UNSET)

        severity = d.pop("severity", UNSET)

        type_ = d.pop("type", UNSET)

        vector = d.pop("vector", UNSET)

        version = d.pop("version", UNSET)

        advisory_cvss = cls(
            score=score,
            severity=severity,
            type_=type_,
            vector=vector,
            version=version,
        )

        advisory_cvss.additional_properties = d
        return advisory_cvss

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
