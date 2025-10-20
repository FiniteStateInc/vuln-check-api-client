from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCorrection")


@_attrs_define
class AdvisoryCorrection:
    """
    Attributes:
        corrected_at (Union[Unset, str]):
        orelease (Union[Unset, str]):
        release (Union[Unset, str]):
    """

    corrected_at: Union[Unset, str] = UNSET
    orelease: Union[Unset, str] = UNSET
    release: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        corrected_at = self.corrected_at

        orelease = self.orelease

        release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if corrected_at is not UNSET:
            field_dict["correctedAt"] = corrected_at
        if orelease is not UNSET:
            field_dict["orelease"] = orelease
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        corrected_at = d.pop("correctedAt", UNSET)

        orelease = d.pop("orelease", UNSET)

        release = d.pop("release", UNSET)

        advisory_correction = cls(
            corrected_at=corrected_at,
            orelease=orelease,
            release=release,
        )

        advisory_correction.additional_properties = d
        return advisory_correction

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
