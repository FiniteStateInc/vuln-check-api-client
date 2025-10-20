from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBeldenAdvisory")


@_attrs_define
class AdvisoryBeldenAdvisory:
    """
    Attributes:
        belden_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cwe (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_last_updated (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    belden_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cwe: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_last_updated: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        belden_id = self.belden_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cwe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cwe, Unset):
            cwe = self.cwe

        date_added = self.date_added

        date_last_updated = self.date_last_updated

        title = self.title

        updated_at = self.updated_at

        url = self.url

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if belden_id is not UNSET:
            field_dict["belden_id"] = belden_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_last_updated is not UNSET:
            field_dict["date_last_updated"] = date_last_updated
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        belden_id = d.pop("belden_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cwe = cast(list[str], d.pop("cwe", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_last_updated = d.pop("date_last_updated", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        advisory_belden_advisory = cls(
            belden_id=belden_id,
            cve=cve,
            cwe=cwe,
            date_added=date_added,
            date_last_updated=date_last_updated,
            title=title,
            updated_at=updated_at,
            url=url,
            version=version,
        )

        advisory_belden_advisory.additional_properties = d
        return advisory_belden_advisory

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
