from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryGitlabAdvisory")


@_attrs_define
class AdvisoryGitlabAdvisory:
    """
    Attributes:
        affected_range (Union[Unset, str]):
        affected_versions (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss_v2 (Union[Unset, str]):
        cvss_v3 (Union[Unset, str]):
        cwe (Union[Unset, list[str]]):
        date (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        filename (Union[Unset, str]):
        fixed_versions (Union[Unset, list[str]]):
        ghsa (Union[Unset, list[str]]):
        gitlab_url (Union[Unset, str]):
        identifier (Union[Unset, str]):
        identifiers (Union[Unset, list[str]]):
        not_impacted (Union[Unset, str]):
        package_manager (Union[Unset, str]):
        package_name (Union[Unset, str]):
        package_slug (Union[Unset, str]):
        pubdate (Union[Unset, str]):
        solution (Union[Unset, str]):
        title (Union[Unset, str]):
        urls (Union[Unset, list[str]]):
        uuid (Union[Unset, str]):
    """

    affected_range: Union[Unset, str] = UNSET
    affected_versions: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_v2: Union[Unset, str] = UNSET
    cvss_v3: Union[Unset, str] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    fixed_versions: Union[Unset, list[str]] = UNSET
    ghsa: Union[Unset, list[str]] = UNSET
    gitlab_url: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    identifiers: Union[Unset, list[str]] = UNSET
    not_impacted: Union[Unset, str] = UNSET
    package_manager: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    package_slug: Union[Unset, str] = UNSET
    pubdate: Union[Unset, str] = UNSET
    solution: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    urls: Union[Unset, list[str]] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_range = self.affected_range

        affected_versions = self.affected_versions

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_v2 = self.cvss_v2

        cvss_v3 = self.cvss_v3

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date = self.date

        date_added = self.date_added

        description = self.description

        filename = self.filename

        fixed_versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixed_versions, Unset):
            fixed_versions = self.fixed_versions

        ghsa: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ghsa, Unset):
            ghsa = self.ghsa

        gitlab_url = self.gitlab_url

        identifier = self.identifier

        identifiers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers

        not_impacted = self.not_impacted

        package_manager = self.package_manager

        package_name = self.package_name

        package_slug = self.package_slug

        pubdate = self.pubdate

        solution = self.solution

        title = self.title

        urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_range is not UNSET:
            field_dict["affected_range"] = affected_range
        if affected_versions is not UNSET:
            field_dict["affected_versions"] = affected_versions
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_v2 is not UNSET:
            field_dict["cvss_v2"] = cvss_v2
        if cvss_v3 is not UNSET:
            field_dict["cvss_v3"] = cvss_v3
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if filename is not UNSET:
            field_dict["filename"] = filename
        if fixed_versions is not UNSET:
            field_dict["fixed_versions"] = fixed_versions
        if ghsa is not UNSET:
            field_dict["ghsa"] = ghsa
        if gitlab_url is not UNSET:
            field_dict["gitlab_url"] = gitlab_url
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if not_impacted is not UNSET:
            field_dict["not_impacted"] = not_impacted
        if package_manager is not UNSET:
            field_dict["package_manager"] = package_manager
        if package_name is not UNSET:
            field_dict["package_name"] = package_name
        if package_slug is not UNSET:
            field_dict["package_slug"] = package_slug
        if pubdate is not UNSET:
            field_dict["pubdate"] = pubdate
        if solution is not UNSET:
            field_dict["solution"] = solution
        if title is not UNSET:
            field_dict["title"] = title
        if urls is not UNSET:
            field_dict["urls"] = urls
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_range = d.pop("affected_range", UNSET)

        affected_versions = d.pop("affected_versions", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_v2 = d.pop("cvss_v2", UNSET)

        cvss_v3 = d.pop("cvss_v3", UNSET)

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date = d.pop("date", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        filename = d.pop("filename", UNSET)

        fixed_versions = cast(list[str], d.pop("fixed_versions", UNSET))

        ghsa = cast(list[str], d.pop("ghsa", UNSET))

        gitlab_url = d.pop("gitlab_url", UNSET)

        identifier = d.pop("identifier", UNSET)

        identifiers = cast(list[str], d.pop("identifiers", UNSET))

        not_impacted = d.pop("not_impacted", UNSET)

        package_manager = d.pop("package_manager", UNSET)

        package_name = d.pop("package_name", UNSET)

        package_slug = d.pop("package_slug", UNSET)

        pubdate = d.pop("pubdate", UNSET)

        solution = d.pop("solution", UNSET)

        title = d.pop("title", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        uuid = d.pop("uuid", UNSET)

        advisory_gitlab_advisory = cls(
            affected_range=affected_range,
            affected_versions=affected_versions,
            cve=cve,
            cvss_v2=cvss_v2,
            cvss_v3=cvss_v3,
            cwe=cwe,
            date=date,
            date_added=date_added,
            description=description,
            filename=filename,
            fixed_versions=fixed_versions,
            ghsa=ghsa,
            gitlab_url=gitlab_url,
            identifier=identifier,
            identifiers=identifiers,
            not_impacted=not_impacted,
            package_manager=package_manager,
            package_name=package_name,
            package_slug=package_slug,
            pubdate=pubdate,
            solution=solution,
            title=title,
            urls=urls,
            uuid=uuid,
        )

        advisory_gitlab_advisory.additional_properties = d
        return advisory_gitlab_advisory

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
