from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEPSSData")


@_attrs_define
class ApiEPSSData:
    """
    Attributes:
        field_timestamp (Union[Unset, str]):
        cve (Union[Unset, str]):
        epss_percentile (Union[Unset, float]):
        epss_score (Union[Unset, float]):
    """

    field_timestamp: Union[Unset, str] = UNSET
    cve: Union[Unset, str] = UNSET
    epss_percentile: Union[Unset, float] = UNSET
    epss_score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_timestamp = self.field_timestamp

        cve = self.cve

        epss_percentile = self.epss_percentile

        epss_score = self.epss_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_timestamp is not UNSET:
            field_dict["_timestamp"] = field_timestamp
        if cve is not UNSET:
            field_dict["cve"] = cve
        if epss_percentile is not UNSET:
            field_dict["epss_percentile"] = epss_percentile
        if epss_score is not UNSET:
            field_dict["epss_score"] = epss_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_timestamp = d.pop("_timestamp", UNSET)

        cve = d.pop("cve", UNSET)

        epss_percentile = d.pop("epss_percentile", UNSET)

        epss_score = d.pop("epss_score", UNSET)

        api_epss_data = cls(
            field_timestamp=field_timestamp,
            cve=cve,
            epss_percentile=epss_percentile,
            epss_score=epss_score,
        )

        api_epss_data.additional_properties = d
        return api_epss_data

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
