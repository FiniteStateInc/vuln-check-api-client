from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected import AdvisoryAffected
    from ..models.advisory_osv_reference import AdvisoryOSVReference


T = TypeVar("T", bound="AdvisoryOSVObj")


@_attrs_define
class AdvisoryOSVObj:
    """
    Attributes:
        affected (Union[Unset, list['AdvisoryAffected']]): collection based on https://ossf.github.io/osv-schema/
        aliases (Union[Unset, list[str]]):
        details (Union[Unset, str]):
        id (Union[Unset, str]):
        modified (Union[Unset, str]):
        published (Union[Unset, str]):
        references (Union[Unset, list['AdvisoryOSVReference']]):
        related (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        withdrawn (Union[Unset, str]):
    """

    affected: Union[Unset, list["AdvisoryAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    details: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryOSVReference"]] = UNSET
    related: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    withdrawn: Union[Unset, str] = UNSET
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

        details = self.details

        id = self.id

        modified = self.modified

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        related: Union[Unset, list[str]] = UNSET
        if not isinstance(self.related, Unset):
            related = self.related

        summary = self.summary

        withdrawn = self.withdrawn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references
        if related is not UNSET:
            field_dict["related"] = related
        if summary is not UNSET:
            field_dict["summary"] = summary
        if withdrawn is not UNSET:
            field_dict["withdrawn"] = withdrawn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected import AdvisoryAffected
        from ..models.advisory_osv_reference import AdvisoryOSVReference

        d = dict(src_dict)
        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        details = d.pop("details", UNSET)

        id = d.pop("id", UNSET)

        modified = d.pop("modified", UNSET)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryOSVReference.from_dict(references_item_data)

            references.append(references_item)

        related = cast(list[str], d.pop("related", UNSET))

        summary = d.pop("summary", UNSET)

        withdrawn = d.pop("withdrawn", UNSET)

        advisory_osv_obj = cls(
            affected=affected,
            aliases=aliases,
            details=details,
            id=id,
            modified=modified,
            published=published,
            references=references,
            related=related,
            summary=summary,
            withdrawn=withdrawn,
        )

        advisory_osv_obj.additional_properties = d
        return advisory_osv_obj

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
