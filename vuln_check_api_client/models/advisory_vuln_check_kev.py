from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_reported_exploit import AdvisoryReportedExploit
    from ..models.advisory_xdb import AdvisoryXDB


T = TypeVar("T", bound="AdvisoryVulnCheckKEV")


@_attrs_define
class AdvisoryVulnCheckKEV:
    """
    Attributes:
        field_timestamp (Union[Unset, str]):
        cisa_date_added (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwes (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        due_date (Union[Unset, str]):
        known_ransomware_campaign_use (Union[Unset, str]):
        product (Union[Unset, str]):
        reported_exploited_by_vulncheck_canaries (Union[Unset, bool]):
        required_action (Union[Unset, str]):
        short_description (Union[Unset, str]):
        vendor_project (Union[Unset, str]):
        vulncheck_reported_exploitation (Union[Unset, list['AdvisoryReportedExploit']]):
        vulncheck_xdb (Union[Unset, list['AdvisoryXDB']]):
        vulnerability_name (Union[Unset, str]):
    """

    field_timestamp: Union[Unset, str] = UNSET
    cisa_date_added: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwes: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    known_ransomware_campaign_use: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    reported_exploited_by_vulncheck_canaries: Union[Unset, bool] = UNSET
    required_action: Union[Unset, str] = UNSET
    short_description: Union[Unset, str] = UNSET
    vendor_project: Union[Unset, str] = UNSET
    vulncheck_reported_exploitation: Union[Unset, list["AdvisoryReportedExploit"]] = UNSET
    vulncheck_xdb: Union[Unset, list["AdvisoryXDB"]] = UNSET
    vulnerability_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_timestamp = self.field_timestamp

        cisa_date_added = self.cisa_date_added

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwes, Unset):
            cwes = self.cwes

        date_added = self.date_added

        due_date = self.due_date

        known_ransomware_campaign_use = self.known_ransomware_campaign_use

        product = self.product

        reported_exploited_by_vulncheck_canaries = self.reported_exploited_by_vulncheck_canaries

        required_action = self.required_action

        short_description = self.short_description

        vendor_project = self.vendor_project

        vulncheck_reported_exploitation: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulncheck_reported_exploitation, Unset):
            vulncheck_reported_exploitation = []
            for vulncheck_reported_exploitation_item_data in self.vulncheck_reported_exploitation:
                vulncheck_reported_exploitation_item = vulncheck_reported_exploitation_item_data.to_dict()
                vulncheck_reported_exploitation.append(vulncheck_reported_exploitation_item)

        vulncheck_xdb: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulncheck_xdb, Unset):
            vulncheck_xdb = []
            for vulncheck_xdb_item_data in self.vulncheck_xdb:
                vulncheck_xdb_item = vulncheck_xdb_item_data.to_dict()
                vulncheck_xdb.append(vulncheck_xdb_item)

        vulnerability_name = self.vulnerability_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_timestamp is not UNSET:
            field_dict["_timestamp"] = field_timestamp
        if cisa_date_added is not UNSET:
            field_dict["cisa_date_added"] = cisa_date_added
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwes is not UNSET:
            field_dict["cwes"] = cwes
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if known_ransomware_campaign_use is not UNSET:
            field_dict["knownRansomwareCampaignUse"] = known_ransomware_campaign_use
        if product is not UNSET:
            field_dict["product"] = product
        if reported_exploited_by_vulncheck_canaries is not UNSET:
            field_dict["reported_exploited_by_vulncheck_canaries"] = reported_exploited_by_vulncheck_canaries
        if required_action is not UNSET:
            field_dict["required_action"] = required_action
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if vendor_project is not UNSET:
            field_dict["vendorProject"] = vendor_project
        if vulncheck_reported_exploitation is not UNSET:
            field_dict["vulncheck_reported_exploitation"] = vulncheck_reported_exploitation
        if vulncheck_xdb is not UNSET:
            field_dict["vulncheck_xdb"] = vulncheck_xdb
        if vulnerability_name is not UNSET:
            field_dict["vulnerabilityName"] = vulnerability_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_reported_exploit import AdvisoryReportedExploit
        from ..models.advisory_xdb import AdvisoryXDB

        d = dict(src_dict)
        field_timestamp = d.pop("_timestamp", UNSET)

        cisa_date_added = d.pop("cisa_date_added", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwes = cast(list[str], d.pop("cwes", UNSET))

        date_added = d.pop("date_added", UNSET)

        due_date = d.pop("dueDate", UNSET)

        known_ransomware_campaign_use = d.pop("knownRansomwareCampaignUse", UNSET)

        product = d.pop("product", UNSET)

        reported_exploited_by_vulncheck_canaries = d.pop("reported_exploited_by_vulncheck_canaries", UNSET)

        required_action = d.pop("required_action", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        vendor_project = d.pop("vendorProject", UNSET)

        vulncheck_reported_exploitation = []
        _vulncheck_reported_exploitation = d.pop("vulncheck_reported_exploitation", UNSET)
        for vulncheck_reported_exploitation_item_data in _vulncheck_reported_exploitation or []:
            vulncheck_reported_exploitation_item = AdvisoryReportedExploit.from_dict(
                vulncheck_reported_exploitation_item_data
            )

            vulncheck_reported_exploitation.append(vulncheck_reported_exploitation_item)

        vulncheck_xdb = []
        _vulncheck_xdb = d.pop("vulncheck_xdb", UNSET)
        for vulncheck_xdb_item_data in _vulncheck_xdb or []:
            vulncheck_xdb_item = AdvisoryXDB.from_dict(vulncheck_xdb_item_data)

            vulncheck_xdb.append(vulncheck_xdb_item)

        vulnerability_name = d.pop("vulnerabilityName", UNSET)

        advisory_vuln_check_kev = cls(
            field_timestamp=field_timestamp,
            cisa_date_added=cisa_date_added,
            cve=cve,
            cwes=cwes,
            date_added=date_added,
            due_date=due_date,
            known_ransomware_campaign_use=known_ransomware_campaign_use,
            product=product,
            reported_exploited_by_vulncheck_canaries=reported_exploited_by_vulncheck_canaries,
            required_action=required_action,
            short_description=short_description,
            vendor_project=vendor_project,
            vulncheck_reported_exploitation=vulncheck_reported_exploitation,
            vulncheck_xdb=vulncheck_xdb,
            vulnerability_name=vulnerability_name,
        )

        advisory_vuln_check_kev.additional_properties = d
        return advisory_vuln_check_kev

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
