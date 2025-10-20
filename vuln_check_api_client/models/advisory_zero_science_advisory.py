from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryZeroScienceAdvisory")


@_attrs_define
class AdvisoryZeroScienceAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        affected_versions (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        impact (Union[Unset, str]):
        link (Union[Unset, str]):
        po_c (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        risk (Union[Unset, str]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        type_ (Union[Unset, str]):
        vendor (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    affected_versions: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    impact: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    po_c: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    risk: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        affected_versions = self.affected_versions

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        impact = self.impact

        link = self.link

        po_c = self.po_c

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        risk = self.risk

        summary = self.summary

        title = self.title

        type_ = self.type_

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisoryId"] = advisory_id
        if affected_versions is not UNSET:
            field_dict["affectedVersions"] = affected_versions
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if impact is not UNSET:
            field_dict["impact"] = impact
        if link is not UNSET:
            field_dict["link"] = link
        if po_c is not UNSET:
            field_dict["poC"] = po_c
        if references is not UNSET:
            field_dict["references"] = references
        if risk is not UNSET:
            field_dict["risk"] = risk
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("advisoryId", UNSET)

        affected_versions = d.pop("affectedVersions", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        impact = d.pop("impact", UNSET)

        link = d.pop("link", UNSET)

        po_c = d.pop("poC", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        risk = d.pop("risk", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        vendor = d.pop("vendor", UNSET)

        advisory_zero_science_advisory = cls(
            advisory_id=advisory_id,
            affected_versions=affected_versions,
            cve=cve,
            date_added=date_added,
            description=description,
            impact=impact,
            link=link,
            po_c=po_c,
            references=references,
            risk=risk,
            summary=summary,
            title=title,
            type_=type_,
            vendor=vendor,
        )

        advisory_zero_science_advisory.additional_properties = d
        return advisory_zero_science_advisory

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
