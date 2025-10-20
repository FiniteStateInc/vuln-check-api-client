from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCVEDetail")


@_attrs_define
class AdvisoryCVEDetail:
    """
    Attributes:
        base_score (Union[Unset, str]):
        cveid (Union[Unset, str]):
        description (Union[Unset, str]):
        vector (Union[Unset, str]):
    """

    base_score: Union[Unset, str] = UNSET
    cveid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    vector: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        cveid = self.cveid

        description = self.description

        vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["baseScore"] = base_score
        if cveid is not UNSET:
            field_dict["cveid"] = cveid
        if description is not UNSET:
            field_dict["description"] = description
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_score = d.pop("baseScore", UNSET)

        cveid = d.pop("cveid", UNSET)

        description = d.pop("description", UNSET)

        vector = d.pop("vector", UNSET)

        advisory_cve_detail = cls(
            base_score=base_score,
            cveid=cveid,
            description=description,
            vector=vector,
        )

        advisory_cve_detail.additional_properties = d
        return advisory_cve_detail

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
