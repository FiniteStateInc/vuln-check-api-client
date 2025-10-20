from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_node_author import AdvisoryNodeAuthor


T = TypeVar("T", bound="AdvisoryNodeSecurity")


@_attrs_define
class AdvisoryNodeSecurity:
    """
    Attributes:
        affected_environments (Union[Unset, list[str]]):
        author (Union[Unset, AdvisoryNodeAuthor]):
        coordinating_vendor (Union[Unset, str]):
        created_at (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss_score (Union[Unset, float]):
        cvss_vector (Union[Unset, str]):
        date_added (Union[Unset, str]):
        id (Union[Unset, int]):
        module_name (Union[Unset, str]):
        overview (Union[Unset, str]):
        patched_versions (Union[Unset, str]):
        publish_date (Union[Unset, str]):
        recommendation (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        vulnerable_versions (Union[Unset, str]):
    """

    affected_environments: Union[Unset, list[str]] = UNSET
    author: Union[Unset, "AdvisoryNodeAuthor"] = UNSET
    coordinating_vendor: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_score: Union[Unset, float] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    module_name: Union[Unset, str] = UNSET
    overview: Union[Unset, str] = UNSET
    patched_versions: Union[Unset, str] = UNSET
    publish_date: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vulnerable_versions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_environments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_environments, Unset):
            affected_environments = self.affected_environments

        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        coordinating_vendor = self.coordinating_vendor

        created_at = self.created_at

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_score = self.cvss_score

        cvss_vector = self.cvss_vector

        date_added = self.date_added

        id = self.id

        module_name = self.module_name

        overview = self.overview

        patched_versions = self.patched_versions

        publish_date = self.publish_date

        recommendation = self.recommendation

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        title = self.title

        updated_at = self.updated_at

        url = self.url

        vulnerable_versions = self.vulnerable_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_environments is not UNSET:
            field_dict["affected_environments"] = affected_environments
        if author is not UNSET:
            field_dict["author"] = author
        if coordinating_vendor is not UNSET:
            field_dict["coordinating_vendor"] = coordinating_vendor
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if module_name is not UNSET:
            field_dict["module_name"] = module_name
        if overview is not UNSET:
            field_dict["overview"] = overview
        if patched_versions is not UNSET:
            field_dict["patched_versions"] = patched_versions
        if publish_date is not UNSET:
            field_dict["publish_date"] = publish_date
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if references is not UNSET:
            field_dict["references"] = references
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if vulnerable_versions is not UNSET:
            field_dict["vulnerable_versions"] = vulnerable_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_node_author import AdvisoryNodeAuthor

        d = dict(src_dict)
        affected_environments = cast(list[str], d.pop("affected_environments", UNSET))

        _author = d.pop("author", UNSET)
        author: Union[Unset, AdvisoryNodeAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = AdvisoryNodeAuthor.from_dict(_author)

        coordinating_vendor = d.pop("coordinating_vendor", UNSET)

        created_at = d.pop("created_at", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        module_name = d.pop("module_name", UNSET)

        overview = d.pop("overview", UNSET)

        patched_versions = d.pop("patched_versions", UNSET)

        publish_date = d.pop("publish_date", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        vulnerable_versions = d.pop("vulnerable_versions", UNSET)

        advisory_node_security = cls(
            affected_environments=affected_environments,
            author=author,
            coordinating_vendor=coordinating_vendor,
            created_at=created_at,
            cve=cve,
            cvss_score=cvss_score,
            cvss_vector=cvss_vector,
            date_added=date_added,
            id=id,
            module_name=module_name,
            overview=overview,
            patched_versions=patched_versions,
            publish_date=publish_date,
            recommendation=recommendation,
            references=references,
            title=title,
            updated_at=updated_at,
            url=url,
            vulnerable_versions=vulnerable_versions,
        )

        advisory_node_security.additional_properties = d
        return advisory_node_security

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
