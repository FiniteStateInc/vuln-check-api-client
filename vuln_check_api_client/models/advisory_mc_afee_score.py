from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryMcAfeeScore")


@_attrs_define
class AdvisoryMcAfeeScore:
    """
    Attributes:
        base (Union[Unset, str]):
        cve (Union[Unset, str]):
        temporal (Union[Unset, str]):
        vector (Union[Unset, str]):
    """

    base: Union[Unset, str] = UNSET
    cve: Union[Unset, str] = UNSET
    temporal: Union[Unset, str] = UNSET
    vector: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        cve = self.cve

        temporal = self.temporal

        vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if cve is not UNSET:
            field_dict["cve"] = cve
        if temporal is not UNSET:
            field_dict["temporal"] = temporal
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base = d.pop("base", UNSET)

        cve = d.pop("cve", UNSET)

        temporal = d.pop("temporal", UNSET)

        vector = d.pop("vector", UNSET)

        advisory_mc_afee_score = cls(
            base=base,
            cve=cve,
            temporal=temporal,
            vector=vector,
        )

        advisory_mc_afee_score.additional_properties = d
        return advisory_mc_afee_score

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
