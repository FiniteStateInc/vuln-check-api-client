from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryJVN")


@_attrs_define
class AdvisoryJVN:
    """
    Attributes:
        affected_en (Union[Unset, str]):
        affected_ja (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description_en (Union[Unset, str]):
        description_ja (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        solution_en (Union[Unset, str]):
        solution_ja (Union[Unset, str]):
        summary_en (Union[Unset, str]):
        summary_ja (Union[Unset, str]):
        title_en (Union[Unset, str]):
        title_ja (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_en: Union[Unset, str] = UNSET
    affected_ja: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description_en: Union[Unset, str] = UNSET
    description_ja: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    solution_en: Union[Unset, str] = UNSET
    solution_ja: Union[Unset, str] = UNSET
    summary_en: Union[Unset, str] = UNSET
    summary_ja: Union[Unset, str] = UNSET
    title_en: Union[Unset, str] = UNSET
    title_ja: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_en = self.affected_en

        affected_ja = self.affected_ja

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description_en = self.description_en

        description_ja = self.description_ja

        id = self.id

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        solution_en = self.solution_en

        solution_ja = self.solution_ja

        summary_en = self.summary_en

        summary_ja = self.summary_ja

        title_en = self.title_en

        title_ja = self.title_ja

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_en is not UNSET:
            field_dict["affected_en"] = affected_en
        if affected_ja is not UNSET:
            field_dict["affected_ja"] = affected_ja
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if description_ja is not UNSET:
            field_dict["description_ja"] = description_ja
        if id is not UNSET:
            field_dict["id"] = id
        if references is not UNSET:
            field_dict["references"] = references
        if solution_en is not UNSET:
            field_dict["solution_en"] = solution_en
        if solution_ja is not UNSET:
            field_dict["solution_ja"] = solution_ja
        if summary_en is not UNSET:
            field_dict["summary_en"] = summary_en
        if summary_ja is not UNSET:
            field_dict["summary_ja"] = summary_ja
        if title_en is not UNSET:
            field_dict["title_en"] = title_en
        if title_ja is not UNSET:
            field_dict["title_ja"] = title_ja
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_en = d.pop("affected_en", UNSET)

        affected_ja = d.pop("affected_ja", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description_en = d.pop("description_en", UNSET)

        description_ja = d.pop("description_ja", UNSET)

        id = d.pop("id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        solution_en = d.pop("solution_en", UNSET)

        solution_ja = d.pop("solution_ja", UNSET)

        summary_en = d.pop("summary_en", UNSET)

        summary_ja = d.pop("summary_ja", UNSET)

        title_en = d.pop("title_en", UNSET)

        title_ja = d.pop("title_ja", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_jvn = cls(
            affected_en=affected_en,
            affected_ja=affected_ja,
            cve=cve,
            date_added=date_added,
            description_en=description_en,
            description_ja=description_ja,
            id=id,
            references=references,
            solution_en=solution_en,
            solution_ja=solution_ja,
            summary_en=summary_en,
            summary_ja=summary_ja,
            title_en=title_en,
            title_ja=title_ja,
            updated_at=updated_at,
            url=url,
        )

        advisory_jvn.additional_properties = d
        return advisory_jvn

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
