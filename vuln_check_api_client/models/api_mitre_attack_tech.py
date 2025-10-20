from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_mitre_detection_tech import ApiMitreDetectionTech
    from ..models.api_mitre_mitigation_2d3_fend_mapping import ApiMitreMitigation2D3FendMapping
    from ..models.api_mitre_mitigation_tech import ApiMitreMitigationTech


T = TypeVar("T", bound="ApiMitreAttackTech")


@_attrs_define
class ApiMitreAttackTech:
    """
    Attributes:
        d3fendmapping (Union[Unset, list['ApiMitreMitigation2D3FendMapping']]):
        detections (Union[Unset, list['ApiMitreDetectionTech']]):
        domain (Union[Unset, str]):
        id (Union[Unset, str]):
        mitigations (Union[Unset, list['ApiMitreMitigationTech']]):
        name (Union[Unset, str]):
        subtechnique (Union[Unset, bool]):
        tactics (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    d3fendmapping: Union[Unset, list["ApiMitreMitigation2D3FendMapping"]] = UNSET
    detections: Union[Unset, list["ApiMitreDetectionTech"]] = UNSET
    domain: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mitigations: Union[Unset, list["ApiMitreMitigationTech"]] = UNSET
    name: Union[Unset, str] = UNSET
    subtechnique: Union[Unset, bool] = UNSET
    tactics: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d3fendmapping: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.d3fendmapping, Unset):
            d3fendmapping = []
            for d3fendmapping_item_data in self.d3fendmapping:
                d3fendmapping_item = d3fendmapping_item_data.to_dict()
                d3fendmapping.append(d3fendmapping_item)

        detections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.detections, Unset):
            detections = []
            for detections_item_data in self.detections:
                detections_item = detections_item_data.to_dict()
                detections.append(detections_item)

        domain = self.domain

        id = self.id

        mitigations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mitigations, Unset):
            mitigations = []
            for mitigations_item_data in self.mitigations:
                mitigations_item = mitigations_item_data.to_dict()
                mitigations.append(mitigations_item)

        name = self.name

        subtechnique = self.subtechnique

        tactics: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tactics, Unset):
            tactics = self.tactics

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if d3fendmapping is not UNSET:
            field_dict["d3fendmapping"] = d3fendmapping
        if detections is not UNSET:
            field_dict["detections"] = detections
        if domain is not UNSET:
            field_dict["domain"] = domain
        if id is not UNSET:
            field_dict["id"] = id
        if mitigations is not UNSET:
            field_dict["mitigations"] = mitigations
        if name is not UNSET:
            field_dict["name"] = name
        if subtechnique is not UNSET:
            field_dict["subtechnique"] = subtechnique
        if tactics is not UNSET:
            field_dict["tactics"] = tactics
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_mitre_detection_tech import ApiMitreDetectionTech
        from ..models.api_mitre_mitigation_2d3_fend_mapping import ApiMitreMitigation2D3FendMapping
        from ..models.api_mitre_mitigation_tech import ApiMitreMitigationTech

        d = dict(src_dict)
        d3fendmapping = []
        _d3fendmapping = d.pop("d3fendmapping", UNSET)
        for d3fendmapping_item_data in _d3fendmapping or []:
            d3fendmapping_item = ApiMitreMitigation2D3FendMapping.from_dict(d3fendmapping_item_data)

            d3fendmapping.append(d3fendmapping_item)

        detections = []
        _detections = d.pop("detections", UNSET)
        for detections_item_data in _detections or []:
            detections_item = ApiMitreDetectionTech.from_dict(detections_item_data)

            detections.append(detections_item)

        domain = d.pop("domain", UNSET)

        id = d.pop("id", UNSET)

        mitigations = []
        _mitigations = d.pop("mitigations", UNSET)
        for mitigations_item_data in _mitigations or []:
            mitigations_item = ApiMitreMitigationTech.from_dict(mitigations_item_data)

            mitigations.append(mitigations_item)

        name = d.pop("name", UNSET)

        subtechnique = d.pop("subtechnique", UNSET)

        tactics = cast(list[str], d.pop("tactics", UNSET))

        url = d.pop("url", UNSET)

        api_mitre_attack_tech = cls(
            d3fendmapping=d3fendmapping,
            detections=detections,
            domain=domain,
            id=id,
            mitigations=mitigations,
            name=name,
            subtechnique=subtechnique,
            tactics=tactics,
            url=url,
        )

        api_mitre_attack_tech.additional_properties = d
        return api_mitre_attack_tech

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
