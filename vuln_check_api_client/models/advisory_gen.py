from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryGen")


@_attrs_define
class AdvisoryGen:
    """
    Attributes:
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss_score (Union[Unset, str]):
        cvss_vector (Union[Unset, str]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]): not all of them have this
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss_score = self.cvss_score

        cvss_vector = self.cvss_vector

        date_added = self.date_added

        id = self.id

        summary = self.summary

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_gen = cls(
            affected=affected,
            cve=cve,
            cvss_score=cvss_score,
            cvss_vector=cvss_vector,
            date_added=date_added,
            id=id,
            summary=summary,
            title=title,
            url=url,
        )

        advisory_gen.additional_properties = d
        return advisory_gen

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
