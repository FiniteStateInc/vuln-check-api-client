from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_threat_associated_base_metric import ApiNVD20ThreatAssociatedBaseMetric


T = TypeVar("T", bound="ApiNVD20ThreatCVSSV40")


@_attrs_define
class ApiNVD20ThreatCVSSV40:
    """
    Attributes:
        associated_base_metric_v40 (Union[Unset, ApiNVD20ThreatAssociatedBaseMetric]):
        base_threat_score (Union[Unset, float]):
        base_threat_severity (Union[Unset, str]):
        exploit_maturity (Union[Unset, str]):
    """

    associated_base_metric_v40: Union[Unset, "ApiNVD20ThreatAssociatedBaseMetric"] = UNSET
    base_threat_score: Union[Unset, float] = UNSET
    base_threat_severity: Union[Unset, str] = UNSET
    exploit_maturity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_base_metric_v40: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.associated_base_metric_v40, Unset):
            associated_base_metric_v40 = self.associated_base_metric_v40.to_dict()

        base_threat_score = self.base_threat_score

        base_threat_severity = self.base_threat_severity

        exploit_maturity = self.exploit_maturity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_base_metric_v40 is not UNSET:
            field_dict["associatedBaseMetricV40"] = associated_base_metric_v40
        if base_threat_score is not UNSET:
            field_dict["baseThreatScore"] = base_threat_score
        if base_threat_severity is not UNSET:
            field_dict["baseThreatSeverity"] = base_threat_severity
        if exploit_maturity is not UNSET:
            field_dict["exploitMaturity"] = exploit_maturity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_threat_associated_base_metric import ApiNVD20ThreatAssociatedBaseMetric

        d = dict(src_dict)
        _associated_base_metric_v40 = d.pop("associatedBaseMetricV40", UNSET)
        associated_base_metric_v40: Union[Unset, ApiNVD20ThreatAssociatedBaseMetric]
        if isinstance(_associated_base_metric_v40, Unset):
            associated_base_metric_v40 = UNSET
        else:
            associated_base_metric_v40 = ApiNVD20ThreatAssociatedBaseMetric.from_dict(_associated_base_metric_v40)

        base_threat_score = d.pop("baseThreatScore", UNSET)

        base_threat_severity = d.pop("baseThreatSeverity", UNSET)

        exploit_maturity = d.pop("exploitMaturity", UNSET)

        api_nvd20_threat_cvssv40 = cls(
            associated_base_metric_v40=associated_base_metric_v40,
            base_threat_score=base_threat_score,
            base_threat_severity=base_threat_severity,
            exploit_maturity=exploit_maturity,
        )

        api_nvd20_threat_cvssv40.additional_properties = d
        return api_nvd20_threat_cvssv40

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
