from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHKCert")


@_attrs_define
class AdvisoryHKCert:
    """
    Attributes:
        affected (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        impact (Union[Unset, str]):
        link (Union[Unset, str]):
        related_links (Union[Unset, list[str]]):
        risk (Union[Unset, str]):
        solutions (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    affected: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    related_links: Union[Unset, list[str]] = UNSET
    risk: Union[Unset, str] = UNSET
    solutions: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = self.affected

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        impact = self.impact

        link = self.link

        related_links: Union[Unset, list[str]] = UNSET
        if not isinstance(self.related_links, Unset):
            related_links = self.related_links

        risk = self.risk

        solutions = self.solutions

        summary = self.summary

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if impact is not UNSET:
            field_dict["impact"] = impact
        if link is not UNSET:
            field_dict["link"] = link
        if related_links is not UNSET:
            field_dict["relatedLinks"] = related_links
        if risk is not UNSET:
            field_dict["risk"] = risk
        if solutions is not UNSET:
            field_dict["solutions"] = solutions
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = cast(list[str], d.pop("affected", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        impact = d.pop("impact", UNSET)

        link = d.pop("link", UNSET)

        related_links = cast(list[str], d.pop("relatedLinks", UNSET))

        risk = d.pop("risk", UNSET)

        solutions = d.pop("solutions", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_hk_cert = cls(
            affected=affected,
            cve=cve,
            date_added=date_added,
            impact=impact,
            link=link,
            related_links=related_links,
            risk=risk,
            solutions=solutions,
            summary=summary,
            title=title,
            type_=type_,
        )

        advisory_hk_cert.additional_properties = d
        return advisory_hk_cert

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
