from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_py_pa_affected import AdvisoryPyPAAffected
    from ..models.advisory_py_pa_reference import AdvisoryPyPAReference


T = TypeVar("T", bound="AdvisoryPyPAAdvisory")


@_attrs_define
class AdvisoryPyPAAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]): ID is the PYSEC- identifier
        affected (Union[Unset, list['AdvisoryPyPAAffected']]): Affected will list out the vulnerable versions.
        aliases (Union[Unset, list[str]]): Aliases are other identifiers that refer to this, such as a CVE
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        details (Union[Unset, str]): Details discuss the vulnerability information
        modified (Union[Unset, str]): Modified is non-zero Time if entry was updated
        published (Union[Unset, str]): Published is the datetime when this was released
        references (Union[Unset, list['AdvisoryPyPAReference']]): References are links to more detailed advisories,
            fixes, etc.
        was_withdrawn (Union[Unset, bool]): WasWD indicates if the advisory was withdrawn or not.
        withdrawn (Union[Unset, str]): Withdrawn is non-zero if this advisory has been withdrawn
    """

    advisory_id: Union[Unset, str] = UNSET
    affected: Union[Unset, list["AdvisoryPyPAAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    references: Union[Unset, list["AdvisoryPyPAReference"]] = UNSET
    was_withdrawn: Union[Unset, bool] = UNSET
    withdrawn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

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

        details = self.details

        modified = self.modified

        published = self.published

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        was_withdrawn = self.was_withdrawn

        withdrawn = self.withdrawn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if affected is not UNSET:
            field_dict["affected"] = affected
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details is not UNSET:
            field_dict["details"] = details
        if modified is not UNSET:
            field_dict["modified"] = modified
        if published is not UNSET:
            field_dict["published"] = published
        if references is not UNSET:
            field_dict["references"] = references
        if was_withdrawn is not UNSET:
            field_dict["was_withdrawn"] = was_withdrawn
        if withdrawn is not UNSET:
            field_dict["withdrawn"] = withdrawn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_py_pa_affected import AdvisoryPyPAAffected
        from ..models.advisory_py_pa_reference import AdvisoryPyPAReference

        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryPyPAAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        details = d.pop("details", UNSET)

        modified = d.pop("modified", UNSET)

        published = d.pop("published", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = AdvisoryPyPAReference.from_dict(references_item_data)

            references.append(references_item)

        was_withdrawn = d.pop("was_withdrawn", UNSET)

        withdrawn = d.pop("withdrawn", UNSET)

        advisory_py_pa_advisory = cls(
            advisory_id=advisory_id,
            affected=affected,
            aliases=aliases,
            cve=cve,
            date_added=date_added,
            details=details,
            modified=modified,
            published=published,
            references=references,
            was_withdrawn=was_withdrawn,
            withdrawn=withdrawn,
        )

        advisory_py_pa_advisory.additional_properties = d
        return advisory_py_pa_advisory

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
