from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_capec import AdvisoryCapec
    from ..models.advisory_cve_reference import AdvisoryCVEReference
    from ..models.advisory_cwe_data import AdvisoryCweData
    from ..models.advisory_misp_value_no_id import AdvisoryMISPValueNoID
    from ..models.advisory_mitre_attack_group_no_id import AdvisoryMITREAttackGroupNoID
    from ..models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs
    from ..models.advisory_mitre_group_cti import AdvisoryMitreGroupCTI
    from ..models.advisory_tool import AdvisoryTool
    from ..models.advisory_vendor_name_for_threat_actor import AdvisoryVendorNameForThreatActor
    from ..models.advisory_vendor_product import AdvisoryVendorProduct


T = TypeVar("T", bound="AdvisoryThreatActorWithExternalObjects")


@_attrs_define
class AdvisoryThreatActorWithExternalObjects:
    """
    Attributes:
        associated_capecs (Union[Unset, list['AdvisoryCapec']]):
        associated_cwes (Union[Unset, list['AdvisoryCweData']]):
        associated_mitre_attack_techniques (Union[Unset, list['AdvisoryMitreAttackTechWithRefs']]):
        country (Union[Unset, str]):
        cve_references (Union[Unset, list['AdvisoryCVEReference']]):
        date_added (Union[Unset, str]):
        malpedia_url (Union[Unset, str]):
        misp_id (Union[Unset, str]):
        misp_threat_actor (Union[Unset, AdvisoryMISPValueNoID]):
        mitre_attack_group (Union[Unset, AdvisoryMITREAttackGroupNoID]):
        mitre_group_cti (Union[Unset, AdvisoryMitreGroupCTI]):
        mitre_id (Union[Unset, str]):
        threat_actor_name (Union[Unset, str]):
        tools (Union[Unset, list['AdvisoryTool']]):
        vendor_names_for_threat_actors (Union[Unset, list['AdvisoryVendorNameForThreatActor']]):
        vendors_and_products_targeted (Union[Unset, list['AdvisoryVendorProduct']]):
    """

    associated_capecs: Union[Unset, list["AdvisoryCapec"]] = UNSET
    associated_cwes: Union[Unset, list["AdvisoryCweData"]] = UNSET
    associated_mitre_attack_techniques: Union[Unset, list["AdvisoryMitreAttackTechWithRefs"]] = UNSET
    country: Union[Unset, str] = UNSET
    cve_references: Union[Unset, list["AdvisoryCVEReference"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    malpedia_url: Union[Unset, str] = UNSET
    misp_id: Union[Unset, str] = UNSET
    misp_threat_actor: Union[Unset, "AdvisoryMISPValueNoID"] = UNSET
    mitre_attack_group: Union[Unset, "AdvisoryMITREAttackGroupNoID"] = UNSET
    mitre_group_cti: Union[Unset, "AdvisoryMitreGroupCTI"] = UNSET
    mitre_id: Union[Unset, str] = UNSET
    threat_actor_name: Union[Unset, str] = UNSET
    tools: Union[Unset, list["AdvisoryTool"]] = UNSET
    vendor_names_for_threat_actors: Union[Unset, list["AdvisoryVendorNameForThreatActor"]] = UNSET
    vendors_and_products_targeted: Union[Unset, list["AdvisoryVendorProduct"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_capecs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.associated_capecs, Unset):
            associated_capecs = []
            for associated_capecs_item_data in self.associated_capecs:
                associated_capecs_item = associated_capecs_item_data.to_dict()
                associated_capecs.append(associated_capecs_item)

        associated_cwes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.associated_cwes, Unset):
            associated_cwes = []
            for associated_cwes_item_data in self.associated_cwes:
                associated_cwes_item = associated_cwes_item_data.to_dict()
                associated_cwes.append(associated_cwes_item)

        associated_mitre_attack_techniques: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.associated_mitre_attack_techniques, Unset):
            associated_mitre_attack_techniques = []
            for associated_mitre_attack_techniques_item_data in self.associated_mitre_attack_techniques:
                associated_mitre_attack_techniques_item = associated_mitre_attack_techniques_item_data.to_dict()
                associated_mitre_attack_techniques.append(associated_mitre_attack_techniques_item)

        country = self.country

        cve_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cve_references, Unset):
            cve_references = []
            for cve_references_item_data in self.cve_references:
                cve_references_item = cve_references_item_data.to_dict()
                cve_references.append(cve_references_item)

        date_added = self.date_added

        malpedia_url = self.malpedia_url

        misp_id = self.misp_id

        misp_threat_actor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.misp_threat_actor, Unset):
            misp_threat_actor = self.misp_threat_actor.to_dict()

        mitre_attack_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mitre_attack_group, Unset):
            mitre_attack_group = self.mitre_attack_group.to_dict()

        mitre_group_cti: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mitre_group_cti, Unset):
            mitre_group_cti = self.mitre_group_cti.to_dict()

        mitre_id = self.mitre_id

        threat_actor_name = self.threat_actor_name

        tools: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        vendor_names_for_threat_actors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vendor_names_for_threat_actors, Unset):
            vendor_names_for_threat_actors = []
            for vendor_names_for_threat_actors_item_data in self.vendor_names_for_threat_actors:
                vendor_names_for_threat_actors_item = vendor_names_for_threat_actors_item_data.to_dict()
                vendor_names_for_threat_actors.append(vendor_names_for_threat_actors_item)

        vendors_and_products_targeted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vendors_and_products_targeted, Unset):
            vendors_and_products_targeted = []
            for vendors_and_products_targeted_item_data in self.vendors_and_products_targeted:
                vendors_and_products_targeted_item = vendors_and_products_targeted_item_data.to_dict()
                vendors_and_products_targeted.append(vendors_and_products_targeted_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_capecs is not UNSET:
            field_dict["associated_capecs"] = associated_capecs
        if associated_cwes is not UNSET:
            field_dict["associated_cwes"] = associated_cwes
        if associated_mitre_attack_techniques is not UNSET:
            field_dict["associated_mitre_attack_techniques"] = associated_mitre_attack_techniques
        if country is not UNSET:
            field_dict["country"] = country
        if cve_references is not UNSET:
            field_dict["cve_references"] = cve_references
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if malpedia_url is not UNSET:
            field_dict["malpedia_url"] = malpedia_url
        if misp_id is not UNSET:
            field_dict["misp_id"] = misp_id
        if misp_threat_actor is not UNSET:
            field_dict["misp_threat_actor"] = misp_threat_actor
        if mitre_attack_group is not UNSET:
            field_dict["mitre_attack_group"] = mitre_attack_group
        if mitre_group_cti is not UNSET:
            field_dict["mitre_group_cti"] = mitre_group_cti
        if mitre_id is not UNSET:
            field_dict["mitre_id"] = mitre_id
        if threat_actor_name is not UNSET:
            field_dict["threat_actor_name"] = threat_actor_name
        if tools is not UNSET:
            field_dict["tools"] = tools
        if vendor_names_for_threat_actors is not UNSET:
            field_dict["vendor_names_for_threat_actors"] = vendor_names_for_threat_actors
        if vendors_and_products_targeted is not UNSET:
            field_dict["vendors_and_products_targeted"] = vendors_and_products_targeted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_capec import AdvisoryCapec
        from ..models.advisory_cve_reference import AdvisoryCVEReference
        from ..models.advisory_cwe_data import AdvisoryCweData
        from ..models.advisory_misp_value_no_id import AdvisoryMISPValueNoID
        from ..models.advisory_mitre_attack_group_no_id import AdvisoryMITREAttackGroupNoID
        from ..models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs
        from ..models.advisory_mitre_group_cti import AdvisoryMitreGroupCTI
        from ..models.advisory_tool import AdvisoryTool
        from ..models.advisory_vendor_name_for_threat_actor import AdvisoryVendorNameForThreatActor
        from ..models.advisory_vendor_product import AdvisoryVendorProduct

        d = dict(src_dict)
        associated_capecs = []
        _associated_capecs = d.pop("associated_capecs", UNSET)
        for associated_capecs_item_data in _associated_capecs or []:
            associated_capecs_item = AdvisoryCapec.from_dict(associated_capecs_item_data)

            associated_capecs.append(associated_capecs_item)

        associated_cwes = []
        _associated_cwes = d.pop("associated_cwes", UNSET)
        for associated_cwes_item_data in _associated_cwes or []:
            associated_cwes_item = AdvisoryCweData.from_dict(associated_cwes_item_data)

            associated_cwes.append(associated_cwes_item)

        associated_mitre_attack_techniques = []
        _associated_mitre_attack_techniques = d.pop("associated_mitre_attack_techniques", UNSET)
        for associated_mitre_attack_techniques_item_data in _associated_mitre_attack_techniques or []:
            associated_mitre_attack_techniques_item = AdvisoryMitreAttackTechWithRefs.from_dict(
                associated_mitre_attack_techniques_item_data
            )

            associated_mitre_attack_techniques.append(associated_mitre_attack_techniques_item)

        country = d.pop("country", UNSET)

        cve_references = []
        _cve_references = d.pop("cve_references", UNSET)
        for cve_references_item_data in _cve_references or []:
            cve_references_item = AdvisoryCVEReference.from_dict(cve_references_item_data)

            cve_references.append(cve_references_item)

        date_added = d.pop("date_added", UNSET)

        malpedia_url = d.pop("malpedia_url", UNSET)

        misp_id = d.pop("misp_id", UNSET)

        _misp_threat_actor = d.pop("misp_threat_actor", UNSET)
        misp_threat_actor: Union[Unset, AdvisoryMISPValueNoID]
        if isinstance(_misp_threat_actor, Unset):
            misp_threat_actor = UNSET
        else:
            misp_threat_actor = AdvisoryMISPValueNoID.from_dict(_misp_threat_actor)

        _mitre_attack_group = d.pop("mitre_attack_group", UNSET)
        mitre_attack_group: Union[Unset, AdvisoryMITREAttackGroupNoID]
        if isinstance(_mitre_attack_group, Unset):
            mitre_attack_group = UNSET
        else:
            mitre_attack_group = AdvisoryMITREAttackGroupNoID.from_dict(_mitre_attack_group)

        _mitre_group_cti = d.pop("mitre_group_cti", UNSET)
        mitre_group_cti: Union[Unset, AdvisoryMitreGroupCTI]
        if isinstance(_mitre_group_cti, Unset):
            mitre_group_cti = UNSET
        else:
            mitre_group_cti = AdvisoryMitreGroupCTI.from_dict(_mitre_group_cti)

        mitre_id = d.pop("mitre_id", UNSET)

        threat_actor_name = d.pop("threat_actor_name", UNSET)

        tools = []
        _tools = d.pop("tools", UNSET)
        for tools_item_data in _tools or []:
            tools_item = AdvisoryTool.from_dict(tools_item_data)

            tools.append(tools_item)

        vendor_names_for_threat_actors = []
        _vendor_names_for_threat_actors = d.pop("vendor_names_for_threat_actors", UNSET)
        for vendor_names_for_threat_actors_item_data in _vendor_names_for_threat_actors or []:
            vendor_names_for_threat_actors_item = AdvisoryVendorNameForThreatActor.from_dict(
                vendor_names_for_threat_actors_item_data
            )

            vendor_names_for_threat_actors.append(vendor_names_for_threat_actors_item)

        vendors_and_products_targeted = []
        _vendors_and_products_targeted = d.pop("vendors_and_products_targeted", UNSET)
        for vendors_and_products_targeted_item_data in _vendors_and_products_targeted or []:
            vendors_and_products_targeted_item = AdvisoryVendorProduct.from_dict(
                vendors_and_products_targeted_item_data
            )

            vendors_and_products_targeted.append(vendors_and_products_targeted_item)

        advisory_threat_actor_with_external_objects = cls(
            associated_capecs=associated_capecs,
            associated_cwes=associated_cwes,
            associated_mitre_attack_techniques=associated_mitre_attack_techniques,
            country=country,
            cve_references=cve_references,
            date_added=date_added,
            malpedia_url=malpedia_url,
            misp_id=misp_id,
            misp_threat_actor=misp_threat_actor,
            mitre_attack_group=mitre_attack_group,
            mitre_group_cti=mitre_group_cti,
            mitre_id=mitre_id,
            threat_actor_name=threat_actor_name,
            tools=tools,
            vendor_names_for_threat_actors=vendor_names_for_threat_actors,
            vendors_and_products_targeted=vendors_and_products_targeted,
        )

        advisory_threat_actor_with_external_objects.additional_properties = d
        return advisory_threat_actor_with_external_objects

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
