from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryVCVulnerableCPEs")


@_attrs_define
class AdvisoryVCVulnerableCPEs:
    """
    Attributes:
        cve (Union[Unset, str]):
        unrolled (Union[Unset, list[str]]):
    """

    cve: Union[Unset, str] = UNSET
    unrolled: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve = self.cve

        unrolled: Union[Unset, list[str]] = UNSET
        if not isinstance(self.unrolled, Unset):
            unrolled = self.unrolled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if unrolled is not UNSET:
            field_dict["unrolled"] = unrolled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = d.pop("cve", UNSET)

        unrolled = cast(list[str], d.pop("unrolled", UNSET))

        advisory_vc_vulnerable_cp_es = cls(
            cve=cve,
            unrolled=unrolled,
        )

        advisory_vc_vulnerable_cp_es.additional_properties = d
        return advisory_vc_vulnerable_cp_es

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
