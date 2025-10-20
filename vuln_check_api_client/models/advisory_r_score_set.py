from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRScoreSet")


@_attrs_define
class AdvisoryRScoreSet:
    """
    Attributes:
        base_score (Union[Unset, str]):
        product_id (Union[Unset, str]):
        temporal_score (Union[Unset, str]):
        vector (Union[Unset, str]):
    """

    base_score: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    temporal_score: Union[Unset, str] = UNSET
    vector: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        product_id = self.product_id

        temporal_score = self.temporal_score

        vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["base_score"] = base_score
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if temporal_score is not UNSET:
            field_dict["temporal_score"] = temporal_score
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_score = d.pop("base_score", UNSET)

        product_id = d.pop("product_id", UNSET)

        temporal_score = d.pop("temporal_score", UNSET)

        vector = d.pop("vector", UNSET)

        advisory_r_score_set = cls(
            base_score=base_score,
            product_id=product_id,
            temporal_score=temporal_score,
            vector=vector,
        )

        advisory_r_score_set.additional_properties = d
        return advisory_r_score_set

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
