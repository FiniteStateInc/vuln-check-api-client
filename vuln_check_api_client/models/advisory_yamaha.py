from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryYamaha")


@_attrs_define
class AdvisoryYamaha:
    """
    Attributes:
        affected (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        fixed (Union[Unset, str]):
        summary_ja (Union[Unset, str]):
        title_ja (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    summary_ja: Union[Unset, str] = UNSET
    title_ja: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        fixed = self.fixed

        summary_ja = self.summary_ja

        title_ja = self.title_ja

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if summary_ja is not UNSET:
            field_dict["summary_ja"] = summary_ja
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
        affected = d.pop("affected", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        fixed = d.pop("fixed", UNSET)

        summary_ja = d.pop("summary_ja", UNSET)

        title_ja = d.pop("title_ja", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_yamaha = cls(
            affected=affected,
            cve=cve,
            date_added=date_added,
            fixed=fixed,
            summary_ja=summary_ja,
            title_ja=title_ja,
            updated_at=updated_at,
            url=url,
        )

        advisory_yamaha.additional_properties = d
        return advisory_yamaha

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
