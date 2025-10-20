from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_affected import AdvisoryMAffected
    from ..models.advisory_m_provider_metadata import AdvisoryMProviderMetadata
    from ..models.advisory_vulnrichment_metric import AdvisoryVulnrichmentMetric


T = TypeVar("T", bound="AdvisoryADP")


@_attrs_define
class AdvisoryADP:
    """
    Attributes:
        affected (Union[Unset, list['AdvisoryMAffected']]):
        metrics (Union[Unset, list['AdvisoryVulnrichmentMetric']]):
        provider_metadata (Union[Unset, AdvisoryMProviderMetadata]):
    """

    affected: Union[Unset, list["AdvisoryMAffected"]] = UNSET
    metrics: Union[Unset, list["AdvisoryVulnrichmentMetric"]] = UNSET
    provider_metadata: Union[Unset, "AdvisoryMProviderMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        metrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        provider_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provider_metadata, Unset):
            provider_metadata = self.provider_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if provider_metadata is not UNSET:
            field_dict["providerMetadata"] = provider_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_affected import AdvisoryMAffected
        from ..models.advisory_m_provider_metadata import AdvisoryMProviderMetadata
        from ..models.advisory_vulnrichment_metric import AdvisoryVulnrichmentMetric

        d = dict(src_dict)
        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryMAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = AdvisoryVulnrichmentMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        _provider_metadata = d.pop("providerMetadata", UNSET)
        provider_metadata: Union[Unset, AdvisoryMProviderMetadata]
        if isinstance(_provider_metadata, Unset):
            provider_metadata = UNSET
        else:
            provider_metadata = AdvisoryMProviderMetadata.from_dict(_provider_metadata)

        advisory_adp = cls(
            affected=affected,
            metrics=metrics,
            provider_metadata=provider_metadata,
        )

        advisory_adp.additional_properties = d
        return advisory_adp

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
