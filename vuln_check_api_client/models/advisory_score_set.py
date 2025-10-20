from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryScoreSet")


@_attrs_define
class AdvisoryScoreSet:
    """
    Attributes:
        base_score (Union[Unset, str]):
        vector (Union[Unset, str]):
    """

    base_score: Union[Unset, str] = UNSET
    vector: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_score = d.pop("baseScore", UNSET)

        vector = d.pop("vector", UNSET)

        advisory_score_set = cls(
            base_score=base_score,
            vector=vector,
        )

        advisory_score_set.additional_properties = d
        return advisory_score_set

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
