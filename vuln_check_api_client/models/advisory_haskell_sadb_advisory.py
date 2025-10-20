from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_haskell_affected import AdvisoryHaskellAffected
    from ..models.advisory_haskell_sadb_advisory_references import AdvisoryHaskellSADBAdvisoryReferences


T = TypeVar("T", bound="AdvisoryHaskellSADBAdvisory")


@_attrs_define
class AdvisoryHaskellSADBAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        affected_packages (Union[Unset, list['AdvisoryHaskellAffected']]):
        aliases (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        cwes (Union[Unset, list[int]]):
        date_added (Union[Unset, str]):
        keywords (Union[Unset, list[str]]):
        references (Union[Unset, AdvisoryHaskellSADBAdvisoryReferences]):
        related_vulns (Union[Unset, list[str]]):
    """

    advisory_id: Union[Unset, str] = UNSET
    affected_packages: Union[Unset, list["AdvisoryHaskellAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwes: Union[Unset, list[int]] = UNSET
    date_added: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    references: Union[Unset, "AdvisoryHaskellSADBAdvisoryReferences"] = UNSET
    related_vulns: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        affected_packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_packages, Unset):
            affected_packages = []
            for affected_packages_item_data in self.affected_packages:
                affected_packages_item = affected_packages_item_data.to_dict()
                affected_packages.append(affected_packages_item)

        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.cwes, Unset):
            cwes = self.cwes

        date_added = self.date_added

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        related_vulns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.related_vulns, Unset):
            related_vulns = self.related_vulns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisory_id"] = advisory_id
        if affected_packages is not UNSET:
            field_dict["affected_packages"] = affected_packages
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwes is not UNSET:
            field_dict["cwes"] = cwes
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if references is not UNSET:
            field_dict["references"] = references
        if related_vulns is not UNSET:
            field_dict["related_vulns"] = related_vulns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_haskell_affected import AdvisoryHaskellAffected
        from ..models.advisory_haskell_sadb_advisory_references import AdvisoryHaskellSADBAdvisoryReferences

        d = dict(src_dict)
        advisory_id = d.pop("advisory_id", UNSET)

        affected_packages = []
        _affected_packages = d.pop("affected_packages", UNSET)
        for affected_packages_item_data in _affected_packages or []:
            affected_packages_item = AdvisoryHaskellAffected.from_dict(affected_packages_item_data)

            affected_packages.append(affected_packages_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cwes = cast(list[int], d.pop("cwes", UNSET))

        date_added = d.pop("date_added", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        _references = d.pop("references", UNSET)
        references: Union[Unset, AdvisoryHaskellSADBAdvisoryReferences]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = AdvisoryHaskellSADBAdvisoryReferences.from_dict(_references)

        related_vulns = cast(list[str], d.pop("related_vulns", UNSET))

        advisory_haskell_sadb_advisory = cls(
            advisory_id=advisory_id,
            affected_packages=affected_packages,
            aliases=aliases,
            cve=cve,
            cwes=cwes,
            date_added=date_added,
            keywords=keywords,
            references=references,
            related_vulns=related_vulns,
        )

        advisory_haskell_sadb_advisory.additional_properties = d
        return advisory_haskell_sadb_advisory

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
