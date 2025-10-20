from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryJuniper")


@_attrs_define
class AdvisoryJuniper:
    """
    Attributes:
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss3_score (Union[Unset, str]):
        cvss3_vector (Union[Unset, str]):
        cvss4_score (Union[Unset, str]):
        cvss4_vector (Union[Unset, str]):
        date_added (Union[Unset, str]):
        fixed (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss3_score: Union[Unset, str] = UNSET
    cvss3_vector: Union[Unset, str] = UNSET
    cvss4_score: Union[Unset, str] = UNSET
    cvss4_vector: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss3_score = self.cvss3_score

        cvss3_vector = self.cvss3_vector

        cvss4_score = self.cvss4_score

        cvss4_vector = self.cvss4_vector

        date_added = self.date_added

        fixed = self.fixed

        id = self.id

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
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if cvss3_vector is not UNSET:
            field_dict["cvss3_vector"] = cvss3_vector
        if cvss4_score is not UNSET:
            field_dict["cvss4_score"] = cvss4_score
        if cvss4_vector is not UNSET:
            field_dict["cvss4_vector"] = cvss4_vector
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if id is not UNSET:
            field_dict["id"] = id
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
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss3_score = d.pop("cvss3_score", UNSET)

        cvss3_vector = d.pop("cvss3_vector", UNSET)

        cvss4_score = d.pop("cvss4_score", UNSET)

        cvss4_vector = d.pop("cvss4_vector", UNSET)

        date_added = d.pop("date_added", UNSET)

        fixed = d.pop("fixed", UNSET)

        id = d.pop("id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_juniper = cls(
            affected=affected,
            cve=cve,
            cvss3_score=cvss3_score,
            cvss3_vector=cvss3_vector,
            cvss4_score=cvss4_score,
            cvss4_vector=cvss4_vector,
            date_added=date_added,
            fixed=fixed,
            id=id,
            references=references,
            summary=summary,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_juniper.additional_properties = d
        return advisory_juniper

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
