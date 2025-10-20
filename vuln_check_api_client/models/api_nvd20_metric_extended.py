from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_epss import ApiEPSS
    from ..models.api_nvd20_cvss_metric_v2 import ApiNVD20CvssMetricV2
    from ..models.api_nvd20_cvss_metric_v3 import ApiNVD20CvssMetricV3
    from ..models.api_nvd20_cvss_metric_v40 import ApiNVD20CvssMetricV40
    from ..models.api_nvd20_temporal_cvssv2 import ApiNVD20TemporalCVSSV2
    from ..models.api_nvd20_temporal_cvssv3 import ApiNVD20TemporalCVSSV3
    from ..models.api_nvd20_threat_cvssv40 import ApiNVD20ThreatCVSSV40
    from ..models.api_ssvc import ApiSSVC


T = TypeVar("T", bound="ApiNVD20MetricExtended")


@_attrs_define
class ApiNVD20MetricExtended:
    """
    Attributes:
        cvss_metric_v2 (Union[Unset, list['ApiNVD20CvssMetricV2']]):
        cvss_metric_v30 (Union[Unset, list['ApiNVD20CvssMetricV3']]):
        cvss_metric_v31 (Union[Unset, list['ApiNVD20CvssMetricV3']]):
        cvss_metric_v40 (Union[Unset, list['ApiNVD20CvssMetricV40']]):
        epss (Union[Unset, ApiEPSS]):
        ssvc (Union[Unset, list['ApiSSVC']]):
        temporal_cvssv2 (Union[Unset, ApiNVD20TemporalCVSSV2]):
        temporal_cvssv2_secondary (Union[Unset, list['ApiNVD20TemporalCVSSV2']]):
        temporal_cvssv30 (Union[Unset, ApiNVD20TemporalCVSSV3]):
        temporal_cvssv30_secondary (Union[Unset, list['ApiNVD20TemporalCVSSV3']]):
        temporal_cvssv31 (Union[Unset, ApiNVD20TemporalCVSSV3]):
        temporal_cvssv31_secondary (Union[Unset, list['ApiNVD20TemporalCVSSV3']]):
        threat_cvssv40 (Union[Unset, ApiNVD20ThreatCVSSV40]):
        threat_cvssv40_secondary (Union[Unset, list['ApiNVD20ThreatCVSSV40']]):
    """

    cvss_metric_v2: Union[Unset, list["ApiNVD20CvssMetricV2"]] = UNSET
    cvss_metric_v30: Union[Unset, list["ApiNVD20CvssMetricV3"]] = UNSET
    cvss_metric_v31: Union[Unset, list["ApiNVD20CvssMetricV3"]] = UNSET
    cvss_metric_v40: Union[Unset, list["ApiNVD20CvssMetricV40"]] = UNSET
    epss: Union[Unset, "ApiEPSS"] = UNSET
    ssvc: Union[Unset, list["ApiSSVC"]] = UNSET
    temporal_cvssv2: Union[Unset, "ApiNVD20TemporalCVSSV2"] = UNSET
    temporal_cvssv2_secondary: Union[Unset, list["ApiNVD20TemporalCVSSV2"]] = UNSET
    temporal_cvssv30: Union[Unset, "ApiNVD20TemporalCVSSV3"] = UNSET
    temporal_cvssv30_secondary: Union[Unset, list["ApiNVD20TemporalCVSSV3"]] = UNSET
    temporal_cvssv31: Union[Unset, "ApiNVD20TemporalCVSSV3"] = UNSET
    temporal_cvssv31_secondary: Union[Unset, list["ApiNVD20TemporalCVSSV3"]] = UNSET
    threat_cvssv40: Union[Unset, "ApiNVD20ThreatCVSSV40"] = UNSET
    threat_cvssv40_secondary: Union[Unset, list["ApiNVD20ThreatCVSSV40"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_metric_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_metric_v2, Unset):
            cvss_metric_v2 = []
            for cvss_metric_v2_item_data in self.cvss_metric_v2:
                cvss_metric_v2_item = cvss_metric_v2_item_data.to_dict()
                cvss_metric_v2.append(cvss_metric_v2_item)

        cvss_metric_v30: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_metric_v30, Unset):
            cvss_metric_v30 = []
            for cvss_metric_v30_item_data in self.cvss_metric_v30:
                cvss_metric_v30_item = cvss_metric_v30_item_data.to_dict()
                cvss_metric_v30.append(cvss_metric_v30_item)

        cvss_metric_v31: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_metric_v31, Unset):
            cvss_metric_v31 = []
            for cvss_metric_v31_item_data in self.cvss_metric_v31:
                cvss_metric_v31_item = cvss_metric_v31_item_data.to_dict()
                cvss_metric_v31.append(cvss_metric_v31_item)

        cvss_metric_v40: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cvss_metric_v40, Unset):
            cvss_metric_v40 = []
            for cvss_metric_v40_item_data in self.cvss_metric_v40:
                cvss_metric_v40_item = cvss_metric_v40_item_data.to_dict()
                cvss_metric_v40.append(cvss_metric_v40_item)

        epss: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.epss, Unset):
            epss = self.epss.to_dict()

        ssvc: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ssvc, Unset):
            ssvc = []
            for ssvc_item_data in self.ssvc:
                ssvc_item = ssvc_item_data.to_dict()
                ssvc.append(ssvc_item)

        temporal_cvssv2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_cvssv2, Unset):
            temporal_cvssv2 = self.temporal_cvssv2.to_dict()

        temporal_cvssv2_secondary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.temporal_cvssv2_secondary, Unset):
            temporal_cvssv2_secondary = []
            for temporal_cvssv2_secondary_item_data in self.temporal_cvssv2_secondary:
                temporal_cvssv2_secondary_item = temporal_cvssv2_secondary_item_data.to_dict()
                temporal_cvssv2_secondary.append(temporal_cvssv2_secondary_item)

        temporal_cvssv30: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_cvssv30, Unset):
            temporal_cvssv30 = self.temporal_cvssv30.to_dict()

        temporal_cvssv30_secondary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.temporal_cvssv30_secondary, Unset):
            temporal_cvssv30_secondary = []
            for temporal_cvssv30_secondary_item_data in self.temporal_cvssv30_secondary:
                temporal_cvssv30_secondary_item = temporal_cvssv30_secondary_item_data.to_dict()
                temporal_cvssv30_secondary.append(temporal_cvssv30_secondary_item)

        temporal_cvssv31: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_cvssv31, Unset):
            temporal_cvssv31 = self.temporal_cvssv31.to_dict()

        temporal_cvssv31_secondary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.temporal_cvssv31_secondary, Unset):
            temporal_cvssv31_secondary = []
            for temporal_cvssv31_secondary_item_data in self.temporal_cvssv31_secondary:
                temporal_cvssv31_secondary_item = temporal_cvssv31_secondary_item_data.to_dict()
                temporal_cvssv31_secondary.append(temporal_cvssv31_secondary_item)

        threat_cvssv40: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.threat_cvssv40, Unset):
            threat_cvssv40 = self.threat_cvssv40.to_dict()

        threat_cvssv40_secondary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.threat_cvssv40_secondary, Unset):
            threat_cvssv40_secondary = []
            for threat_cvssv40_secondary_item_data in self.threat_cvssv40_secondary:
                threat_cvssv40_secondary_item = threat_cvssv40_secondary_item_data.to_dict()
                threat_cvssv40_secondary.append(threat_cvssv40_secondary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_metric_v2 is not UNSET:
            field_dict["cvssMetricV2"] = cvss_metric_v2
        if cvss_metric_v30 is not UNSET:
            field_dict["cvssMetricV30"] = cvss_metric_v30
        if cvss_metric_v31 is not UNSET:
            field_dict["cvssMetricV31"] = cvss_metric_v31
        if cvss_metric_v40 is not UNSET:
            field_dict["cvssMetricV40"] = cvss_metric_v40
        if epss is not UNSET:
            field_dict["epss"] = epss
        if ssvc is not UNSET:
            field_dict["ssvc"] = ssvc
        if temporal_cvssv2 is not UNSET:
            field_dict["temporalCVSSV2"] = temporal_cvssv2
        if temporal_cvssv2_secondary is not UNSET:
            field_dict["temporalCVSSV2Secondary"] = temporal_cvssv2_secondary
        if temporal_cvssv30 is not UNSET:
            field_dict["temporalCVSSV30"] = temporal_cvssv30
        if temporal_cvssv30_secondary is not UNSET:
            field_dict["temporalCVSSV30Secondary"] = temporal_cvssv30_secondary
        if temporal_cvssv31 is not UNSET:
            field_dict["temporalCVSSV31"] = temporal_cvssv31
        if temporal_cvssv31_secondary is not UNSET:
            field_dict["temporalCVSSV31Secondary"] = temporal_cvssv31_secondary
        if threat_cvssv40 is not UNSET:
            field_dict["threatCVSSV40"] = threat_cvssv40
        if threat_cvssv40_secondary is not UNSET:
            field_dict["threatCVSSV40Secondary"] = threat_cvssv40_secondary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_epss import ApiEPSS
        from ..models.api_nvd20_cvss_metric_v2 import ApiNVD20CvssMetricV2
        from ..models.api_nvd20_cvss_metric_v3 import ApiNVD20CvssMetricV3
        from ..models.api_nvd20_cvss_metric_v40 import ApiNVD20CvssMetricV40
        from ..models.api_nvd20_temporal_cvssv2 import ApiNVD20TemporalCVSSV2
        from ..models.api_nvd20_temporal_cvssv3 import ApiNVD20TemporalCVSSV3
        from ..models.api_nvd20_threat_cvssv40 import ApiNVD20ThreatCVSSV40
        from ..models.api_ssvc import ApiSSVC

        d = dict(src_dict)
        cvss_metric_v2 = []
        _cvss_metric_v2 = d.pop("cvssMetricV2", UNSET)
        for cvss_metric_v2_item_data in _cvss_metric_v2 or []:
            cvss_metric_v2_item = ApiNVD20CvssMetricV2.from_dict(cvss_metric_v2_item_data)

            cvss_metric_v2.append(cvss_metric_v2_item)

        cvss_metric_v30 = []
        _cvss_metric_v30 = d.pop("cvssMetricV30", UNSET)
        for cvss_metric_v30_item_data in _cvss_metric_v30 or []:
            cvss_metric_v30_item = ApiNVD20CvssMetricV3.from_dict(cvss_metric_v30_item_data)

            cvss_metric_v30.append(cvss_metric_v30_item)

        cvss_metric_v31 = []
        _cvss_metric_v31 = d.pop("cvssMetricV31", UNSET)
        for cvss_metric_v31_item_data in _cvss_metric_v31 or []:
            cvss_metric_v31_item = ApiNVD20CvssMetricV3.from_dict(cvss_metric_v31_item_data)

            cvss_metric_v31.append(cvss_metric_v31_item)

        cvss_metric_v40 = []
        _cvss_metric_v40 = d.pop("cvssMetricV40", UNSET)
        for cvss_metric_v40_item_data in _cvss_metric_v40 or []:
            cvss_metric_v40_item = ApiNVD20CvssMetricV40.from_dict(cvss_metric_v40_item_data)

            cvss_metric_v40.append(cvss_metric_v40_item)

        _epss = d.pop("epss", UNSET)
        epss: Union[Unset, ApiEPSS]
        if isinstance(_epss, Unset):
            epss = UNSET
        else:
            epss = ApiEPSS.from_dict(_epss)

        ssvc = []
        _ssvc = d.pop("ssvc", UNSET)
        for ssvc_item_data in _ssvc or []:
            ssvc_item = ApiSSVC.from_dict(ssvc_item_data)

            ssvc.append(ssvc_item)

        _temporal_cvssv2 = d.pop("temporalCVSSV2", UNSET)
        temporal_cvssv2: Union[Unset, ApiNVD20TemporalCVSSV2]
        if isinstance(_temporal_cvssv2, Unset):
            temporal_cvssv2 = UNSET
        else:
            temporal_cvssv2 = ApiNVD20TemporalCVSSV2.from_dict(_temporal_cvssv2)

        temporal_cvssv2_secondary = []
        _temporal_cvssv2_secondary = d.pop("temporalCVSSV2Secondary", UNSET)
        for temporal_cvssv2_secondary_item_data in _temporal_cvssv2_secondary or []:
            temporal_cvssv2_secondary_item = ApiNVD20TemporalCVSSV2.from_dict(temporal_cvssv2_secondary_item_data)

            temporal_cvssv2_secondary.append(temporal_cvssv2_secondary_item)

        _temporal_cvssv30 = d.pop("temporalCVSSV30", UNSET)
        temporal_cvssv30: Union[Unset, ApiNVD20TemporalCVSSV3]
        if isinstance(_temporal_cvssv30, Unset):
            temporal_cvssv30 = UNSET
        else:
            temporal_cvssv30 = ApiNVD20TemporalCVSSV3.from_dict(_temporal_cvssv30)

        temporal_cvssv30_secondary = []
        _temporal_cvssv30_secondary = d.pop("temporalCVSSV30Secondary", UNSET)
        for temporal_cvssv30_secondary_item_data in _temporal_cvssv30_secondary or []:
            temporal_cvssv30_secondary_item = ApiNVD20TemporalCVSSV3.from_dict(temporal_cvssv30_secondary_item_data)

            temporal_cvssv30_secondary.append(temporal_cvssv30_secondary_item)

        _temporal_cvssv31 = d.pop("temporalCVSSV31", UNSET)
        temporal_cvssv31: Union[Unset, ApiNVD20TemporalCVSSV3]
        if isinstance(_temporal_cvssv31, Unset):
            temporal_cvssv31 = UNSET
        else:
            temporal_cvssv31 = ApiNVD20TemporalCVSSV3.from_dict(_temporal_cvssv31)

        temporal_cvssv31_secondary = []
        _temporal_cvssv31_secondary = d.pop("temporalCVSSV31Secondary", UNSET)
        for temporal_cvssv31_secondary_item_data in _temporal_cvssv31_secondary or []:
            temporal_cvssv31_secondary_item = ApiNVD20TemporalCVSSV3.from_dict(temporal_cvssv31_secondary_item_data)

            temporal_cvssv31_secondary.append(temporal_cvssv31_secondary_item)

        _threat_cvssv40 = d.pop("threatCVSSV40", UNSET)
        threat_cvssv40: Union[Unset, ApiNVD20ThreatCVSSV40]
        if isinstance(_threat_cvssv40, Unset):
            threat_cvssv40 = UNSET
        else:
            threat_cvssv40 = ApiNVD20ThreatCVSSV40.from_dict(_threat_cvssv40)

        threat_cvssv40_secondary = []
        _threat_cvssv40_secondary = d.pop("threatCVSSV40Secondary", UNSET)
        for threat_cvssv40_secondary_item_data in _threat_cvssv40_secondary or []:
            threat_cvssv40_secondary_item = ApiNVD20ThreatCVSSV40.from_dict(threat_cvssv40_secondary_item_data)

            threat_cvssv40_secondary.append(threat_cvssv40_secondary_item)

        api_nvd20_metric_extended = cls(
            cvss_metric_v2=cvss_metric_v2,
            cvss_metric_v30=cvss_metric_v30,
            cvss_metric_v31=cvss_metric_v31,
            cvss_metric_v40=cvss_metric_v40,
            epss=epss,
            ssvc=ssvc,
            temporal_cvssv2=temporal_cvssv2,
            temporal_cvssv2_secondary=temporal_cvssv2_secondary,
            temporal_cvssv30=temporal_cvssv30,
            temporal_cvssv30_secondary=temporal_cvssv30_secondary,
            temporal_cvssv31=temporal_cvssv31,
            temporal_cvssv31_secondary=temporal_cvssv31_secondary,
            threat_cvssv40=threat_cvssv40,
            threat_cvssv40_secondary=threat_cvssv40_secondary,
        )

        api_nvd20_metric_extended.additional_properties = d
        return api_nvd20_metric_extended

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
