from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_capec import AdvisoryCapec
    from ..models.advisory_cve_reference import AdvisoryCVEReference
    from ..models.advisory_cwe_data import AdvisoryCweData
    from ..models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs
    from ..models.advisory_tool import AdvisoryTool


T = TypeVar("T", bound="AdvisoryBotnet")


@_attrs_define
class AdvisoryBotnet:
    """
    Attributes:
        associated_capecs (Union[Unset, list['AdvisoryCapec']]):
        associated_cwes (Union[Unset, list['AdvisoryCweData']]):
        associated_mitre_attack_techniques (Union[Unset, list['AdvisoryMitreAttackTechWithRefs']]):
        botnet_name (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cve_references (Union[Unset, list['AdvisoryCVEReference']]):
        date_added (Union[Unset, str]):
        malpedia_url (Union[Unset, str]):
        tools (Union[Unset, list['AdvisoryTool']]):
    """

    associated_capecs: Union[Unset, list["AdvisoryCapec"]] = UNSET
    associated_cwes: Union[Unset, list["AdvisoryCweData"]] = UNSET
    associated_mitre_attack_techniques: Union[Unset, list["AdvisoryMitreAttackTechWithRefs"]] = UNSET
    botnet_name: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cve_references: Union[Unset, list["AdvisoryCVEReference"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    malpedia_url: Union[Unset, str] = UNSET
    tools: Union[Unset, list["AdvisoryTool"]] = UNSET
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

        botnet_name = self.botnet_name

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cve_references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cve_references, Unset):
            cve_references = []
            for cve_references_item_data in self.cve_references:
                cve_references_item = cve_references_item_data.to_dict()
                cve_references.append(cve_references_item)

        date_added = self.date_added

        malpedia_url = self.malpedia_url

        tools: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_capecs is not UNSET:
            field_dict["associated_capecs"] = associated_capecs
        if associated_cwes is not UNSET:
            field_dict["associated_cwes"] = associated_cwes
        if associated_mitre_attack_techniques is not UNSET:
            field_dict["associated_mitre_attack_techniques"] = associated_mitre_attack_techniques
        if botnet_name is not UNSET:
            field_dict["botnet_name"] = botnet_name
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cve_references is not UNSET:
            field_dict["cve_references"] = cve_references
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if malpedia_url is not UNSET:
            field_dict["malpedia_url"] = malpedia_url
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_capec import AdvisoryCapec
        from ..models.advisory_cve_reference import AdvisoryCVEReference
        from ..models.advisory_cwe_data import AdvisoryCweData
        from ..models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs
        from ..models.advisory_tool import AdvisoryTool

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

        botnet_name = d.pop("botnet_name", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cve_references = []
        _cve_references = d.pop("cve_references", UNSET)
        for cve_references_item_data in _cve_references or []:
            cve_references_item = AdvisoryCVEReference.from_dict(cve_references_item_data)

            cve_references.append(cve_references_item)

        date_added = d.pop("date_added", UNSET)

        malpedia_url = d.pop("malpedia_url", UNSET)

        tools = []
        _tools = d.pop("tools", UNSET)
        for tools_item_data in _tools or []:
            tools_item = AdvisoryTool.from_dict(tools_item_data)

            tools.append(tools_item)

        advisory_botnet = cls(
            associated_capecs=associated_capecs,
            associated_cwes=associated_cwes,
            associated_mitre_attack_techniques=associated_mitre_attack_techniques,
            botnet_name=botnet_name,
            cve=cve,
            cve_references=cve_references,
            date_added=date_added,
            malpedia_url=malpedia_url,
            tools=tools,
        )

        advisory_botnet.additional_properties = d
        return advisory_botnet

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
