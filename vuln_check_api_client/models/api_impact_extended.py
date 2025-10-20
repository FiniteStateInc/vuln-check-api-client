from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvssv40 import AdvisoryCVSSV40
    from ..models.advisory_cvssv40_threat import AdvisoryCVSSV40Threat
    from ..models.api_base_metric_v2 import ApiBaseMetricV2
    from ..models.api_base_metric_v3 import ApiBaseMetricV3
    from ..models.api_epss import ApiEPSS
    from ..models.api_ssvc import ApiSSVC
    from ..models.api_temporal_metric_v2 import ApiTemporalMetricV2
    from ..models.api_temporal_metric_v3 import ApiTemporalMetricV3


T = TypeVar("T", bound="ApiImpactExtended")


@_attrs_define
class ApiImpactExtended:
    """
    Attributes:
        base_metric_v2 (Union[Unset, ApiBaseMetricV2]):
        base_metric_v3 (Union[Unset, ApiBaseMetricV3]):
        corrected_base_metric_v3 (Union[Unset, ApiBaseMetricV3]):
        epss (Union[Unset, ApiEPSS]):
        metric_v40 (Union[Unset, AdvisoryCVSSV40]):
        ssvc (Union[Unset, list['ApiSSVC']]):
        temporal_metric_v2 (Union[Unset, ApiTemporalMetricV2]):
        temporal_metric_v3 (Union[Unset, ApiTemporalMetricV3]):
        temporal_v3_corrected (Union[Unset, ApiTemporalMetricV3]):
        threat_metric_v40 (Union[Unset, AdvisoryCVSSV40Threat]):
    """

    base_metric_v2: Union[Unset, "ApiBaseMetricV2"] = UNSET
    base_metric_v3: Union[Unset, "ApiBaseMetricV3"] = UNSET
    corrected_base_metric_v3: Union[Unset, "ApiBaseMetricV3"] = UNSET
    epss: Union[Unset, "ApiEPSS"] = UNSET
    metric_v40: Union[Unset, "AdvisoryCVSSV40"] = UNSET
    ssvc: Union[Unset, list["ApiSSVC"]] = UNSET
    temporal_metric_v2: Union[Unset, "ApiTemporalMetricV2"] = UNSET
    temporal_metric_v3: Union[Unset, "ApiTemporalMetricV3"] = UNSET
    temporal_v3_corrected: Union[Unset, "ApiTemporalMetricV3"] = UNSET
    threat_metric_v40: Union[Unset, "AdvisoryCVSSV40Threat"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_metric_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_metric_v2, Unset):
            base_metric_v2 = self.base_metric_v2.to_dict()

        base_metric_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_metric_v3, Unset):
            base_metric_v3 = self.base_metric_v3.to_dict()

        corrected_base_metric_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.corrected_base_metric_v3, Unset):
            corrected_base_metric_v3 = self.corrected_base_metric_v3.to_dict()

        epss: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.epss, Unset):
            epss = self.epss.to_dict()

        metric_v40: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metric_v40, Unset):
            metric_v40 = self.metric_v40.to_dict()

        ssvc: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ssvc, Unset):
            ssvc = []
            for ssvc_item_data in self.ssvc:
                ssvc_item = ssvc_item_data.to_dict()
                ssvc.append(ssvc_item)

        temporal_metric_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_metric_v2, Unset):
            temporal_metric_v2 = self.temporal_metric_v2.to_dict()

        temporal_metric_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_metric_v3, Unset):
            temporal_metric_v3 = self.temporal_metric_v3.to_dict()

        temporal_v3_corrected: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporal_v3_corrected, Unset):
            temporal_v3_corrected = self.temporal_v3_corrected.to_dict()

        threat_metric_v40: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.threat_metric_v40, Unset):
            threat_metric_v40 = self.threat_metric_v40.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_metric_v2 is not UNSET:
            field_dict["baseMetricV2"] = base_metric_v2
        if base_metric_v3 is not UNSET:
            field_dict["baseMetricV3"] = base_metric_v3
        if corrected_base_metric_v3 is not UNSET:
            field_dict["correctedBaseMetricV3"] = corrected_base_metric_v3
        if epss is not UNSET:
            field_dict["epss"] = epss
        if metric_v40 is not UNSET:
            field_dict["metricV40"] = metric_v40
        if ssvc is not UNSET:
            field_dict["ssvc"] = ssvc
        if temporal_metric_v2 is not UNSET:
            field_dict["temporalMetricV2"] = temporal_metric_v2
        if temporal_metric_v3 is not UNSET:
            field_dict["temporalMetricV3"] = temporal_metric_v3
        if temporal_v3_corrected is not UNSET:
            field_dict["temporalV3Corrected"] = temporal_v3_corrected
        if threat_metric_v40 is not UNSET:
            field_dict["threatMetricV40"] = threat_metric_v40

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvssv40 import AdvisoryCVSSV40
        from ..models.advisory_cvssv40_threat import AdvisoryCVSSV40Threat
        from ..models.api_base_metric_v2 import ApiBaseMetricV2
        from ..models.api_base_metric_v3 import ApiBaseMetricV3
        from ..models.api_epss import ApiEPSS
        from ..models.api_ssvc import ApiSSVC
        from ..models.api_temporal_metric_v2 import ApiTemporalMetricV2
        from ..models.api_temporal_metric_v3 import ApiTemporalMetricV3

        d = dict(src_dict)
        _base_metric_v2 = d.pop("baseMetricV2", UNSET)
        base_metric_v2: Union[Unset, ApiBaseMetricV2]
        if isinstance(_base_metric_v2, Unset):
            base_metric_v2 = UNSET
        else:
            base_metric_v2 = ApiBaseMetricV2.from_dict(_base_metric_v2)

        _base_metric_v3 = d.pop("baseMetricV3", UNSET)
        base_metric_v3: Union[Unset, ApiBaseMetricV3]
        if isinstance(_base_metric_v3, Unset):
            base_metric_v3 = UNSET
        else:
            base_metric_v3 = ApiBaseMetricV3.from_dict(_base_metric_v3)

        _corrected_base_metric_v3 = d.pop("correctedBaseMetricV3", UNSET)
        corrected_base_metric_v3: Union[Unset, ApiBaseMetricV3]
        if isinstance(_corrected_base_metric_v3, Unset):
            corrected_base_metric_v3 = UNSET
        else:
            corrected_base_metric_v3 = ApiBaseMetricV3.from_dict(_corrected_base_metric_v3)

        _epss = d.pop("epss", UNSET)
        epss: Union[Unset, ApiEPSS]
        if isinstance(_epss, Unset):
            epss = UNSET
        else:
            epss = ApiEPSS.from_dict(_epss)

        _metric_v40 = d.pop("metricV40", UNSET)
        metric_v40: Union[Unset, AdvisoryCVSSV40]
        if isinstance(_metric_v40, Unset):
            metric_v40 = UNSET
        else:
            metric_v40 = AdvisoryCVSSV40.from_dict(_metric_v40)

        ssvc = []
        _ssvc = d.pop("ssvc", UNSET)
        for ssvc_item_data in _ssvc or []:
            ssvc_item = ApiSSVC.from_dict(ssvc_item_data)

            ssvc.append(ssvc_item)

        _temporal_metric_v2 = d.pop("temporalMetricV2", UNSET)
        temporal_metric_v2: Union[Unset, ApiTemporalMetricV2]
        if isinstance(_temporal_metric_v2, Unset):
            temporal_metric_v2 = UNSET
        else:
            temporal_metric_v2 = ApiTemporalMetricV2.from_dict(_temporal_metric_v2)

        _temporal_metric_v3 = d.pop("temporalMetricV3", UNSET)
        temporal_metric_v3: Union[Unset, ApiTemporalMetricV3]
        if isinstance(_temporal_metric_v3, Unset):
            temporal_metric_v3 = UNSET
        else:
            temporal_metric_v3 = ApiTemporalMetricV3.from_dict(_temporal_metric_v3)

        _temporal_v3_corrected = d.pop("temporalV3Corrected", UNSET)
        temporal_v3_corrected: Union[Unset, ApiTemporalMetricV3]
        if isinstance(_temporal_v3_corrected, Unset):
            temporal_v3_corrected = UNSET
        else:
            temporal_v3_corrected = ApiTemporalMetricV3.from_dict(_temporal_v3_corrected)

        _threat_metric_v40 = d.pop("threatMetricV40", UNSET)
        threat_metric_v40: Union[Unset, AdvisoryCVSSV40Threat]
        if isinstance(_threat_metric_v40, Unset):
            threat_metric_v40 = UNSET
        else:
            threat_metric_v40 = AdvisoryCVSSV40Threat.from_dict(_threat_metric_v40)

        api_impact_extended = cls(
            base_metric_v2=base_metric_v2,
            base_metric_v3=base_metric_v3,
            corrected_base_metric_v3=corrected_base_metric_v3,
            epss=epss,
            metric_v40=metric_v40,
            ssvc=ssvc,
            temporal_metric_v2=temporal_metric_v2,
            temporal_metric_v3=temporal_metric_v3,
            temporal_v3_corrected=temporal_v3_corrected,
            threat_metric_v40=threat_metric_v40,
        )

        api_impact_extended.additional_properties = d
        return api_impact_extended

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
