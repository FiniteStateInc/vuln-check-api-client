from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_bdu_vector import AdvisoryBDUVector


T = TypeVar("T", bound="AdvisoryBDUCvss")


@_attrs_define
class AdvisoryBDUCvss:
    """
    Attributes:
        vector (Union[Unset, AdvisoryBDUVector]):
    """

    vector: Union[Unset, "AdvisoryBDUVector"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_bdu_vector import AdvisoryBDUVector

        d = dict(src_dict)
        _vector = d.pop("vector", UNSET)
        vector: Union[Unset, AdvisoryBDUVector]
        if isinstance(_vector, Unset):
            vector = UNSET
        else:
            vector = AdvisoryBDUVector.from_dict(_vector)

        advisory_bdu_cvss = cls(
            vector=vector,
        )

        advisory_bdu_cvss.additional_properties = d
        return advisory_bdu_cvss

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
