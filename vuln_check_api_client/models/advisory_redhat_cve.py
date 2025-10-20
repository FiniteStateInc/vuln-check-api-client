from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_rel import AdvisoryAffectedRel
    from ..models.advisory_package_stat import AdvisoryPackageStat
    from ..models.advisory_vuln_check_package import AdvisoryVulnCheckPackage


T = TypeVar("T", bound="AdvisoryRedhatCVE")


@_attrs_define
class AdvisoryRedhatCVE:
    """
    Attributes:
        advisories (Union[Unset, list[str]]):
        advisory_csaf_vex_url (Union[Unset, list[str]]):
        affected_packages (Union[Unset, list[str]]): used for un-marshlling from redhat
        affected_release (Union[Unset, list['AdvisoryAffectedRel']]):
        bugzilla (Union[Unset, str]):
        bugzilla_description (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cve_csaf_vex_url (Union[Unset, str]):
        cvss3_score (Union[Unset, str]):
        cvss3_scoring_vector (Union[Unset, str]):
        cvss_score (Union[Unset, float]):
        cvss_scoring_vector (Union[Unset, str]):
        cwe (Union[Unset, str]):
        package_state (Union[Unset, list['AdvisoryPackageStat']]):
        packages (Union[Unset, list['AdvisoryVulnCheckPackage']]): used to index into vulncheck OS
        public_date (Union[Unset, str]):
        resource_url (Union[Unset, str]):
        severity (Union[Unset, str]):
    """

    advisories: Union[Unset, list[str]] = UNSET
    advisory_csaf_vex_url: Union[Unset, list[str]] = UNSET
    affected_packages: Union[Unset, list[str]] = UNSET
    affected_release: Union[Unset, list["AdvisoryAffectedRel"]] = UNSET
    bugzilla: Union[Unset, str] = UNSET
    bugzilla_description: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cve_csaf_vex_url: Union[Unset, str] = UNSET
    cvss3_score: Union[Unset, str] = UNSET
    cvss3_scoring_vector: Union[Unset, str] = UNSET
    cvss_score: Union[Unset, float] = UNSET
    cvss_scoring_vector: Union[Unset, str] = UNSET
    cwe: Union[Unset, str] = UNSET
    package_state: Union[Unset, list["AdvisoryPackageStat"]] = UNSET
    packages: Union[Unset, list["AdvisoryVulnCheckPackage"]] = UNSET
    public_date: Union[Unset, str] = UNSET
    resource_url: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.advisories, Unset):
            advisories = self.advisories

        advisory_csaf_vex_url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.advisory_csaf_vex_url, Unset):
            advisory_csaf_vex_url = self.advisory_csaf_vex_url

        affected_packages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_packages, Unset):
            affected_packages = self.affected_packages

        affected_release: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_release, Unset):
            affected_release = []
            for affected_release_item_data in self.affected_release:
                affected_release_item = affected_release_item_data.to_dict()
                affected_release.append(affected_release_item)

        bugzilla = self.bugzilla

        bugzilla_description = self.bugzilla_description

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cve_csaf_vex_url = self.cve_csaf_vex_url

        cvss3_score = self.cvss3_score

        cvss3_scoring_vector = self.cvss3_scoring_vector

        cvss_score = self.cvss_score

        cvss_scoring_vector = self.cvss_scoring_vector

        cwe = self.cwe

        package_state: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.package_state, Unset):
            package_state = []
            for package_state_item_data in self.package_state:
                package_state_item = package_state_item_data.to_dict()
                package_state.append(package_state_item)

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        public_date = self.public_date

        resource_url = self.resource_url

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisories is not UNSET:
            field_dict["advisories"] = advisories
        if advisory_csaf_vex_url is not UNSET:
            field_dict["advisory_csaf_vex_url"] = advisory_csaf_vex_url
        if affected_packages is not UNSET:
            field_dict["affected_packages"] = affected_packages
        if affected_release is not UNSET:
            field_dict["affected_release"] = affected_release
        if bugzilla is not UNSET:
            field_dict["bugzilla"] = bugzilla
        if bugzilla_description is not UNSET:
            field_dict["bugzilla_description"] = bugzilla_description
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cve_csaf_vex_url is not UNSET:
            field_dict["cve_csaf_vex_url"] = cve_csaf_vex_url
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if cvss3_scoring_vector is not UNSET:
            field_dict["cvss3_scoring_vector"] = cvss3_scoring_vector
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_scoring_vector is not UNSET:
            field_dict["cvss_scoring_vector"] = cvss_scoring_vector
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if package_state is not UNSET:
            field_dict["package_state"] = package_state
        if packages is not UNSET:
            field_dict["packages"] = packages
        if public_date is not UNSET:
            field_dict["public_date"] = public_date
        if resource_url is not UNSET:
            field_dict["resource_url"] = resource_url
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_rel import AdvisoryAffectedRel
        from ..models.advisory_package_stat import AdvisoryPackageStat
        from ..models.advisory_vuln_check_package import AdvisoryVulnCheckPackage

        d = dict(src_dict)
        advisories = cast(list[str], d.pop("advisories", UNSET))

        advisory_csaf_vex_url = cast(list[str], d.pop("advisory_csaf_vex_url", UNSET))

        affected_packages = cast(list[str], d.pop("affected_packages", UNSET))

        affected_release = []
        _affected_release = d.pop("affected_release", UNSET)
        for affected_release_item_data in _affected_release or []:
            affected_release_item = AdvisoryAffectedRel.from_dict(affected_release_item_data)

            affected_release.append(affected_release_item)

        bugzilla = d.pop("bugzilla", UNSET)

        bugzilla_description = d.pop("bugzilla_description", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cve_csaf_vex_url = d.pop("cve_csaf_vex_url", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        cvss3_scoring_vector = d.pop("cvss3_scoring_vector", UNSET)

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_scoring_vector = d.pop("cvss_scoring_vector", UNSET)

        cwe = d.pop("cwe", UNSET)

        package_state = []
        _package_state = d.pop("package_state", UNSET)
        for package_state_item_data in _package_state or []:
            package_state_item = AdvisoryPackageStat.from_dict(package_state_item_data)

            package_state.append(package_state_item)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = AdvisoryVulnCheckPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        public_date = d.pop("public_date", UNSET)

        resource_url = d.pop("resource_url", UNSET)

        severity = d.pop("severity", UNSET)

        advisory_redhat_cve = cls(
            advisories=advisories,
            advisory_csaf_vex_url=advisory_csaf_vex_url,
            affected_packages=affected_packages,
            affected_release=affected_release,
            bugzilla=bugzilla,
            bugzilla_description=bugzilla_description,
            cve=cve,
            cve_csaf_vex_url=cve_csaf_vex_url,
            cvss3_score=cvss3_score,
            cvss3_scoring_vector=cvss3_scoring_vector,
            cvss_score=cvss_score,
            cvss_scoring_vector=cvss_scoring_vector,
            cwe=cwe,
            package_state=package_state,
            packages=packages,
            public_date=public_date,
            resource_url=resource_url,
            severity=severity,
        )

        advisory_redhat_cve.additional_properties = d
        return advisory_redhat_cve

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
