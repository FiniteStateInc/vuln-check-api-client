from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mitre_attack_ref import AdvisoryMitreAttackRef
    from ..models.advisory_nist_control import AdvisoryNISTControl


T = TypeVar("T", bound="AdvisoryMitreAttackTechWithRefs")


@_attrs_define
class AdvisoryMitreAttackTechWithRefs:
    """
    Attributes:
        domain (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        nist_controls (Union[Unset, list['AdvisoryNISTControl']]):
        references (Union[Unset, list['AdvisoryMitreAttackRef']]):
        subtechnique (Union[Unset, bool]):
        tactics (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    domain: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nist_controls: Union[Unset, list["AdvisoryNISTControl"]] = UNSET
    references: Union[Unset, list["AdvisoryMitreAttackRef"]] = UNSET
    subtechnique: Union[Unset, bool] = UNSET
    tactics: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        id = self.id

        name = self.name

        nist_controls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nist_controls, Unset):
            nist_controls = []
            for nist_controls_item_data in self.nist_controls:
                nist_controls_item = nist_controls_item_data.to_dict()
                nist_controls.append(nist_controls_item)

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        subtechnique = self.subtechnique

        tactics: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tactics, Unset):
            tactics = self.tactics

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if nist_controls is not UNSET:
            field_dict["nist_controls"] = nist_controls
        if references is not UNSET:
            field_dict["references"] = references
        if subtechnique is not UNSET:
            field_dict["subtechnique"] = subtechnique
        if tactics is not UNSET:
            field_dict["tactics"] = tactics
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mitre_attack_ref import AdvisoryMitreAttackRef
        from ..models.advisory_nist_control import AdvisoryNISTControl

        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        nist_controls = []
        _nist_controls = d.pop("nist_controls", UNSET)
        for nist_controls_item_data in _nist_controls or []:
            nist_controls_item = AdvisoryNISTControl.from_dict(nist_controls_item_data)

            nist_controls.append(nist_controls_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryMitreAttackRef.from_dict(references_item_data)

            references.append(references_item)

        subtechnique = d.pop("subtechnique", UNSET)

        tactics = cast(list[str], d.pop("tactics", UNSET))

        url = d.pop("url", UNSET)

        advisory_mitre_attack_tech_with_refs = cls(
            domain=domain,
            id=id,
            name=name,
            nist_controls=nist_controls,
            references=references,
            subtechnique=subtechnique,
            tactics=tactics,
            url=url,
        )

        advisory_mitre_attack_tech_with_refs.additional_properties = d
        return advisory_mitre_attack_tech_with_refs

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
