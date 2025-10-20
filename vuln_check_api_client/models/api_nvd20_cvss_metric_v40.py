from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvssv40 import AdvisoryCVSSV40


T = TypeVar("T", bound="ApiNVD20CvssMetricV40")


@_attrs_define
class ApiNVD20CvssMetricV40:
    """
    Attributes:
        cvss_data (Union[Unset, AdvisoryCVSSV40]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    cvss_data: Union[Unset, "AdvisoryCVSSV40"] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_data, Unset):
            cvss_data = self.cvss_data.to_dict()

        source = self.source

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_data is not UNSET:
            field_dict["cvssData"] = cvss_data
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvssv40 import AdvisoryCVSSV40

        d = dict(src_dict)
        _cvss_data = d.pop("cvssData", UNSET)
        cvss_data: Union[Unset, AdvisoryCVSSV40]
        if isinstance(_cvss_data, Unset):
            cvss_data = UNSET
        else:
            cvss_data = AdvisoryCVSSV40.from_dict(_cvss_data)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        api_nvd20_cvss_metric_v40 = cls(
            cvss_data=cvss_data,
            source=source,
            type_=type_,
        )

        api_nvd20_cvss_metric_v40.additional_properties = d
        return api_nvd20_cvss_metric_v40

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
