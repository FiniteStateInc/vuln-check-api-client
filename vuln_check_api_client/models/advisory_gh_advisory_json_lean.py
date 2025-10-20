from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cwes import AdvisoryCwes
    from ..models.advisory_gh_cvss import AdvisoryGHCvss
    from ..models.advisory_gh_identifier import AdvisoryGHIdentifier
    from ..models.advisory_gh_reference import AdvisoryGHReference
    from ..models.advisory_gh_vulnerabilities import AdvisoryGHVulnerabilities


T = TypeVar("T", bound="AdvisoryGHAdvisoryJSONLean")


@_attrs_define
class AdvisoryGHAdvisoryJSONLean:
    """
    Attributes:
        classification (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, AdvisoryGHCvss]):
        cwes (Union[Unset, AdvisoryCwes]):
        database_id (Union[Unset, int]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        ghsa_id (Union[Unset, str]):
        id (Union[Unset, str]):
        identifiers (Union[Unset, list['AdvisoryGHIdentifier']]):
        notifications_permalink (Union[Unset, str]):
        origin (Union[Unset, str]):
        permalink (Union[Unset, str]):
        published_at (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryGHReference']]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        updatedAt (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        vulnerabilities (Union[Unset, AdvisoryGHVulnerabilities]):
        withdrawn_at (Union[Unset, str]):
    """

    classification: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, "AdvisoryGHCvss"] = UNSET
    cwes: Union[Unset, "AdvisoryCwes"] = UNSET
    database_id: Union[Unset, int] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ghsa_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    identifiers: Union[Unset, list["AdvisoryGHIdentifier"]] = UNSET
    notifications_permalink: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    permalink: Union[Unset, str] = UNSET
    published_at: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryGHReference"]] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    updatedAt: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vulnerabilities: Union[Unset, "AdvisoryGHVulnerabilities"] = UNSET
    withdrawn_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification = self.classification

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss, Unset):
            cvss = self.cvss.to_dict()

        cwes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cwes, Unset):
            cwes = self.cwes.to_dict()

        database_id = self.database_id

        date_added = self.date_added

        description = self.description

        ghsa_id = self.ghsa_id

        id = self.id

        identifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        notifications_permalink = self.notifications_permalink

        origin = self.origin

        permalink = self.permalink

        published_at = self.published_at

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        severity = self.severity

        summary = self.summary

        updatedAt = self.updatedAt

        updated_at = self.updated_at

        vulnerabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = self.vulnerabilities.to_dict()

        withdrawn_at = self.withdrawn_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification is not UNSET:
            field_dict["classification"] = classification
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if cwes is not UNSET:
            field_dict["cwes"] = cwes
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if ghsa_id is not UNSET:
            field_dict["ghsaId"] = ghsa_id
        if id is not UNSET:
            field_dict["id"] = id
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if notifications_permalink is not UNSET:
            field_dict["notificationsPermalink"] = notifications_permalink
        if origin is not UNSET:
            field_dict["origin"] = origin
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if references is not UNSET:
            field_dict["references"] = references
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if updatedAt is not UNSET:
            field_dict["updatedAt"] = updatedAt
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities
        if withdrawn_at is not UNSET:
            field_dict["withdrawnAt"] = withdrawn_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cwes import AdvisoryCwes
        from ..models.advisory_gh_cvss import AdvisoryGHCvss
        from ..models.advisory_gh_identifier import AdvisoryGHIdentifier
        from ..models.advisory_gh_reference import AdvisoryGHReference
        from ..models.advisory_gh_vulnerabilities import AdvisoryGHVulnerabilities

        d = dict(src_dict)
        classification = d.pop("classification", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        _cvss = d.pop("cvss", UNSET)
        cvss: Union[Unset, AdvisoryGHCvss]
        if isinstance(_cvss, Unset):
            cvss = UNSET
        else:
            cvss = AdvisoryGHCvss.from_dict(_cvss)

        _cwes = d.pop("cwes", UNSET)
        cwes: Union[Unset, AdvisoryCwes]
        if isinstance(_cwes, Unset):
            cwes = UNSET
        else:
            cwes = AdvisoryCwes.from_dict(_cwes)

        database_id = d.pop("databaseId", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        ghsa_id = d.pop("ghsaId", UNSET)

        id = d.pop("id", UNSET)

        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for identifiers_item_data in _identifiers or []:
            identifiers_item = AdvisoryGHIdentifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        notifications_permalink = d.pop("notificationsPermalink", UNSET)

        origin = d.pop("origin", UNSET)

        permalink = d.pop("permalink", UNSET)

        published_at = d.pop("publishedAt", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryGHReference.from_dict(references_item_data)

            references.append(references_item)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        updatedAt = d.pop("updatedAt", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        vulnerabilities: Union[Unset, AdvisoryGHVulnerabilities]
        if isinstance(_vulnerabilities, Unset):
            vulnerabilities = UNSET
        else:
            vulnerabilities = AdvisoryGHVulnerabilities.from_dict(_vulnerabilities)

        withdrawn_at = d.pop("withdrawnAt", UNSET)

        advisory_gh_advisory_json_lean = cls(
            classification=classification,
            cve=cve,
            cvss=cvss,
            cwes=cwes,
            database_id=database_id,
            date_added=date_added,
            description=description,
            ghsa_id=ghsa_id,
            id=id,
            identifiers=identifiers,
            notifications_permalink=notifications_permalink,
            origin=origin,
            permalink=permalink,
            published_at=published_at,
            references=references,
            severity=severity,
            summary=summary,
            updatedAt=updatedAt,
            updated_at=updated_at,
            vulnerabilities=vulnerabilities,
            withdrawn_at=withdrawn_at,
        )

        advisory_gh_advisory_json_lean.additional_properties = d
        return advisory_gh_advisory_json_lean

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
