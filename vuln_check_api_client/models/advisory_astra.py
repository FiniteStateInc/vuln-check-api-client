from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAstra")


@_attrs_define
class AdvisoryAstra:
    """
    Attributes:
        bdu (Union[Unset, list[str]]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary_ru (Union[Unset, str]):
        title_ru (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    bdu: Union[Unset, list[str]] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary_ru: Union[Unset, str] = UNSET
    title_ru: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bdu: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bdu, Unset):
            bdu = self.bdu

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary_ru = self.summary_ru

        title_ru = self.title_ru

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bdu is not UNSET:
            field_dict["bdu"] = bdu
        if bulletin_id is not UNSET:
            field_dict["bulletin_id"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if references is not UNSET:
            field_dict["references"] = references
        if summary_ru is not UNSET:
            field_dict["summary_ru"] = summary_ru
        if title_ru is not UNSET:
            field_dict["title_ru"] = title_ru
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bdu = cast(list[str], d.pop("bdu", UNSET))

        bulletin_id = d.pop("bulletin_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary_ru = d.pop("summary_ru", UNSET)

        title_ru = d.pop("title_ru", UNSET)

        url = d.pop("url", UNSET)

        advisory_astra = cls(
            bdu=bdu,
            bulletin_id=bulletin_id,
            cve=cve,
            date_added=date_added,
            references=references,
            summary_ru=summary_ru,
            title_ru=title_ru,
            url=url,
        )

        advisory_astra.additional_properties = d
        return advisory_astra

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
