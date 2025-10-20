from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryIAVA")


@_attrs_define
class AdvisoryIAVA:
    """
    Attributes:
        iava (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
    """

    iava: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iava = self.iava

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iava is not UNSET:
            field_dict["IAVA"] = iava
        if cve is not UNSET:
            field_dict["cve"] = cve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        iava = d.pop("IAVA", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        advisory_iava = cls(
            iava=iava,
            cve=cve,
        )

        advisory_iava.additional_properties = d
        return advisory_iava

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
