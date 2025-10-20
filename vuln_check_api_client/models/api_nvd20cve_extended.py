from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration
    from ..models.api_categorization_extended import ApiCategorizationExtended
    from ..models.api_mitre_attack_tech import ApiMitreAttackTech
    from ..models.api_nvd20_description import ApiNVD20Description
    from ..models.api_nvd20_metric_extended import ApiNVD20MetricExtended
    from ..models.api_nvd20_reference_extended import ApiNVD20ReferenceExtended
    from ..models.api_nvd20_vendor_comment import ApiNVD20VendorComment
    from ..models.api_nvd20_weakness_extended import ApiNVD20WeaknessExtended
    from ..models.api_related_attack_pattern import ApiRelatedAttackPattern


T = TypeVar("T", bound="ApiNVD20CVEExtended")


@_attrs_define
class ApiNVD20CVEExtended:
    """
    Attributes:
        alias (Union[Unset, str]):
        status (Union[Unset, str]):
        field_timestamp (Union[Unset, str]): the deep tag instructs deep.Equal to ignore this field (used during
            OpenSearch loading)
        categorization (Union[Unset, ApiCategorizationExtended]):
        cisa_action_due (Union[Unset, str]):
        cisa_exploit_add (Union[Unset, str]):
        cisa_required_action (Union[Unset, str]):
        cisa_vulnerability_name (Union[Unset, str]):
        configurations (Union[Unset, list['AdvisoryNVD20Configuration']]):
        date_added (Union[Unset, str]):
        descriptions (Union[Unset, list['ApiNVD20Description']]):
        document_generation_date (Union[Unset, str]):
        evaluator_comment (Union[Unset, str]):
        evaluator_impact (Union[Unset, str]):
        evaluator_solution (Union[Unset, str]):
        id (Union[Unset, str]):
        last_modified (Union[Unset, str]):
        metrics (Union[Unset, ApiNVD20MetricExtended]):
        mitre_attack_techniques (Union[Unset, list['ApiMitreAttackTech']]):
        published (Union[Unset, str]):
        references (Union[Unset, list['ApiNVD20ReferenceExtended']]):
        related_attack_patterns (Union[Unset, list['ApiRelatedAttackPattern']]):
        source_identifier (Union[Unset, str]):
        vc_configurations (Union[Unset, list['AdvisoryNVD20Configuration']]):
        vc_vulnerable_cp_es (Union[Unset, list[str]]):
        vendor_comments (Union[Unset, list['ApiNVD20VendorComment']]):
        vuln_status (Union[Unset, str]):
        vulncheck_kev_exploit_add (Union[Unset, str]):
        vulnerable_cp_es (Union[Unset, list[str]]):
        weaknesses (Union[Unset, list['ApiNVD20WeaknessExtended']]):
    """

    alias: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    field_timestamp: Union[Unset, str] = UNSET
    categorization: Union[Unset, "ApiCategorizationExtended"] = UNSET
    cisa_action_due: Union[Unset, str] = UNSET
    cisa_exploit_add: Union[Unset, str] = UNSET
    cisa_required_action: Union[Unset, str] = UNSET
    cisa_vulnerability_name: Union[Unset, str] = UNSET
    configurations: Union[Unset, list["AdvisoryNVD20Configuration"]] = UNSET
    date_added: Union[Unset, str] = UNSET
    descriptions: Union[Unset, list["ApiNVD20Description"]] = UNSET
    document_generation_date: Union[Unset, str] = UNSET
    evaluator_comment: Union[Unset, str] = UNSET
    evaluator_impact: Union[Unset, str] = UNSET
    evaluator_solution: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    metrics: Union[Unset, "ApiNVD20MetricExtended"] = UNSET
    mitre_attack_techniques: Union[Unset, list["ApiMitreAttackTech"]] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["ApiNVD20ReferenceExtended"]] = UNSET
    related_attack_patterns: Union[Unset, list["ApiRelatedAttackPattern"]] = UNSET
    source_identifier: Union[Unset, str] = UNSET
    vc_configurations: Union[Unset, list["AdvisoryNVD20Configuration"]] = UNSET
    vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
    vendor_comments: Union[Unset, list["ApiNVD20VendorComment"]] = UNSET
    vuln_status: Union[Unset, str] = UNSET
    vulncheck_kev_exploit_add: Union[Unset, str] = UNSET
    vulnerable_cp_es: Union[Unset, list[str]] = UNSET
    weaknesses: Union[Unset, list["ApiNVD20WeaknessExtended"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        status = self.status

        field_timestamp = self.field_timestamp

        categorization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.categorization, Unset):
            categorization = self.categorization.to_dict()

        cisa_action_due = self.cisa_action_due

        cisa_exploit_add = self.cisa_exploit_add

        cisa_required_action = self.cisa_required_action

        cisa_vulnerability_name = self.cisa_vulnerability_name

        configurations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item = configurations_item_data.to_dict()
                configurations.append(configurations_item)

        date_added = self.date_added

        descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)

        document_generation_date = self.document_generation_date

        evaluator_comment = self.evaluator_comment

        evaluator_impact = self.evaluator_impact

        evaluator_solution = self.evaluator_solution

        id = self.id

        last_modified = self.last_modified

        metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        mitre_attack_techniques: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mitre_attack_techniques, Unset):
            mitre_attack_techniques = []
            for mitre_attack_techniques_item_data in self.mitre_attack_techniques:
                mitre_attack_techniques_item = mitre_attack_techniques_item_data.to_dict()
                mitre_attack_techniques.append(mitre_attack_techniques_item)

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        related_attack_patterns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related_attack_patterns, Unset):
            related_attack_patterns = []
            for related_attack_patterns_item_data in self.related_attack_patterns:
                related_attack_patterns_item = related_attack_patterns_item_data.to_dict()
                related_attack_patterns.append(related_attack_patterns_item)

        source_identifier = self.source_identifier

        vc_configurations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vc_configurations, Unset):
            vc_configurations = []
            for vc_configurations_item_data in self.vc_configurations:
                vc_configurations_item = vc_configurations_item_data.to_dict()
                vc_configurations.append(vc_configurations_item)

        vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vc_vulnerable_cp_es, Unset):
            vc_vulnerable_cp_es = self.vc_vulnerable_cp_es

        vendor_comments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vendor_comments, Unset):
            vendor_comments = []
            for vendor_comments_item_data in self.vendor_comments:
                vendor_comments_item = vendor_comments_item_data.to_dict()
                vendor_comments.append(vendor_comments_item)

        vuln_status = self.vuln_status

        vulncheck_kev_exploit_add = self.vulncheck_kev_exploit_add

        vulnerable_cp_es: Union[Unset, list[str]] = UNSET
        if not isinstance(self.vulnerable_cp_es, Unset):
            vulnerable_cp_es = self.vulnerable_cp_es

        weaknesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.weaknesses, Unset):
            weaknesses = []
            for weaknesses_item_data in self.weaknesses:
                weaknesses_item = weaknesses_item_data.to_dict()
                weaknesses.append(weaknesses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["ALIAS"] = alias
        if status is not UNSET:
            field_dict["STATUS"] = status
        if field_timestamp is not UNSET:
            field_dict["_timestamp"] = field_timestamp
        if categorization is not UNSET:
            field_dict["categorization"] = categorization
        if cisa_action_due is not UNSET:
            field_dict["cisaActionDue"] = cisa_action_due
        if cisa_exploit_add is not UNSET:
            field_dict["cisaExploitAdd"] = cisa_exploit_add
        if cisa_required_action is not UNSET:
            field_dict["cisaRequiredAction"] = cisa_required_action
        if cisa_vulnerability_name is not UNSET:
            field_dict["cisaVulnerabilityName"] = cisa_vulnerability_name
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if document_generation_date is not UNSET:
            field_dict["documentGenerationDate"] = document_generation_date
        if evaluator_comment is not UNSET:
            field_dict["evaluatorComment"] = evaluator_comment
        if evaluator_impact is not UNSET:
            field_dict["evaluatorImpact"] = evaluator_impact
        if evaluator_solution is not UNSET:
            field_dict["evaluatorSolution"] = evaluator_solution
        if id is not UNSET:
            field_dict["id"] = id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if mitre_attack_techniques is not UNSET:
            field_dict["mitreAttackTechniques"] = mitre_attack_techniques
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references
        if related_attack_patterns is not UNSET:
            field_dict["relatedAttackPatterns"] = related_attack_patterns
        if source_identifier is not UNSET:
            field_dict["sourceIdentifier"] = source_identifier
        if vc_configurations is not UNSET:
            field_dict["vcConfigurations"] = vc_configurations
        if vc_vulnerable_cp_es is not UNSET:
            field_dict["vcVulnerableCPEs"] = vc_vulnerable_cp_es
        if vendor_comments is not UNSET:
            field_dict["vendorComments"] = vendor_comments
        if vuln_status is not UNSET:
            field_dict["vulnStatus"] = vuln_status
        if vulncheck_kev_exploit_add is not UNSET:
            field_dict["vulncheckKEVExploitAdd"] = vulncheck_kev_exploit_add
        if vulnerable_cp_es is not UNSET:
            field_dict["vulnerableCPEs"] = vulnerable_cp_es
        if weaknesses is not UNSET:
            field_dict["weaknesses"] = weaknesses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration
        from ..models.api_categorization_extended import ApiCategorizationExtended
        from ..models.api_mitre_attack_tech import ApiMitreAttackTech
        from ..models.api_nvd20_description import ApiNVD20Description
        from ..models.api_nvd20_metric_extended import ApiNVD20MetricExtended
        from ..models.api_nvd20_reference_extended import ApiNVD20ReferenceExtended
        from ..models.api_nvd20_vendor_comment import ApiNVD20VendorComment
        from ..models.api_nvd20_weakness_extended import ApiNVD20WeaknessExtended
        from ..models.api_related_attack_pattern import ApiRelatedAttackPattern

        d = dict(src_dict)
        alias = d.pop("ALIAS", UNSET)

        status = d.pop("STATUS", UNSET)

        field_timestamp = d.pop("_timestamp", UNSET)

        _categorization = d.pop("categorization", UNSET)
        categorization: Union[Unset, ApiCategorizationExtended]
        if isinstance(_categorization, Unset):
            categorization = UNSET
        else:
            categorization = ApiCategorizationExtended.from_dict(_categorization)

        cisa_action_due = d.pop("cisaActionDue", UNSET)

        cisa_exploit_add = d.pop("cisaExploitAdd", UNSET)

        cisa_required_action = d.pop("cisaRequiredAction", UNSET)

        cisa_vulnerability_name = d.pop("cisaVulnerabilityName", UNSET)

        configurations = []
        _configurations = d.pop("configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = AdvisoryNVD20Configuration.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        date_added = d.pop("date_added", UNSET)

        descriptions = []
        _descriptions = d.pop("descriptions", UNSET)
        for descriptions_item_data in _descriptions or []:
            descriptions_item = ApiNVD20Description.from_dict(descriptions_item_data)

            descriptions.append(descriptions_item)

        document_generation_date = d.pop("documentGenerationDate", UNSET)

        evaluator_comment = d.pop("evaluatorComment", UNSET)

        evaluator_impact = d.pop("evaluatorImpact", UNSET)

        evaluator_solution = d.pop("evaluatorSolution", UNSET)

        id = d.pop("id", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, ApiNVD20MetricExtended]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = ApiNVD20MetricExtended.from_dict(_metrics)

        mitre_attack_techniques = []
        _mitre_attack_techniques = d.pop("mitreAttackTechniques", UNSET)
        for mitre_attack_techniques_item_data in _mitre_attack_techniques or []:
            mitre_attack_techniques_item = ApiMitreAttackTech.from_dict(mitre_attack_techniques_item_data)

            mitre_attack_techniques.append(mitre_attack_techniques_item)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = ApiNVD20ReferenceExtended.from_dict(references_item_data)

            references.append(references_item)

        related_attack_patterns = []
        _related_attack_patterns = d.pop("relatedAttackPatterns", UNSET)
        for related_attack_patterns_item_data in _related_attack_patterns or []:
            related_attack_patterns_item = ApiRelatedAttackPattern.from_dict(related_attack_patterns_item_data)

            related_attack_patterns.append(related_attack_patterns_item)

        source_identifier = d.pop("sourceIdentifier", UNSET)

        vc_configurations = []
        _vc_configurations = d.pop("vcConfigurations", UNSET)
        for vc_configurations_item_data in _vc_configurations or []:
            vc_configurations_item = AdvisoryNVD20Configuration.from_dict(vc_configurations_item_data)

            vc_configurations.append(vc_configurations_item)

        vc_vulnerable_cp_es = cast(list[str], d.pop("vcVulnerableCPEs", UNSET))

        vendor_comments = []
        _vendor_comments = d.pop("vendorComments", UNSET)
        for vendor_comments_item_data in _vendor_comments or []:
            vendor_comments_item = ApiNVD20VendorComment.from_dict(vendor_comments_item_data)

            vendor_comments.append(vendor_comments_item)

        vuln_status = d.pop("vulnStatus", UNSET)

        vulncheck_kev_exploit_add = d.pop("vulncheckKEVExploitAdd", UNSET)

        vulnerable_cp_es = cast(list[str], d.pop("vulnerableCPEs", UNSET))

        weaknesses = []
        _weaknesses = d.pop("weaknesses", UNSET)
        for weaknesses_item_data in _weaknesses or []:
            weaknesses_item = ApiNVD20WeaknessExtended.from_dict(weaknesses_item_data)

            weaknesses.append(weaknesses_item)

        api_nvd20cve_extended = cls(
            alias=alias,
            status=status,
            field_timestamp=field_timestamp,
            categorization=categorization,
            cisa_action_due=cisa_action_due,
            cisa_exploit_add=cisa_exploit_add,
            cisa_required_action=cisa_required_action,
            cisa_vulnerability_name=cisa_vulnerability_name,
            configurations=configurations,
            date_added=date_added,
            descriptions=descriptions,
            document_generation_date=document_generation_date,
            evaluator_comment=evaluator_comment,
            evaluator_impact=evaluator_impact,
            evaluator_solution=evaluator_solution,
            id=id,
            last_modified=last_modified,
            metrics=metrics,
            mitre_attack_techniques=mitre_attack_techniques,
            published=published,
            references=references,
            related_attack_patterns=related_attack_patterns,
            source_identifier=source_identifier,
            vc_configurations=vc_configurations,
            vc_vulnerable_cp_es=vc_vulnerable_cp_es,
            vendor_comments=vendor_comments,
            vuln_status=vuln_status,
            vulncheck_kev_exploit_add=vulncheck_kev_exploit_add,
            vulnerable_cp_es=vulnerable_cp_es,
            weaknesses=weaknesses,
        )

        api_nvd20cve_extended.additional_properties = d
        return api_nvd20cve_extended

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
