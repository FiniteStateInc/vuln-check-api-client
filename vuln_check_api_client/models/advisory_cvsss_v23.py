from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCvsssV23")


@_attrs_define
class AdvisoryCvsssV23:
    """
    Attributes:
        basescore (Union[Unset, str]):
        temporalscore (Union[Unset, str]):
    """

    basescore: Union[Unset, str] = UNSET
    temporalscore: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basescore = self.basescore

        temporalscore = self.temporalscore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basescore is not UNSET:
            field_dict["basescore"] = basescore
        if temporalscore is not UNSET:
            field_dict["temporalscore"] = temporalscore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        basescore = d.pop("basescore", UNSET)

        temporalscore = d.pop("temporalscore", UNSET)

        advisory_cvsss_v23 = cls(
            basescore=basescore,
            temporalscore=temporalscore,
        )

        advisory_cvsss_v23.additional_properties = d
        return advisory_cvsss_v23

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
