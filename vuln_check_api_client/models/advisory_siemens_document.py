from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_siemens_acknowledgments import AdvisorySiemensAcknowledgments
    from ..models.advisory_siemens_distribution import AdvisorySiemensDistribution
    from ..models.advisory_siemens_notes import AdvisorySiemensNotes
    from ..models.advisory_siemens_publisher import AdvisorySiemensPublisher
    from ..models.advisory_siemens_references import AdvisorySiemensReferences
    from ..models.advisory_siemens_tracking import AdvisorySiemensTracking


T = TypeVar("T", bound="AdvisorySiemensDocument")


@_attrs_define
class AdvisorySiemensDocument:
    """
    Attributes:
        acknowledgments (Union[Unset, list['AdvisorySiemensAcknowledgments']]):
        category (Union[Unset, str]):
        csaf_version (Union[Unset, str]):
        distribution (Union[Unset, AdvisorySiemensDistribution]):
        notes (Union[Unset, list['AdvisorySiemensNotes']]):
        publisher (Union[Unset, AdvisorySiemensPublisher]):
        references (Union[Unset, list['AdvisorySiemensReferences']]):
        title (Union[Unset, str]):
        tracking (Union[Unset, AdvisorySiemensTracking]):
    """

    acknowledgments: Union[Unset, list["AdvisorySiemensAcknowledgments"]] = UNSET
    category: Union[Unset, str] = UNSET
    csaf_version: Union[Unset, str] = UNSET
    distribution: Union[Unset, "AdvisorySiemensDistribution"] = UNSET
    notes: Union[Unset, list["AdvisorySiemensNotes"]] = UNSET
    publisher: Union[Unset, "AdvisorySiemensPublisher"] = UNSET
    references: Union[Unset, list["AdvisorySiemensReferences"]] = UNSET
    title: Union[Unset, str] = UNSET
    tracking: Union[Unset, "AdvisorySiemensTracking"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledgments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.acknowledgments, Unset):
            acknowledgments = []
            for acknowledgments_item_data in self.acknowledgments:
                acknowledgments_item = acknowledgments_item_data.to_dict()
                acknowledgments.append(acknowledgments_item)

        category = self.category

        csaf_version = self.csaf_version

        distribution: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

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
        if acknowledgments is not UNSET:
            field_dict["acknowledgments"] = acknowledgments
        if category is not UNSET:
            field_dict["category"] = category
        if csaf_version is not UNSET:
            field_dict["csaf_version"] = csaf_version
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
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
        from ..models.advisory_siemens_acknowledgments import AdvisorySiemensAcknowledgments
        from ..models.advisory_siemens_distribution import AdvisorySiemensDistribution
        from ..models.advisory_siemens_notes import AdvisorySiemensNotes
        from ..models.advisory_siemens_publisher import AdvisorySiemensPublisher
        from ..models.advisory_siemens_references import AdvisorySiemensReferences
        from ..models.advisory_siemens_tracking import AdvisorySiemensTracking

        d = dict(src_dict)
        acknowledgments = []
        _acknowledgments = d.pop("acknowledgments", UNSET)
        for acknowledgments_item_data in _acknowledgments or []:
            acknowledgments_item = AdvisorySiemensAcknowledgments.from_dict(acknowledgments_item_data)

            acknowledgments.append(acknowledgments_item)

        category = d.pop("category", UNSET)

        csaf_version = d.pop("csaf_version", UNSET)

        _distribution = d.pop("distribution", UNSET)
        distribution: Union[Unset, AdvisorySiemensDistribution]
        if isinstance(_distribution, Unset):
            distribution = UNSET
        else:
            distribution = AdvisorySiemensDistribution.from_dict(_distribution)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = AdvisorySiemensNotes.from_dict(notes_item_data)

            notes.append(notes_item)

        _publisher = d.pop("publisher", UNSET)
        publisher: Union[Unset, AdvisorySiemensPublisher]
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = AdvisorySiemensPublisher.from_dict(_publisher)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisorySiemensReferences.from_dict(references_item_data)

            references.append(references_item)

        title = d.pop("title", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, AdvisorySiemensTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = AdvisorySiemensTracking.from_dict(_tracking)

        advisory_siemens_document = cls(
            acknowledgments=acknowledgments,
            category=category,
            csaf_version=csaf_version,
            distribution=distribution,
            notes=notes,
            publisher=publisher,
            references=references,
            title=title,
            tracking=tracking,
        )

        advisory_siemens_document.additional_properties = d
        return advisory_siemens_document

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
