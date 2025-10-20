from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_android_affected import AdvisoryAndroidAffected
    from ..models.advisory_android_reference import AdvisoryAndroidReference


T = TypeVar("T", bound="AdvisoryAndroidAdvisory")


@_attrs_define
class AdvisoryAndroidAdvisory:
    """
    Attributes:
        affected (Union[Unset, list['AdvisoryAndroidAffected']]):
        aliases (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        modified (Union[Unset, str]):
        published (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryAndroidReference']]):
        summary (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected: Union[Unset, list["AdvisoryAndroidAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryAndroidReference"]] = UNSET
    summary: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        modified = self.modified

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        summary = self.summary

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references
        if summary is not UNSET:
            field_dict["summary"] = summary
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_android_affected import AdvisoryAndroidAffected
        from ..models.advisory_android_reference import AdvisoryAndroidReference

        d = dict(src_dict)
        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryAndroidAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        modified = d.pop("modified", UNSET)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryAndroidReference.from_dict(references_item_data)

            references.append(references_item)

        summary = d.pop("summary", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_android_advisory = cls(
            affected=affected,
            aliases=aliases,
            cve=cve,
            date_added=date_added,
            id=id,
            modified=modified,
            published=published,
            references=references,
            summary=summary,
            updated_at=updated_at,
            url=url,
        )

        advisory_android_advisory.additional_properties = d
        return advisory_android_advisory

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
