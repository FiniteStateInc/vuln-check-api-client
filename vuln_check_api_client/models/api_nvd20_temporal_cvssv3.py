from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_temporal_associated_base_metric import ApiNVD20TemporalAssociatedBaseMetric


T = TypeVar("T", bound="ApiNVD20TemporalCVSSV3")


@_attrs_define
class ApiNVD20TemporalCVSSV3:
    """
    Attributes:
        associated_base_metric_v3 (Union[Unset, ApiNVD20TemporalAssociatedBaseMetric]):
        exploit_code_maturity (Union[Unset, str]):
        remediation_level (Union[Unset, str]):
        report_confidence (Union[Unset, str]):
        temporal_score (Union[Unset, float]):
        vector_string (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    associated_base_metric_v3: Union[Unset, "ApiNVD20TemporalAssociatedBaseMetric"] = UNSET
    exploit_code_maturity: Union[Unset, str] = UNSET
    remediation_level: Union[Unset, str] = UNSET
    report_confidence: Union[Unset, str] = UNSET
    temporal_score: Union[Unset, float] = UNSET
    vector_string: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_base_metric_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.associated_base_metric_v3, Unset):
            associated_base_metric_v3 = self.associated_base_metric_v3.to_dict()

        exploit_code_maturity = self.exploit_code_maturity

        remediation_level = self.remediation_level

        report_confidence = self.report_confidence

        temporal_score = self.temporal_score

        vector_string = self.vector_string

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_base_metric_v3 is not UNSET:
            field_dict["associatedBaseMetricV3"] = associated_base_metric_v3
        if exploit_code_maturity is not UNSET:
            field_dict["exploitCodeMaturity"] = exploit_code_maturity
        if remediation_level is not UNSET:
            field_dict["remediationLevel"] = remediation_level
        if report_confidence is not UNSET:
            field_dict["reportConfidence"] = report_confidence
        if temporal_score is not UNSET:
            field_dict["temporalScore"] = temporal_score
        if vector_string is not UNSET:
            field_dict["vectorString"] = vector_string
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_temporal_associated_base_metric import ApiNVD20TemporalAssociatedBaseMetric

        d = dict(src_dict)
        _associated_base_metric_v3 = d.pop("associatedBaseMetricV3", UNSET)
        associated_base_metric_v3: Union[Unset, ApiNVD20TemporalAssociatedBaseMetric]
        if isinstance(_associated_base_metric_v3, Unset):
            associated_base_metric_v3 = UNSET
        else:
            associated_base_metric_v3 = ApiNVD20TemporalAssociatedBaseMetric.from_dict(_associated_base_metric_v3)

        exploit_code_maturity = d.pop("exploitCodeMaturity", UNSET)

        remediation_level = d.pop("remediationLevel", UNSET)

        report_confidence = d.pop("reportConfidence", UNSET)

        temporal_score = d.pop("temporalScore", UNSET)

        vector_string = d.pop("vectorString", UNSET)

        version = d.pop("version", UNSET)

        api_nvd20_temporal_cvssv3 = cls(
            associated_base_metric_v3=associated_base_metric_v3,
            exploit_code_maturity=exploit_code_maturity,
            remediation_level=remediation_level,
            report_confidence=report_confidence,
            temporal_score=temporal_score,
            vector_string=vector_string,
            version=version,
        )

        api_nvd20_temporal_cvssv3.additional_properties = d
        return api_nvd20_temporal_cvssv3

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
