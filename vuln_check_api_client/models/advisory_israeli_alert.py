from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryIsraeliAlert")


@_attrs_define
class AdvisoryIsraeliAlert:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        details_he (Union[Unset, str]):
        handling_he (Union[Unset, str]):
        link (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary_he (Union[Unset, str]):
        title_he (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    details_he: Union[Unset, str] = UNSET
    handling_he: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary_he: Union[Unset, str] = UNSET
    title_he: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        details_he = self.details_he

        handling_he = self.handling_he

        link = self.link

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary_he = self.summary_he

        title_he = self.title_he

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details_he is not UNSET:
            field_dict["details_he"] = details_he
        if handling_he is not UNSET:
            field_dict["handling_he"] = handling_he
        if link is not UNSET:
            field_dict["link"] = link
        if references is not UNSET:
            field_dict["references"] = references
        if summary_he is not UNSET:
            field_dict["summary_he"] = summary_he
        if title_he is not UNSET:
            field_dict["title_he"] = title_he

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        details_he = d.pop("details_he", UNSET)

        handling_he = d.pop("handling_he", UNSET)

        link = d.pop("link", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary_he = d.pop("summary_he", UNSET)

        title_he = d.pop("title_he", UNSET)

        advisory_israeli_alert = cls(
            cve=cve,
            date_added=date_added,
            details_he=details_he,
            handling_he=handling_he,
            link=link,
            references=references,
            summary_he=summary_he,
            title_he=title_he,
        )

        advisory_israeli_alert.additional_properties = d
        return advisory_israeli_alert

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
