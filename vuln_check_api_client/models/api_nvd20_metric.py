from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20_cvss_metric_v2 import ApiNVD20CvssMetricV2
    from ..models.api_nvd20_cvss_metric_v3 import ApiNVD20CvssMetricV3
    from ..models.api_nvd20_cvss_metric_v40 import ApiNVD20CvssMetricV40


T = TypeVar("T", bound="ApiNVD20Metric")


@_attrs_define
class ApiNVD20Metric:
    """
    Attributes:
        cvss_metric_v2 (Union[Unset, list['ApiNVD20CvssMetricV2']]):
        cvss_metric_v30 (Union[Unset, list['ApiNVD20CvssMetricV3']]):
        cvss_metric_v31 (Union[Unset, list['ApiNVD20CvssMetricV3']]):
        cvss_metric_v40 (Union[Unset, list['ApiNVD20CvssMetricV40']]):
    """

    cvss_metric_v2: Union[Unset, list["ApiNVD20CvssMetricV2"]] = UNSET
    cvss_metric_v30: Union[Unset, list["ApiNVD20CvssMetricV3"]] = UNSET
    cvss_metric_v31: Union[Unset, list["ApiNVD20CvssMetricV3"]] = UNSET
    cvss_metric_v40: Union[Unset, list["ApiNVD20CvssMetricV40"]] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20_cvss_metric_v2 import ApiNVD20CvssMetricV2
        from ..models.api_nvd20_cvss_metric_v3 import ApiNVD20CvssMetricV3
        from ..models.api_nvd20_cvss_metric_v40 import ApiNVD20CvssMetricV40

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

        api_nvd20_metric = cls(
            cvss_metric_v2=cvss_metric_v2,
            cvss_metric_v30=cvss_metric_v30,
            cvss_metric_v31=cvss_metric_v31,
            cvss_metric_v40=cvss_metric_v40,
        )

        api_nvd20_metric.additional_properties = d
        return api_nvd20_metric

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
