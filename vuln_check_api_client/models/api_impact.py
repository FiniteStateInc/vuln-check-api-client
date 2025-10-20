from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvssv40 import AdvisoryCVSSV40
    from ..models.api_base_metric_v2 import ApiBaseMetricV2
    from ..models.api_base_metric_v3 import ApiBaseMetricV3


T = TypeVar("T", bound="ApiImpact")


@_attrs_define
class ApiImpact:
    """
    Attributes:
        base_metric_v2 (Union[Unset, ApiBaseMetricV2]):
        base_metric_v3 (Union[Unset, ApiBaseMetricV3]):
        metric_v40 (Union[Unset, AdvisoryCVSSV40]):
    """

    base_metric_v2: Union[Unset, "ApiBaseMetricV2"] = UNSET
    base_metric_v3: Union[Unset, "ApiBaseMetricV3"] = UNSET
    metric_v40: Union[Unset, "AdvisoryCVSSV40"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_metric_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_metric_v2, Unset):
            base_metric_v2 = self.base_metric_v2.to_dict()

        base_metric_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_metric_v3, Unset):
            base_metric_v3 = self.base_metric_v3.to_dict()

        metric_v40: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metric_v40, Unset):
            metric_v40 = self.metric_v40.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_metric_v2 is not UNSET:
            field_dict["baseMetricV2"] = base_metric_v2
        if base_metric_v3 is not UNSET:
            field_dict["baseMetricV3"] = base_metric_v3
        if metric_v40 is not UNSET:
            field_dict["metricV40"] = metric_v40

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvssv40 import AdvisoryCVSSV40
        from ..models.api_base_metric_v2 import ApiBaseMetricV2
        from ..models.api_base_metric_v3 import ApiBaseMetricV3

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

        _metric_v40 = d.pop("metricV40", UNSET)
        metric_v40: Union[Unset, AdvisoryCVSSV40]
        if isinstance(_metric_v40, Unset):
            metric_v40 = UNSET
        else:
            metric_v40 = AdvisoryCVSSV40.from_dict(_metric_v40)

        api_impact = cls(
            base_metric_v2=base_metric_v2,
            base_metric_v3=base_metric_v3,
            metric_v40=metric_v40,
        )

        api_impact.additional_properties = d
        return api_impact

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
