from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_configurations import ApiConfigurations
    from ..models.api_cve_extended import ApiCVEExtended
    from ..models.api_impact_extended import ApiImpactExtended
    from ..models.api_mitre_attack_tech import ApiMitreAttackTech
    from ..models.api_related_attack_pattern import ApiRelatedAttackPattern


T = TypeVar("T", bound="ApiCveItemsExtended")


@_attrs_define
class ApiCveItemsExtended:
    """
    Attributes:
        field_timestamp (Union[Unset, str]):
        configurations (Union[Unset, ApiConfigurations]):
        cve (Union[Unset, ApiCVEExtended]):
        date_added (Union[Unset, str]):
        document_generation_date (Union[Unset, str]): the deep tag instructs deep.Equal to ignore this field (used
            during OpenSearch loading)
        impact (Union[Unset, ApiImpactExtended]):
        last_modified_date (Union[Unset, str]):
        mitre_attack_techniques (Union[Unset, list['ApiMitreAttackTech']]):
        published_date (Union[Unset, str]):
        related_attack_patterns (Union[Unset, list['ApiRelatedAttackPattern']]):
        vc_configurations (Union[Unset, ApiConfigurations]):
        vc_vulnerable_cp_es (Union[Unset, list[str]]):
        vulnerable_cpes (Union[Unset, list[str]]):
    """

    field_timestamp: Union[Unset, str] = UNSET
    configurations: Union[Unset, "ApiConfigurations"] = UNSET
    cve: Union[Unset, "ApiCVEExtended"] = UNSET
    date_added: Union[Unset, str] = UNSET
    document_generation_date: Union[Unset, str] = UNSET
    impact: Union[Unset, "ApiImpactExtended"] = UNSET
    last_modified_date: Union[Unset, str] = UNSET
    mitre_attack_techniques: Union[Unset, list["ApiMitreAttackTech"]] = UNSET
    published_date: Union[Unset, str] = UNSET
    related_attack_patterns: Union[Unset, list["ApiRelatedAttackPattern"]] = UNSET
    vc_configurations: Union[Unset, "ApiConfigurations"] = UNSET
    vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
    vulnerable_cpes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_timestamp = self.field_timestamp

        configurations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = self.configurations.to_dict()

        cve: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve.to_dict()

        date_added = self.date_added

        document_generation_date = self.document_generation_date

        impact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact.to_dict()

        last_modified_date = self.last_modified_date

        mitre_attack_techniques: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mitre_attack_techniques, Unset):
            mitre_attack_techniques = []
            for mitre_attack_techniques_item_data in self.mitre_attack_techniques:
                mitre_attack_techniques_item = mitre_attack_techniques_item_data.to_dict()
                mitre_attack_techniques.append(mitre_attack_techniques_item)

        published_date = self.published_date

        related_attack_patterns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related_attack_patterns, Unset):
            related_attack_patterns = []
            for related_attack_patterns_item_data in self.related_attack_patterns:
                related_attack_patterns_item = related_attack_patterns_item_data.to_dict()
                related_attack_patterns.append(related_attack_patterns_item)

        vc_configurations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vc_configurations, Unset):
            vc_configurations = self.vc_configurations.to_dict()

        vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vc_vulnerable_cp_es, Unset):
            vc_vulnerable_cp_es = self.vc_vulnerable_cp_es

        vulnerable_cpes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerable_cpes, Unset):
            vulnerable_cpes = self.vulnerable_cpes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_timestamp is not UNSET:
            field_dict["_timestamp"] = field_timestamp
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if document_generation_date is not UNSET:
            field_dict["documentGenerationDate"] = document_generation_date
        if impact is not UNSET:
            field_dict["impact"] = impact
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if mitre_attack_techniques is not UNSET:
            field_dict["mitre_attack_techniques"] = mitre_attack_techniques
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if related_attack_patterns is not UNSET:
            field_dict["related_attack_patterns"] = related_attack_patterns
        if vc_configurations is not UNSET:
            field_dict["vcConfigurations"] = vc_configurations
        if vc_vulnerable_cp_es is not UNSET:
            field_dict["vcVulnerableCPEs"] = vc_vulnerable_cp_es
        if vulnerable_cpes is not UNSET:
            field_dict["vulnerable_cpes"] = vulnerable_cpes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_configurations import ApiConfigurations
        from ..models.api_cve_extended import ApiCVEExtended
        from ..models.api_impact_extended import ApiImpactExtended
        from ..models.api_mitre_attack_tech import ApiMitreAttackTech
        from ..models.api_related_attack_pattern import ApiRelatedAttackPattern

        d = dict(src_dict)
        field_timestamp = d.pop("_timestamp", UNSET)

        _configurations = d.pop("configurations", UNSET)
        configurations: Union[Unset, ApiConfigurations]
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = ApiConfigurations.from_dict(_configurations)

        _cve = d.pop("cve", UNSET)
        cve: Union[Unset, ApiCVEExtended]
        if isinstance(_cve, Unset):
            cve = UNSET
        else:
            cve = ApiCVEExtended.from_dict(_cve)

        date_added = d.pop("date_added", UNSET)

        document_generation_date = d.pop("documentGenerationDate", UNSET)

        _impact = d.pop("impact", UNSET)
        impact: Union[Unset, ApiImpactExtended]
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = ApiImpactExtended.from_dict(_impact)

        last_modified_date = d.pop("lastModifiedDate", UNSET)

        mitre_attack_techniques = []
        _mitre_attack_techniques = d.pop("mitre_attack_techniques", UNSET)
        for mitre_attack_techniques_item_data in _mitre_attack_techniques or []:
            mitre_attack_techniques_item = ApiMitreAttackTech.from_dict(mitre_attack_techniques_item_data)

            mitre_attack_techniques.append(mitre_attack_techniques_item)

        published_date = d.pop("publishedDate", UNSET)

        related_attack_patterns = []
        _related_attack_patterns = d.pop("related_attack_patterns", UNSET)
        for related_attack_patterns_item_data in _related_attack_patterns or []:
            related_attack_patterns_item = ApiRelatedAttackPattern.from_dict(related_attack_patterns_item_data)

            related_attack_patterns.append(related_attack_patterns_item)

        _vc_configurations = d.pop("vcConfigurations", UNSET)
        vc_configurations: Union[Unset, ApiConfigurations]
        if isinstance(_vc_configurations, Unset):
            vc_configurations = UNSET
        else:
            vc_configurations = ApiConfigurations.from_dict(_vc_configurations)

        vc_vulnerable_cp_es = cast(list[str], d.pop("vcVulnerableCPEs", UNSET))

        vulnerable_cpes = cast(list[str], d.pop("vulnerable_cpes", UNSET))

        api_cve_items_extended = cls(
            field_timestamp=field_timestamp,
            configurations=configurations,
            cve=cve,
            date_added=date_added,
            document_generation_date=document_generation_date,
            impact=impact,
            last_modified_date=last_modified_date,
            mitre_attack_techniques=mitre_attack_techniques,
            published_date=published_date,
            related_attack_patterns=related_attack_patterns,
            vc_configurations=vc_configurations,
            vc_vulnerable_cp_es=vc_vulnerable_cp_es,
            vulnerable_cpes=vulnerable_cpes,
        )

        api_cve_items_extended.additional_properties = d
        return api_cve_items_extended

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
