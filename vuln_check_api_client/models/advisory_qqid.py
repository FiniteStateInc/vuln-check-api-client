from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryQQID")


@_attrs_define
class AdvisoryQQID:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cvss3_score (Union[Unset, str]):
        cvss_score (Union[Unset, str]):
        date_added (Union[Unset, str]):
        qid (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cvss3_score: Union[Unset, str] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    qid: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss3_score = self.cvss3_score

        cvss_score = self.cvss_score

        date_added = self.date_added

        qid = self.qid

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if qid is not UNSET:
            field_dict["qid"] = qid
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
        cve = cast(list[str], d.pop("cve", UNSET))

        cvss3_score = d.pop("cvss3_score", UNSET)

        cvss_score = d.pop("cvss_score", UNSET)

        date_added = d.pop("date_added", UNSET)

        qid = d.pop("qid", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_qqid = cls(
            cve=cve,
            cvss3_score=cvss3_score,
            cvss_score=cvss_score,
            date_added=date_added,
            qid=qid,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_qqid.additional_properties = d
        return advisory_qqid

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
