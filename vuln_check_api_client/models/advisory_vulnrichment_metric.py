from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_vulnrichment_other import AdvisoryVulnrichmentOther


T = TypeVar("T", bound="AdvisoryVulnrichmentMetric")


@_attrs_define
class AdvisoryVulnrichmentMetric:
    """
    Attributes:
        other (Union[Unset, AdvisoryVulnrichmentOther]):
    """

    other: Union[Unset, "AdvisoryVulnrichmentOther"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        other: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_vulnrichment_other import AdvisoryVulnrichmentOther

        d = dict(src_dict)
        _other = d.pop("other", UNSET)
        other: Union[Unset, AdvisoryVulnrichmentOther]
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = AdvisoryVulnrichmentOther.from_dict(_other)

        advisory_vulnrichment_metric = cls(
            other=other,
        )

        advisory_vulnrichment_metric.additional_properties = d
        return advisory_vulnrichment_metric

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
