from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_siemens_tlp import AdvisorySiemensTLP


T = TypeVar("T", bound="AdvisorySiemensDistribution")


@_attrs_define
class AdvisorySiemensDistribution:
    """
    Attributes:
        text (Union[Unset, str]):
        tlp (Union[Unset, AdvisorySiemensTLP]):
    """

    text: Union[Unset, str] = UNSET
    tlp: Union[Unset, "AdvisorySiemensTLP"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        tlp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlp, Unset):
            tlp = self.tlp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if tlp is not UNSET:
            field_dict["tlp"] = tlp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_siemens_tlp import AdvisorySiemensTLP

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        _tlp = d.pop("tlp", UNSET)
        tlp: Union[Unset, AdvisorySiemensTLP]
        if isinstance(_tlp, Unset):
            tlp = UNSET
        else:
            tlp = AdvisorySiemensTLP.from_dict(_tlp)

        advisory_siemens_distribution = cls(
            text=text,
            tlp=tlp,
        )

        advisory_siemens_distribution.additional_properties = d
        return advisory_siemens_distribution

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
