from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryOpenJDKCVE")


@_attrs_define
class AdvisoryOpenJDKCVE:
    """
    Attributes:
        cve (Union[Unset, str]):
        cvss_score (Union[Unset, str]):
        cvss_vector (Union[Unset, str]):
    """

    cve: Union[Unset, str] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve = self.cve

        cvss_score = self.cvss_score

        cvss_vector = self.cvss_vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = d.pop("cve", UNSET)

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        advisory_open_jdkcve = cls(
            cve=cve,
            cvss_score=cvss_score,
            cvss_vector=cvss_vector,
        )

        advisory_open_jdkcve.additional_properties = d
        return advisory_open_jdkcve

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
