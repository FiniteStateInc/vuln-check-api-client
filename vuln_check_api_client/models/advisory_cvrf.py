from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvrf_reference import AdvisoryCVRFReference
    from ..models.advisory_document_note import AdvisoryDocumentNote
    from ..models.advisory_document_tracking import AdvisoryDocumentTracking
    from ..models.advisory_product_tree import AdvisoryProductTree
    from ..models.advisory_vulnerability import AdvisoryVulnerability


T = TypeVar("T", bound="AdvisoryCvrf")


@_attrs_define
class AdvisoryCvrf:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        notes (Union[Unset, list['AdvisoryDocumentNote']]):
        product_tree (Union[Unset, AdvisoryProductTree]):
        references (Union[Unset, list['AdvisoryCVRFReference']]):
        title (Union[Unset, str]):
        tracking (Union[Unset, AdvisoryDocumentTracking]):
        vulnerabilities (Union[Unset, list['AdvisoryVulnerability']]):
    """

    cve: Union[Unset, list[str]] = UNSET
    notes: Union[Unset, list["AdvisoryDocumentNote"]] = UNSET
    product_tree: Union[Unset, "AdvisoryProductTree"] = UNSET
    references: Union[Unset, list["AdvisoryCVRFReference"]] = UNSET
    title: Union[Unset, str] = UNSET
    tracking: Union[Unset, "AdvisoryDocumentTracking"] = UNSET
    vulnerabilities: Union[Unset, list["AdvisoryVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        product_tree: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_tree, Unset):
            product_tree = self.product_tree.to_dict()

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

        vulnerabilities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if notes is not UNSET:
            field_dict["notes"] = notes
        if product_tree is not UNSET:
            field_dict["productTree"] = product_tree
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvrf_reference import AdvisoryCVRFReference
        from ..models.advisory_document_note import AdvisoryDocumentNote
        from ..models.advisory_document_tracking import AdvisoryDocumentTracking
        from ..models.advisory_product_tree import AdvisoryProductTree
        from ..models.advisory_vulnerability import AdvisoryVulnerability

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = AdvisoryDocumentNote.from_dict(notes_item_data)

            notes.append(notes_item)

        _product_tree = d.pop("productTree", UNSET)
        product_tree: Union[Unset, AdvisoryProductTree]
        if isinstance(_product_tree, Unset):
            product_tree = UNSET
        else:
            product_tree = AdvisoryProductTree.from_dict(_product_tree)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryCVRFReference.from_dict(references_item_data)

            references.append(references_item)

        title = d.pop("title", UNSET)

        _tracking = d.pop("tracking", UNSET)
        tracking: Union[Unset, AdvisoryDocumentTracking]
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = AdvisoryDocumentTracking.from_dict(_tracking)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = AdvisoryVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        advisory_cvrf = cls(
            cve=cve,
            notes=notes,
            product_tree=product_tree,
            references=references,
            title=title,
            tracking=tracking,
            vulnerabilities=vulnerabilities,
        )

        advisory_cvrf.additional_properties = d
        return advisory_cvrf

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
