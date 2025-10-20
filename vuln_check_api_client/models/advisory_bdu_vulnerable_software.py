from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_bdu_soft import AdvisoryBDUSoft


T = TypeVar("T", bound="AdvisoryBDUVulnerableSoftware")


@_attrs_define
class AdvisoryBDUVulnerableSoftware:
    """
    Attributes:
        soft (Union[Unset, AdvisoryBDUSoft]):
    """

    soft: Union[Unset, "AdvisoryBDUSoft"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        soft: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.soft, Unset):
            soft = self.soft.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if soft is not UNSET:
            field_dict["soft"] = soft

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_bdu_soft import AdvisoryBDUSoft

        d = dict(src_dict)
        _soft = d.pop("soft", UNSET)
        soft: Union[Unset, AdvisoryBDUSoft]
        if isinstance(_soft, Unset):
            soft = UNSET
        else:
            soft = AdvisoryBDUSoft.from_dict(_soft)

        advisory_bdu_vulnerable_software = cls(
            soft=soft,
        )

        advisory_bdu_vulnerable_software.additional_properties = d
        return advisory_bdu_vulnerable_software

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
