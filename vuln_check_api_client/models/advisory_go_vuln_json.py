from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_go_credits import AdvisoryGoCredits
    from ..models.advisory_go_vuln_affected import AdvisoryGoVulnAffected
    from ..models.advisory_go_vuln_reference import AdvisoryGoVulnReference


T = TypeVar("T", bound="AdvisoryGoVulnJSON")


@_attrs_define
class AdvisoryGoVulnJSON:
    """
    Attributes:
        advisory_url (Union[Unset, str]):
        affected (Union[Unset, list['AdvisoryGoVulnAffected']]):
        aliases (Union[Unset, list[str]]):
        credits_ (Union[Unset, list['AdvisoryGoCredits']]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        details (Union[Unset, str]):
        ghsa (Union[Unset, list[str]]):
        go_advisory_id (Union[Unset, str]):
        modified (Union[Unset, str]):
        published (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryGoVulnReference']]):
    """

    advisory_url: Union[Unset, str] = UNSET
    affected: Union[Unset, list["AdvisoryGoVulnAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    credits_: Union[Unset, list["AdvisoryGoCredits"]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    ghsa: Union[Unset, list[str]] = UNSET
    go_advisory_id: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryGoVulnReference"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_url = self.advisory_url

        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        credits_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = []
            for credits_item_data in self.credits_:
                credits_item = credits_item_data.to_dict()
                credits_.append(credits_item)

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        details = self.details

        ghsa: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ghsa, Unset):
            ghsa = self.ghsa

        go_advisory_id = self.go_advisory_id

        modified = self.modified

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_url is not UNSET:
            field_dict["advisory_url"] = advisory_url
        if affected is not UNSET:
            field_dict["affected"] = affected
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details is not UNSET:
            field_dict["details"] = details
        if ghsa is not UNSET:
            field_dict["ghsa"] = ghsa
        if go_advisory_id is not UNSET:
            field_dict["go_advisory_id"] = go_advisory_id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_go_credits import AdvisoryGoCredits
        from ..models.advisory_go_vuln_affected import AdvisoryGoVulnAffected
        from ..models.advisory_go_vuln_reference import AdvisoryGoVulnReference

        d = dict(src_dict)
        advisory_url = d.pop("advisory_url", UNSET)

        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryGoVulnAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        credits_ = []
        _credits_ = d.pop("credits", UNSET)
        for credits_item_data in _credits_ or []:
            credits_item = AdvisoryGoCredits.from_dict(credits_item_data)

            credits_.append(credits_item)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        details = d.pop("details", UNSET)

        ghsa = cast(list[str], d.pop("ghsa", UNSET))

        go_advisory_id = d.pop("go_advisory_id", UNSET)

        modified = d.pop("modified", UNSET)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryGoVulnReference.from_dict(references_item_data)

            references.append(references_item)

        advisory_go_vuln_json = cls(
            advisory_url=advisory_url,
            affected=affected,
            aliases=aliases,
            credits_=credits_,
            cve=cve,
            date_added=date_added,
            details=details,
            ghsa=ghsa,
            go_advisory_id=go_advisory_id,
            modified=modified,
            published=published,
            references=references,
        )

        advisory_go_vuln_json.additional_properties = d
        return advisory_go_vuln_json

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
