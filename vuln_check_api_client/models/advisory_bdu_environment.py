from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_bdu_os import AdvisoryBDUOs


T = TypeVar("T", bound="AdvisoryBDUEnvironment")


@_attrs_define
class AdvisoryBDUEnvironment:
    """
    Attributes:
        os (Union[Unset, AdvisoryBDUOs]):
    """

    os: Union[Unset, "AdvisoryBDUOs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        os: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.os, Unset):
            os = self.os.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_bdu_os import AdvisoryBDUOs

        d = dict(src_dict)
        _os = d.pop("os", UNSET)
        os: Union[Unset, AdvisoryBDUOs]
        if isinstance(_os, Unset):
            os = UNSET
        else:
            os = AdvisoryBDUOs.from_dict(_os)

        advisory_bdu_environment = cls(
            os=os,
        )

        advisory_bdu_environment.additional_properties = d
        return advisory_bdu_environment

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
