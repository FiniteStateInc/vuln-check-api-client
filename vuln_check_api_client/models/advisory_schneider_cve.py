from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySchneiderCVE")


@_attrs_define
class AdvisorySchneiderCVE:
    """
    Attributes:
        cve (Union[Unset, str]):
        cvss_score3 (Union[Unset, str]):
        cvss_score4 (Union[Unset, str]):
        cvss_vector3 (Union[Unset, str]):
        cvss_vector4 (Union[Unset, str]):
    """

    cve: Union[Unset, str] = UNSET
    cvss_score3: Union[Unset, str] = UNSET
    cvss_score4: Union[Unset, str] = UNSET
    cvss_vector3: Union[Unset, str] = UNSET
    cvss_vector4: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve = self.cve

        cvss_score3 = self.cvss_score3

        cvss_score4 = self.cvss_score4

        cvss_vector3 = self.cvss_vector3

        cvss_vector4 = self.cvss_vector4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score3 is not UNSET:
            field_dict["cvss_score3"] = cvss_score3
        if cvss_score4 is not UNSET:
            field_dict["cvss_score4"] = cvss_score4
        if cvss_vector3 is not UNSET:
            field_dict["cvss_vector3"] = cvss_vector3
        if cvss_vector4 is not UNSET:
            field_dict["cvss_vector4"] = cvss_vector4

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = d.pop("cve", UNSET)

        cvss_score3 = d.pop("cvss_score3", UNSET)

        cvss_score4 = d.pop("cvss_score4", UNSET)

        cvss_vector3 = d.pop("cvss_vector3", UNSET)

        cvss_vector4 = d.pop("cvss_vector4", UNSET)

        advisory_schneider_cve = cls(
            cve=cve,
            cvss_score3=cvss_score3,
            cvss_score4=cvss_score4,
            cvss_vector3=cvss_vector3,
            cvss_vector4=cvss_vector4,
        )

        advisory_schneider_cve.additional_properties = d
        return advisory_schneider_cve

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
