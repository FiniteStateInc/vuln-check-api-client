from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_cvss_data_v3 import ApiNVD20CvssDataV3


T = TypeVar("T", bound="ApiNVD20CvssMetricV3")


@_attrs_define
class ApiNVD20CvssMetricV3:
    """
    Attributes:
        cvss_data (Union[Unset, ApiNVD20CvssDataV3]):
        exploitability_score (Union[Unset, float]):
        impact_score (Union[Unset, float]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    cvss_data: Union[Unset, "ApiNVD20CvssDataV3"] = UNSET
    exploitability_score: Union[Unset, float] = UNSET
    impact_score: Union[Unset, float] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_data, Unset):
            cvss_data = self.cvss_data.to_dict()

        exploitability_score = self.exploitability_score

        impact_score = self.impact_score

        source = self.source

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_data is not UNSET:
            field_dict["cvssData"] = cvss_data
        if exploitability_score is not UNSET:
            field_dict["exploitabilityScore"] = exploitability_score
        if impact_score is not UNSET:
            field_dict["impactScore"] = impact_score
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_cvss_data_v3 import ApiNVD20CvssDataV3

        d = dict(src_dict)
        _cvss_data = d.pop("cvssData", UNSET)
        cvss_data: Union[Unset, ApiNVD20CvssDataV3]
        if isinstance(_cvss_data, Unset):
            cvss_data = UNSET
        else:
            cvss_data = ApiNVD20CvssDataV3.from_dict(_cvss_data)

        exploitability_score = d.pop("exploitabilityScore", UNSET)

        impact_score = d.pop("impactScore", UNSET)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        api_nvd20_cvss_metric_v3 = cls(
            cvss_data=cvss_data,
            exploitability_score=exploitability_score,
            impact_score=impact_score,
            source=source,
            type_=type_,
        )

        api_nvd20_cvss_metric_v3.additional_properties = d
        return api_nvd20_cvss_metric_v3

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
