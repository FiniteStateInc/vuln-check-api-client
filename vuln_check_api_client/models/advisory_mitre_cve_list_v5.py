from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mitre_cve_list_v5_ref import AdvisoryMitreCVEListV5Ref


T = TypeVar("T", bound="AdvisoryMitreCVEListV5")


@_attrs_define
class AdvisoryMitreCVEListV5:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        mitre_ref (Union[Unset, AdvisoryMitreCVEListV5Ref]):
        references (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    mitre_ref: Union[Unset, "AdvisoryMitreCVEListV5Ref"] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        mitre_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mitre_ref, Unset):
            mitre_ref = self.mitre_ref.to_dict()

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary = self.summary

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if mitre_ref is not UNSET:
            field_dict["mitre_ref"] = mitre_ref
        if references is not UNSET:
            field_dict["references"] = references
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mitre_cve_list_v5_ref import AdvisoryMitreCVEListV5Ref

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        _mitre_ref = d.pop("mitre_ref", UNSET)
        mitre_ref: Union[Unset, AdvisoryMitreCVEListV5Ref]
        if isinstance(_mitre_ref, Unset):
            mitre_ref = UNSET
        else:
            mitre_ref = AdvisoryMitreCVEListV5Ref.from_dict(_mitre_ref)

        references = cast(list[str], d.pop("references", UNSET))

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_mitre_cve_list_v5 = cls(
            cve=cve,
            date_added=date_added,
            mitre_ref=mitre_ref,
            references=references,
            summary=summary,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_mitre_cve_list_v5.additional_properties = d
        return advisory_mitre_cve_list_v5

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
