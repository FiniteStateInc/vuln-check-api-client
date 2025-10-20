from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration
    from ..models.api_nvd20_description import ApiNVD20Description
    from ..models.api_nvd20_metric import ApiNVD20Metric
    from ..models.api_nvd20_reference import ApiNVD20Reference
    from ..models.api_nvd20_vendor_comment import ApiNVD20VendorComment
    from ..models.api_nvd20_weakness import ApiNVD20Weakness


T = TypeVar("T", bound="ApiNVD20CVE")


@_attrs_define
class ApiNVD20CVE:
    """
    Attributes:
        cisa_action_due (Union[Unset, str]):
        cisa_exploit_add (Union[Unset, str]):
        cisa_required_action (Union[Unset, str]):
        cisa_vulnerability_name (Union[Unset, str]):
        configurations (Union[Unset, list['AdvisoryNVD20Configuration']]):
        descriptions (Union[Unset, list['ApiNVD20Description']]):
        evaluator_comment (Union[Unset, str]):
        evaluator_impact (Union[Unset, str]):
        evaluator_solution (Union[Unset, str]):
        id (Union[Unset, str]):
        last_modified (Union[Unset, str]):
        metrics (Union[Unset, ApiNVD20Metric]):
        published (Union[Unset, str]):
        references (Union[Unset, list['ApiNVD20Reference']]):
        source_identifier (Union[Unset, str]):
        vc_configurations (Union[Unset, list['AdvisoryNVD20Configuration']]):
        vc_vulnerable_cp_es (Union[Unset, list[str]]):
        vendor_comments (Union[Unset, list['ApiNVD20VendorComment']]):
        vuln_status (Union[Unset, str]):
        weaknesses (Union[Unset, list['ApiNVD20Weakness']]):
    """

    cisa_action_due: Union[Unset, str] = UNSET
    cisa_exploit_add: Union[Unset, str] = UNSET
    cisa_required_action: Union[Unset, str] = UNSET
    cisa_vulnerability_name: Union[Unset, str] = UNSET
    configurations: Union[Unset, list["AdvisoryNVD20Configuration"]] = UNSET
    descriptions: Union[Unset, list["ApiNVD20Description"]] = UNSET
    evaluator_comment: Union[Unset, str] = UNSET
    evaluator_impact: Union[Unset, str] = UNSET
    evaluator_solution: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    metrics: Union[Unset, "ApiNVD20Metric"] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["ApiNVD20Reference"]] = UNSET
    source_identifier: Union[Unset, str] = UNSET
    vc_configurations: Union[Unset, list["AdvisoryNVD20Configuration"]] = UNSET
    vc_vulnerable_cp_es: Union[Unset, list[str]] = UNSET
    vendor_comments: Union[Unset, list["ApiNVD20VendorComment"]] = UNSET
    vuln_status: Union[Unset, str] = UNSET
    weaknesses: Union[Unset, list["ApiNVD20Weakness"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        descriptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)

        evaluator_comment = self.evaluator_comment

        evaluator_impact = self.evaluator_impact

        evaluator_solution = self.evaluator_solution

        id = self.id

        last_modified = self.last_modified

        metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

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

        weaknesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.weaknesses, Unset):
            weaknesses = []
            for weaknesses_item_data in self.weaknesses:
                weaknesses_item = weaknesses_item_data.to_dict()
                weaknesses.append(weaknesses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
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
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references
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
        if weaknesses is not UNSET:
            field_dict["weaknesses"] = weaknesses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_nvd20_configuration import AdvisoryNVD20Configuration
        from ..models.api_nvd20_description import ApiNVD20Description
        from ..models.api_nvd20_metric import ApiNVD20Metric
        from ..models.api_nvd20_reference import ApiNVD20Reference
        from ..models.api_nvd20_vendor_comment import ApiNVD20VendorComment
        from ..models.api_nvd20_weakness import ApiNVD20Weakness

        d = dict(src_dict)
        cisa_action_due = d.pop("cisaActionDue", UNSET)

        cisa_exploit_add = d.pop("cisaExploitAdd", UNSET)

        cisa_required_action = d.pop("cisaRequiredAction", UNSET)

        cisa_vulnerability_name = d.pop("cisaVulnerabilityName", UNSET)

        configurations = []
        _configurations = d.pop("configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = AdvisoryNVD20Configuration.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        descriptions = []
        _descriptions = d.pop("descriptions", UNSET)
        for descriptions_item_data in _descriptions or []:
            descriptions_item = ApiNVD20Description.from_dict(descriptions_item_data)

            descriptions.append(descriptions_item)

        evaluator_comment = d.pop("evaluatorComment", UNSET)

        evaluator_impact = d.pop("evaluatorImpact", UNSET)

        evaluator_solution = d.pop("evaluatorSolution", UNSET)

        id = d.pop("id", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, ApiNVD20Metric]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = ApiNVD20Metric.from_dict(_metrics)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = ApiNVD20Reference.from_dict(references_item_data)

            references.append(references_item)

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

        weaknesses = []
        _weaknesses = d.pop("weaknesses", UNSET)
        for weaknesses_item_data in _weaknesses or []:
            weaknesses_item = ApiNVD20Weakness.from_dict(weaknesses_item_data)

            weaknesses.append(weaknesses_item)

        api_nvd20cve = cls(
            cisa_action_due=cisa_action_due,
            cisa_exploit_add=cisa_exploit_add,
            cisa_required_action=cisa_required_action,
            cisa_vulnerability_name=cisa_vulnerability_name,
            configurations=configurations,
            descriptions=descriptions,
            evaluator_comment=evaluator_comment,
            evaluator_impact=evaluator_impact,
            evaluator_solution=evaluator_solution,
            id=id,
            last_modified=last_modified,
            metrics=metrics,
            published=published,
            references=references,
            source_identifier=source_identifier,
            vc_configurations=vc_configurations,
            vc_vulnerable_cp_es=vc_vulnerable_cp_es,
            vendor_comments=vendor_comments,
            vuln_status=vuln_status,
            weaknesses=weaknesses,
        )

        api_nvd20cve.additional_properties = d
        return api_nvd20cve

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
