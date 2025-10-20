from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_temporal_cvssv3 import ApiTemporalCVSSV3


T = TypeVar("T", bound="ApiTemporalMetricV3")


@_attrs_define
class ApiTemporalMetricV3:
    """
    Attributes:
        cvss_v3 (Union[Unset, ApiTemporalCVSSV3]):
    """

    cvss_v3: Union[Unset, "ApiTemporalCVSSV3"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v3, Unset):
            cvss_v3 = self.cvss_v3.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_v3 is not UNSET:
            field_dict["cvssV3"] = cvss_v3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_temporal_cvssv3 import ApiTemporalCVSSV3

        d = dict(src_dict)
        _cvss_v3 = d.pop("cvssV3", UNSET)
        cvss_v3: Union[Unset, ApiTemporalCVSSV3]
        if isinstance(_cvss_v3, Unset):
            cvss_v3 = UNSET
        else:
            cvss_v3 = ApiTemporalCVSSV3.from_dict(_cvss_v3)

        api_temporal_metric_v3 = cls(
            cvss_v3=cvss_v3,
        )

        api_temporal_metric_v3.additional_properties = d
        return api_temporal_metric_v3

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
