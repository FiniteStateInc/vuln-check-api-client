from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_siemens_document import AdvisorySiemensDocument
    from ..models.advisory_siemens_product_tree import AdvisorySiemensProductTree
    from ..models.advisory_siemens_vulnerability import AdvisorySiemensVulnerability


T = TypeVar("T", bound="AdvisorySSASource")


@_attrs_define
class AdvisorySSASource:
    """
    Attributes:
        document (Union[Unset, AdvisorySiemensDocument]):
        product_tree (Union[Unset, AdvisorySiemensProductTree]):
        vulnerabilities (Union[Unset, list['AdvisorySiemensVulnerability']]):
    """

    document: Union[Unset, "AdvisorySiemensDocument"] = UNSET
    product_tree: Union[Unset, "AdvisorySiemensProductTree"] = UNSET
    vulnerabilities: Union[Unset, list["AdvisorySiemensVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

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
        if product_tree is not UNSET:
            field_dict["product_tree"] = product_tree
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_siemens_document import AdvisorySiemensDocument
        from ..models.advisory_siemens_product_tree import AdvisorySiemensProductTree
        from ..models.advisory_siemens_vulnerability import AdvisorySiemensVulnerability

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: Union[Unset, AdvisorySiemensDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = AdvisorySiemensDocument.from_dict(_document)

        _product_tree = d.pop("product_tree", UNSET)
        product_tree: Union[Unset, AdvisorySiemensProductTree]
        if isinstance(_product_tree, Unset):
            product_tree = UNSET
        else:
            product_tree = AdvisorySiemensProductTree.from_dict(_product_tree)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = AdvisorySiemensVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        advisory_ssa_source = cls(
            document=document,
            product_tree=product_tree,
            vulnerabilities=vulnerabilities,
        )

        advisory_ssa_source.additional_properties = d
        return advisory_ssa_source

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
