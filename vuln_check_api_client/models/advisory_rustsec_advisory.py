from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_rustsec_affected import AdvisoryRustsecAffected
    from ..models.advisory_rustsec_front_matter_advisory import AdvisoryRustsecFrontMatterAdvisory
    from ..models.advisory_rustsec_front_matter_versions import AdvisoryRustsecFrontMatterVersions


T = TypeVar("T", bound="AdvisoryRustsecAdvisory")


@_attrs_define
class AdvisoryRustsecAdvisory:
    """
    Attributes:
        advisory (Union[Unset, AdvisoryRustsecFrontMatterAdvisory]):
        affected (Union[Unset, AdvisoryRustsecAffected]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        versions (Union[Unset, AdvisoryRustsecFrontMatterVersions]):
    """

    advisory: Union[Unset, "AdvisoryRustsecFrontMatterAdvisory"] = UNSET
    affected: Union[Unset, "AdvisoryRustsecAffected"] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    versions: Union[Unset, "AdvisoryRustsecFrontMatterVersions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.advisory, Unset):
            advisory = self.advisory.to_dict()

        affected: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = self.affected.to_dict()

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        versions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["advisory"] = advisory
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_rustsec_affected import AdvisoryRustsecAffected
        from ..models.advisory_rustsec_front_matter_advisory import AdvisoryRustsecFrontMatterAdvisory
        from ..models.advisory_rustsec_front_matter_versions import AdvisoryRustsecFrontMatterVersions

        d = dict(src_dict)
        _advisory = d.pop("advisory", UNSET)
        advisory: Union[Unset, AdvisoryRustsecFrontMatterAdvisory]
        if isinstance(_advisory, Unset):
            advisory = UNSET
        else:
            advisory = AdvisoryRustsecFrontMatterAdvisory.from_dict(_advisory)

        _affected = d.pop("affected", UNSET)
        affected: Union[Unset, AdvisoryRustsecAffected]
        if isinstance(_affected, Unset):
            affected = UNSET
        else:
            affected = AdvisoryRustsecAffected.from_dict(_affected)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        _versions = d.pop("versions", UNSET)
        versions: Union[Unset, AdvisoryRustsecFrontMatterVersions]
        if isinstance(_versions, Unset):
            versions = UNSET
        else:
            versions = AdvisoryRustsecFrontMatterVersions.from_dict(_versions)

        advisory_rustsec_advisory = cls(
            advisory=advisory,
            affected=affected,
            cve=cve,
            date_added=date_added,
            description=description,
            versions=versions,
        )

        advisory_rustsec_advisory.additional_properties = d
        return advisory_rustsec_advisory

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
