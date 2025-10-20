from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_document_publisher import AdvisoryDocumentPublisher
    from ..models.advisory_m_document_tracking import AdvisoryMDocumentTracking
    from ..models.advisory_m_product_tree import AdvisoryMProductTree
    from ..models.advisory_m_vulnerability import AdvisoryMVulnerability
    from ..models.advisory_ms_document_title import AdvisoryMSDocumentTitle
    from ..models.advisory_r_note import AdvisoryRNote


T = TypeVar("T", bound="AdvisoryMSCVRF")


@_attrs_define
class AdvisoryMSCVRF:
    """
    Attributes:
        document_title (Union[Unset, AdvisoryMSDocumentTitle]):
        document_tracking (Union[Unset, AdvisoryMDocumentTracking]):
        product_tree (Union[Unset, AdvisoryMProductTree]):
        document_type (Union[Unset, str]):
        documentnotes (Union[Unset, list['AdvisoryRNote']]): diff
        documentpublisher (Union[Unset, AdvisoryDocumentPublisher]):
        vulnerability (Union[Unset, list['AdvisoryMVulnerability']]):
    """

    document_title: Union[Unset, "AdvisoryMSDocumentTitle"] = UNSET
    document_tracking: Union[Unset, "AdvisoryMDocumentTracking"] = UNSET
    product_tree: Union[Unset, "AdvisoryMProductTree"] = UNSET
    document_type: Union[Unset, str] = UNSET
    documentnotes: Union[Unset, list["AdvisoryRNote"]] = UNSET
    documentpublisher: Union[Unset, "AdvisoryDocumentPublisher"] = UNSET
    vulnerability: Union[Unset, list["AdvisoryMVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_title, Unset):
            document_title = self.document_title.to_dict()

        document_tracking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_tracking, Unset):
            document_tracking = self.document_tracking.to_dict()

        product_tree: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_tree, Unset):
            product_tree = self.product_tree.to_dict()

        document_type = self.document_type

        documentnotes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documentnotes, Unset):
            documentnotes = []
            for documentnotes_item_data in self.documentnotes:
                documentnotes_item = documentnotes_item_data.to_dict()
                documentnotes.append(documentnotes_item)

        documentpublisher: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.documentpublisher, Unset):
            documentpublisher = self.documentpublisher.to_dict()

        vulnerability: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerability, Unset):
            vulnerability = []
            for vulnerability_item_data in self.vulnerability:
                vulnerability_item = vulnerability_item_data.to_dict()
                vulnerability.append(vulnerability_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_title is not UNSET:
            field_dict["DocumentTitle"] = document_title
        if document_tracking is not UNSET:
            field_dict["DocumentTracking"] = document_tracking
        if product_tree is not UNSET:
            field_dict["ProductTree"] = product_tree
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if documentnotes is not UNSET:
            field_dict["documentnotes"] = documentnotes
        if documentpublisher is not UNSET:
            field_dict["documentpublisher"] = documentpublisher
        if vulnerability is not UNSET:
            field_dict["vulnerability"] = vulnerability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_document_publisher import AdvisoryDocumentPublisher
        from ..models.advisory_m_document_tracking import AdvisoryMDocumentTracking
        from ..models.advisory_m_product_tree import AdvisoryMProductTree
        from ..models.advisory_m_vulnerability import AdvisoryMVulnerability
        from ..models.advisory_ms_document_title import AdvisoryMSDocumentTitle
        from ..models.advisory_r_note import AdvisoryRNote

        d = dict(src_dict)
        _document_title = d.pop("DocumentTitle", UNSET)
        document_title: Union[Unset, AdvisoryMSDocumentTitle]
        if isinstance(_document_title, Unset):
            document_title = UNSET
        else:
            document_title = AdvisoryMSDocumentTitle.from_dict(_document_title)

        _document_tracking = d.pop("DocumentTracking", UNSET)
        document_tracking: Union[Unset, AdvisoryMDocumentTracking]
        if isinstance(_document_tracking, Unset):
            document_tracking = UNSET
        else:
            document_tracking = AdvisoryMDocumentTracking.from_dict(_document_tracking)

        _product_tree = d.pop("ProductTree", UNSET)
        product_tree: Union[Unset, AdvisoryMProductTree]
        if isinstance(_product_tree, Unset):
            product_tree = UNSET
        else:
            product_tree = AdvisoryMProductTree.from_dict(_product_tree)

        document_type = d.pop("document_type", UNSET)

        documentnotes = []
        _documentnotes = d.pop("documentnotes", UNSET)
        for documentnotes_item_data in _documentnotes or []:
            documentnotes_item = AdvisoryRNote.from_dict(documentnotes_item_data)

            documentnotes.append(documentnotes_item)

        _documentpublisher = d.pop("documentpublisher", UNSET)
        documentpublisher: Union[Unset, AdvisoryDocumentPublisher]
        if isinstance(_documentpublisher, Unset):
            documentpublisher = UNSET
        else:
            documentpublisher = AdvisoryDocumentPublisher.from_dict(_documentpublisher)

        vulnerability = []
        _vulnerability = d.pop("vulnerability", UNSET)
        for vulnerability_item_data in _vulnerability or []:
            vulnerability_item = AdvisoryMVulnerability.from_dict(vulnerability_item_data)

            vulnerability.append(vulnerability_item)

        advisory_mscvrf = cls(
            document_title=document_title,
            document_tracking=document_tracking,
            product_tree=product_tree,
            document_type=document_type,
            documentnotes=documentnotes,
            documentpublisher=documentpublisher,
            vulnerability=vulnerability,
        )

        advisory_mscvrf.additional_properties = d
        return advisory_mscvrf

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
