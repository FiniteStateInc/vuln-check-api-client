from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisorySSDAdvisory")


@_attrs_define
class AdvisorySSDAdvisory:
    """
    Attributes:
        analysis (Union[Unset, str]):
        credit (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        link (Union[Unset, str]):
        poc (Union[Unset, str]): contains actual poc code
        published (Union[Unset, str]):
        response_ref (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    analysis: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    poc: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    response_ref: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis = self.analysis

        credit = self.credit

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        link = self.link

        poc = self.poc

        published = self.published

        response_ref = self.response_ref

        summary = self.summary

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if credit is not UNSET:
            field_dict["credit"] = credit
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if link is not UNSET:
            field_dict["link"] = link
        if poc is not UNSET:
            field_dict["poc"] = poc
        if published is not UNSET:
            field_dict["published"] = published
        if response_ref is not UNSET:
            field_dict["response_ref"] = response_ref
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        analysis = d.pop("analysis", UNSET)

        credit = d.pop("credit", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        link = d.pop("link", UNSET)

        poc = d.pop("poc", UNSET)

        published = d.pop("published", UNSET)

        response_ref = d.pop("response_ref", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        advisory_ssd_advisory = cls(
            analysis=analysis,
            credit=credit,
            cve=cve,
            date_added=date_added,
            link=link,
            poc=poc,
            published=published,
            response_ref=response_ref,
            summary=summary,
            title=title,
        )

        advisory_ssd_advisory.additional_properties = d
        return advisory_ssd_advisory

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
