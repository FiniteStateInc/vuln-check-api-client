from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_csaf_note import AdvisoryCSAFNote
    from ..models.advisory_csaf_vulnerability import AdvisoryCSAFVulnerability
    from ..models.advisory_document_metadata import AdvisoryDocumentMetadata
    from ..models.advisory_product_branch import AdvisoryProductBranch


T = TypeVar("T", bound="AdvisoryCSAF")


@_attrs_define
class AdvisoryCSAF:
    """
    Attributes:
        document (Union[Unset, AdvisoryDocumentMetadata]):
        notes (Union[Unset, list['AdvisoryCSAFNote']]): Notes holds notes associated with the whole document.
            https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#3217-document-property---notes
        product_tree (Union[Unset, AdvisoryProductBranch]):
        vulnerabilities (Union[Unset, list['AdvisoryCSAFVulnerability']]): Vulnerabilities contains information about
            the vulnerabilities,
            (i.e. CVEs), associated threats, and product status.

            https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#323-vulnerabilities-property
    """

    document: Union[Unset, "AdvisoryDocumentMetadata"] = UNSET
    notes: Union[Unset, list["AdvisoryCSAFNote"]] = UNSET
    product_tree: Union[Unset, "AdvisoryProductBranch"] = UNSET
    vulnerabilities: Union[Unset, list["AdvisoryCSAFVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        product_tree: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_tree, Unset):
            product_tree = self.product_tree.to_dict()

        vulnerabilities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if notes is not UNSET:
            field_dict["notes"] = notes
        if product_tree is not UNSET:
            field_dict["product_tree"] = product_tree
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_csaf_note import AdvisoryCSAFNote
        from ..models.advisory_csaf_vulnerability import AdvisoryCSAFVulnerability
        from ..models.advisory_document_metadata import AdvisoryDocumentMetadata
        from ..models.advisory_product_branch import AdvisoryProductBranch

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: Union[Unset, AdvisoryDocumentMetadata]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = AdvisoryDocumentMetadata.from_dict(_document)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = AdvisoryCSAFNote.from_dict(notes_item_data)

            notes.append(notes_item)

        _product_tree = d.pop("product_tree", UNSET)
        product_tree: Union[Unset, AdvisoryProductBranch]
        if isinstance(_product_tree, Unset):
            product_tree = UNSET
        else:
            product_tree = AdvisoryProductBranch.from_dict(_product_tree)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = AdvisoryCSAFVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        advisory_csaf = cls(
            document=document,
            notes=notes,
            product_tree=product_tree,
            vulnerabilities=vulnerabilities,
        )

        advisory_csaf.additional_properties = d
        return advisory_csaf

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
