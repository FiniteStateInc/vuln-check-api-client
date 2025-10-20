from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAdvisoryRecord")


@_attrs_define
class AdvisoryAdvisoryRecord:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        external_id (Union[Unset, list[str]]):
        lang (Union[Unset, str]):
        name (Union[Unset, str]):
        refsource (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    external_id: Union[Unset, list[str]] = UNSET
    lang: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    refsource: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        external_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.external_id, Unset):
            external_id = self.external_id

        lang = self.lang

        name = self.name

        refsource = self.refsource

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if lang is not UNSET:
            field_dict["lang"] = lang
        if name is not UNSET:
            field_dict["name"] = name
        if refsource is not UNSET:
            field_dict["refsource"] = refsource
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        external_id = cast(list[str], d.pop("external_id", UNSET))

        lang = d.pop("lang", UNSET)

        name = d.pop("name", UNSET)

        refsource = d.pop("refsource", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        url = d.pop("url", UNSET)

        advisory_advisory_record = cls(
            cve=cve,
            date_added=date_added,
            external_id=external_id,
            lang=lang,
            name=name,
            refsource=refsource,
            tags=tags,
            url=url,
        )

        advisory_advisory_record.additional_properties = d
        return advisory_advisory_record

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
