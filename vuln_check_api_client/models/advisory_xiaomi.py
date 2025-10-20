from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryXiaomi")


@_attrs_define
class AdvisoryXiaomi:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        internal_id (Union[Unset, str]):
        summary (Union[Unset, str]):
        summary_cn (Union[Unset, str]):
        title (Union[Unset, str]):
        title_cn (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    internal_id: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    summary_cn: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    title_cn: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        internal_id = self.internal_id

        summary = self.summary

        summary_cn = self.summary_cn

        title = self.title

        title_cn = self.title_cn

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if summary_cn is not UNSET:
            field_dict["summary_cn"] = summary_cn
        if title is not UNSET:
            field_dict["title"] = title
        if title_cn is not UNSET:
            field_dict["title_cn"] = title_cn
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        internal_id = d.pop("internal_id", UNSET)

        summary = d.pop("summary", UNSET)

        summary_cn = d.pop("summary_cn", UNSET)

        title = d.pop("title", UNSET)

        title_cn = d.pop("title_cn", UNSET)

        url = d.pop("url", UNSET)

        advisory_xiaomi = cls(
            cve=cve,
            date_added=date_added,
            internal_id=internal_id,
            summary=summary,
            summary_cn=summary_cn,
            title=title,
            title_cn=title_cn,
            url=url,
        )

        advisory_xiaomi.additional_properties = d
        return advisory_xiaomi

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
