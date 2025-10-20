from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_csaf_distribution import AdvisoryCSAFDistribution
    from ..models.advisory_csaf_note import AdvisoryCSAFNote
    from ..models.advisory_csaf_reference import AdvisoryCSAFReference
    from ..models.advisory_publisher import AdvisoryPublisher
    from ..models.advisory_tracking import AdvisoryTracking


T = TypeVar("T", bound="AdvisoryDocumentMetadata")


@_attrs_define
class AdvisoryDocumentMetadata:
    """
    Attributes:
        category (Union[Unset, str]):
        csaf_version (Union[Unset, str]):
        distribution (Union[Unset, AdvisoryCSAFDistribution]):
        lang (Union[Unset, str]):
        notes (Union[Unset, list['AdvisoryCSAFNote']]): used by ncsc
        publisher (Union[Unset, AdvisoryPublisher]):
        references (Union[Unset, list['AdvisoryCSAFReference']]):
        title (Union[Unset, str]): Aggregate severity is a vehicle that is provided by the document producer to convey
            the urgency and
            criticality with which the one or more vulnerabilities reported should be addressed.
        tracking (Union[Unset, AdvisoryTracking]):
    """

    category: Union[Unset, str] = UNSET
    csaf_version: Union[Unset, str] = UNSET
    distribution: Union[Unset, "AdvisoryCSAFDistribution"] = UNSET
    lang: Union[Unset, str] = UNSET
    notes: Union[Unset, list["AdvisoryCSAFNote"]] = UNSET
    publisher: Union[Unset, "AdvisoryPublisher"] = UNSET
    references: Union[Unset, list["AdvisoryCSAFReference"]] = UNSET
    title: Union[Unset, str] = UNSET
    tracking: Union[Unset, "AdvisoryTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        csaf_version = self.csaf_version

        distribution: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        lang = self.lang

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        publisher: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        title = self.title

        tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if csaf_version is not UNSET:
            field_dict["csaf_version"] = csaf_version
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if lang is not UNSET:
            field_dict["lang"] = lang
        if notes is not UNSET:
            field_dict["notes"] = notes
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_csaf_distribution import AdvisoryCSAFDistribution
        from ..models.advisory_csaf_note import AdvisoryCSAFNote
        from ..models.advisory_csaf_reference import AdvisoryCSAFReference
        from ..models.advisory_publisher import AdvisoryPublisher
        from ..models.advisory_tracking import AdvisoryTracking

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        csaf_version = d.pop("csaf_version", UNSET)

        _distribution = d.pop("distribution", UNSET)
        distribution: Union[Unset, AdvisoryCSAFDistribution]
        if isinstance(_distribution, Unset):
            distribution = UNSET
        else:
            distribution = AdvisoryCSAFDistribution.from_dict(_distribution)

        lang = d.pop("lang", UNSET)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = AdvisoryCSAFNote.from_dict(notes_item_data)

            notes.append(notes_item)

        _publisher = d.pop("publisher", UNSET)
        publisher: Union[Unset, AdvisoryPublisher]
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = AdvisoryPublisher.from_dict(_publisher)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryCSAFReference.from_dict(references_item_data)

            references.append(references_item)

        title = d.pop("title", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, AdvisoryTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = AdvisoryTracking.from_dict(_tracking)

        advisory_document_metadata = cls(
            category=category,
            csaf_version=csaf_version,
            distribution=distribution,
            lang=lang,
            notes=notes,
            publisher=publisher,
            references=references,
            title=title,
            tracking=tracking,
        )

        advisory_document_metadata.additional_properties = d
        return advisory_document_metadata

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
