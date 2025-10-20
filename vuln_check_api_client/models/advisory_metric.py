from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_cvss_v20 import AdvisoryMCvssV20
    from ..models.advisory_m_cvss_v30 import AdvisoryMCvssV30
    from ..models.advisory_m_cvss_v31 import AdvisoryMCvssV31
    from ..models.advisory_m_cvss_v40 import AdvisoryMCvssV40
    from ..models.advisory_metrics_other import AdvisoryMetricsOther


T = TypeVar("T", bound="AdvisoryMetric")


@_attrs_define
class AdvisoryMetric:
    """
    Attributes:
        cvss_v2_0 (Union[Unset, AdvisoryMCvssV20]):
        cvss_v3_0 (Union[Unset, AdvisoryMCvssV30]):
        cvss_v3_1 (Union[Unset, AdvisoryMCvssV31]):
        cvss_v4_0 (Union[Unset, AdvisoryMCvssV40]):
        format_ (Union[Unset, str]):
        other (Union[Unset, AdvisoryMetricsOther]):
    """

    cvss_v2_0: Union[Unset, "AdvisoryMCvssV20"] = UNSET
    cvss_v3_0: Union[Unset, "AdvisoryMCvssV30"] = UNSET
    cvss_v3_1: Union[Unset, "AdvisoryMCvssV31"] = UNSET
    cvss_v4_0: Union[Unset, "AdvisoryMCvssV40"] = UNSET
    format_: Union[Unset, str] = UNSET
    other: Union[Unset, "AdvisoryMetricsOther"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_v2_0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v2_0, Unset):
            cvss_v2_0 = self.cvss_v2_0.to_dict()

        cvss_v3_0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v3_0, Unset):
            cvss_v3_0 = self.cvss_v3_0.to_dict()

        cvss_v3_1: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v3_1, Unset):
            cvss_v3_1 = self.cvss_v3_1.to_dict()

        cvss_v4_0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v4_0, Unset):
            cvss_v4_0 = self.cvss_v4_0.to_dict()

        format_ = self.format_

        other: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_v2_0 is not UNSET:
            field_dict["cvssV2_0"] = cvss_v2_0
        if cvss_v3_0 is not UNSET:
            field_dict["cvssV3_0"] = cvss_v3_0
        if cvss_v3_1 is not UNSET:
            field_dict["cvssV3_1"] = cvss_v3_1
        if cvss_v4_0 is not UNSET:
            field_dict["cvssV4_0"] = cvss_v4_0
        if format_ is not UNSET:
            field_dict["format"] = format_
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_cvss_v20 import AdvisoryMCvssV20
        from ..models.advisory_m_cvss_v30 import AdvisoryMCvssV30
        from ..models.advisory_m_cvss_v31 import AdvisoryMCvssV31
        from ..models.advisory_m_cvss_v40 import AdvisoryMCvssV40
        from ..models.advisory_metrics_other import AdvisoryMetricsOther

        d = dict(src_dict)
        _cvss_v2_0 = d.pop("cvssV2_0", UNSET)
        cvss_v2_0: Union[Unset, AdvisoryMCvssV20]
        if isinstance(_cvss_v2_0, Unset):
            cvss_v2_0 = UNSET
        else:
            cvss_v2_0 = AdvisoryMCvssV20.from_dict(_cvss_v2_0)

        _cvss_v3_0 = d.pop("cvssV3_0", UNSET)
        cvss_v3_0: Union[Unset, AdvisoryMCvssV30]
        if isinstance(_cvss_v3_0, Unset):
            cvss_v3_0 = UNSET
        else:
            cvss_v3_0 = AdvisoryMCvssV30.from_dict(_cvss_v3_0)

        _cvss_v3_1 = d.pop("cvssV3_1", UNSET)
        cvss_v3_1: Union[Unset, AdvisoryMCvssV31]
        if isinstance(_cvss_v3_1, Unset):
            cvss_v3_1 = UNSET
        else:
            cvss_v3_1 = AdvisoryMCvssV31.from_dict(_cvss_v3_1)

        _cvss_v4_0 = d.pop("cvssV4_0", UNSET)
        cvss_v4_0: Union[Unset, AdvisoryMCvssV40]
        if isinstance(_cvss_v4_0, Unset):
            cvss_v4_0 = UNSET
        else:
            cvss_v4_0 = AdvisoryMCvssV40.from_dict(_cvss_v4_0)

        format_ = d.pop("format", UNSET)

        _other = d.pop("other", UNSET)
        other: Union[Unset, AdvisoryMetricsOther]
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = AdvisoryMetricsOther.from_dict(_other)

        advisory_metric = cls(
            cvss_v2_0=cvss_v2_0,
            cvss_v3_0=cvss_v3_0,
            cvss_v3_1=cvss_v3_1,
            cvss_v4_0=cvss_v4_0,
            format_=format_,
            other=other,
        )

        advisory_metric.additional_properties = d
        return advisory_metric

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
