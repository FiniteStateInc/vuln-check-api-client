from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_credit import AdvisoryCredit
    from ..models.advisory_impact import AdvisoryImpact
    from ..models.advisory_m_affected import AdvisoryMAffected
    from ..models.advisory_m_descriptions import AdvisoryMDescriptions
    from ..models.advisory_m_problem_types import AdvisoryMProblemTypes
    from ..models.advisory_m_provider_metadata import AdvisoryMProviderMetadata
    from ..models.advisory_m_reference import AdvisoryMReference
    from ..models.advisory_mcpe_applicability import AdvisoryMCPEApplicability
    from ..models.advisory_metric import AdvisoryMetric
    from ..models.advisory_timeline import AdvisoryTimeline


T = TypeVar("T", bound="AdvisoryMCna")


@_attrs_define
class AdvisoryMCna:
    """
    Attributes:
        affected (Union[Unset, list['AdvisoryMAffected']]):
        cpe_applicability (Union[Unset, list['AdvisoryMCPEApplicability']]):
        credits_ (Union[Unset, list['AdvisoryCredit']]):
        descriptions (Union[Unset, list['AdvisoryMDescriptions']]):
        impacts (Union[Unset, list['AdvisoryImpact']]):
        metrics (Union[Unset, list['AdvisoryMetric']]):
        problem_types (Union[Unset, list['AdvisoryMProblemTypes']]):
        provider_metadata (Union[Unset, AdvisoryMProviderMetadata]):
        references (Union[Unset, list['AdvisoryMReference']]):
        tags (Union[Unset, list[str]]):
        timeline (Union[Unset, list['AdvisoryTimeline']]):
        title (Union[Unset, str]):
    """

    affected: Union[Unset, list["AdvisoryMAffected"]] = UNSET
    cpe_applicability: Union[Unset, list["AdvisoryMCPEApplicability"]] = UNSET
    credits_: Union[Unset, list["AdvisoryCredit"]] = UNSET
    descriptions: Union[Unset, list["AdvisoryMDescriptions"]] = UNSET
    impacts: Union[Unset, list["AdvisoryImpact"]] = UNSET
    metrics: Union[Unset, list["AdvisoryMetric"]] = UNSET
    problem_types: Union[Unset, list["AdvisoryMProblemTypes"]] = UNSET
    provider_metadata: Union[Unset, "AdvisoryMProviderMetadata"] = UNSET
    references: Union[Unset, list["AdvisoryMReference"]] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    timeline: Union[Unset, list["AdvisoryTimeline"]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        cpe_applicability: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cpe_applicability, Unset):
            cpe_applicability = []
            for cpe_applicability_item_data in self.cpe_applicability:
                cpe_applicability_item = cpe_applicability_item_data.to_dict()
                cpe_applicability.append(cpe_applicability_item)

        credits_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = []
            for credits_item_data in self.credits_:
                credits_item = credits_item_data.to_dict()
                credits_.append(credits_item)

        descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)

        impacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.impacts, Unset):
            impacts = []
            for impacts_item_data in self.impacts:
                impacts_item = impacts_item_data.to_dict()
                impacts.append(impacts_item)

        metrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        problem_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.problem_types, Unset):
            problem_types = []
            for problem_types_item_data in self.problem_types:
                problem_types_item = problem_types_item_data.to_dict()
                problem_types.append(problem_types_item)

        provider_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provider_metadata, Unset):
            provider_metadata = self.provider_metadata.to_dict()

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        timeline: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cpe_applicability is not UNSET:
            field_dict["cpeApplicability"] = cpe_applicability
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if impacts is not UNSET:
            field_dict["impacts"] = impacts
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if problem_types is not UNSET:
            field_dict["problemTypes"] = problem_types
        if provider_metadata is not UNSET:
            field_dict["providerMetadata"] = provider_metadata
        if references is not UNSET:
            field_dict["references"] = references
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_credit import AdvisoryCredit
        from ..models.advisory_impact import AdvisoryImpact
        from ..models.advisory_m_affected import AdvisoryMAffected
        from ..models.advisory_m_descriptions import AdvisoryMDescriptions
        from ..models.advisory_m_problem_types import AdvisoryMProblemTypes
        from ..models.advisory_m_provider_metadata import AdvisoryMProviderMetadata
        from ..models.advisory_m_reference import AdvisoryMReference
        from ..models.advisory_mcpe_applicability import AdvisoryMCPEApplicability
        from ..models.advisory_metric import AdvisoryMetric
        from ..models.advisory_timeline import AdvisoryTimeline

        d = dict(src_dict)
        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryMAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        cpe_applicability = []
        _cpe_applicability = d.pop("cpeApplicability", UNSET)
        for cpe_applicability_item_data in _cpe_applicability or []:
            cpe_applicability_item = AdvisoryMCPEApplicability.from_dict(cpe_applicability_item_data)

            cpe_applicability.append(cpe_applicability_item)

        credits_ = []
        _credits_ = d.pop("credits", UNSET)
        for credits_item_data in _credits_ or []:
            credits_item = AdvisoryCredit.from_dict(credits_item_data)

            credits_.append(credits_item)

        descriptions = []
        _descriptions = d.pop("descriptions", UNSET)
        for descriptions_item_data in _descriptions or []:
            descriptions_item = AdvisoryMDescriptions.from_dict(descriptions_item_data)

            descriptions.append(descriptions_item)

        impacts = []
        _impacts = d.pop("impacts", UNSET)
        for impacts_item_data in _impacts or []:
            impacts_item = AdvisoryImpact.from_dict(impacts_item_data)

            impacts.append(impacts_item)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = AdvisoryMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        problem_types = []
        _problem_types = d.pop("problemTypes", UNSET)
        for problem_types_item_data in _problem_types or []:
            problem_types_item = AdvisoryMProblemTypes.from_dict(problem_types_item_data)

            problem_types.append(problem_types_item)

        _provider_metadata = d.pop("providerMetadata", UNSET)
        provider_metadata: Union[Unset, AdvisoryMProviderMetadata]
        if isinstance(_provider_metadata, Unset):
            provider_metadata = UNSET
        else:
            provider_metadata = AdvisoryMProviderMetadata.from_dict(_provider_metadata)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryMReference.from_dict(references_item_data)

            references.append(references_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        timeline = []
        _timeline = d.pop("timeline", UNSET)
        for timeline_item_data in _timeline or []:
            timeline_item = AdvisoryTimeline.from_dict(timeline_item_data)

            timeline.append(timeline_item)

        title = d.pop("title", UNSET)

        advisory_m_cna = cls(
            affected=affected,
            cpe_applicability=cpe_applicability,
            credits_=credits_,
            descriptions=descriptions,
            impacts=impacts,
            metrics=metrics,
            problem_types=problem_types,
            provider_metadata=provider_metadata,
            references=references,
            tags=tags,
            timeline=timeline,
            title=title,
        )

        advisory_m_cna.additional_properties = d
        return advisory_m_cna

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
