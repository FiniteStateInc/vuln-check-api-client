from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiNVD20ThreatAssociatedBaseMetric")


@_attrs_define
class ApiNVD20ThreatAssociatedBaseMetric:
    """
    Attributes:
        base_score (Union[Unset, float]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    base_score: Union[Unset, float] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        source = self.source

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_score = d.pop("baseScore", UNSET)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        api_nvd20_threat_associated_base_metric = cls(
            base_score=base_score,
            source=source,
            type_=type_,
        )

        api_nvd20_threat_associated_base_metric.additional_properties = d
        return api_nvd20_threat_associated_base_metric

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
