from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEPSS")


@_attrs_define
class ApiEPSS:
    """
    Attributes:
        epss_percentile (Union[Unset, float]):
        epss_score (Union[Unset, float]):
        last_modified (Union[Unset, str]):
    """

    epss_percentile: Union[Unset, float] = UNSET
    epss_score: Union[Unset, float] = UNSET
    last_modified: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        epss_percentile = self.epss_percentile

        epss_score = self.epss_score

        last_modified = self.last_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if epss_percentile is not UNSET:
            field_dict["epss_percentile"] = epss_percentile
        if epss_score is not UNSET:
            field_dict["epss_score"] = epss_score
        if last_modified is not UNSET:
            field_dict["last_modified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        epss_percentile = d.pop("epss_percentile", UNSET)

        epss_score = d.pop("epss_score", UNSET)

        last_modified = d.pop("last_modified", UNSET)

        api_epss = cls(
            epss_percentile=epss_percentile,
            epss_score=epss_score,
            last_modified=last_modified,
        )

        api_epss.additional_properties = d
        return api_epss

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
