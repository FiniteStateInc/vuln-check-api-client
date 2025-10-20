from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryGHCvss")


@_attrs_define
class AdvisoryGHCvss:
    """
    Attributes:
        score (Union[Unset, float]):
        vector_string (Union[Unset, str]):
    """

    score: Union[Unset, float] = UNSET
    vector_string: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        vector_string = self.vector_string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        advisory_gh_cvss = cls(
            score=score,
            vector_string=vector_string,
        )

        advisory_gh_cvss.additional_properties = d
        return advisory_gh_cvss

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
