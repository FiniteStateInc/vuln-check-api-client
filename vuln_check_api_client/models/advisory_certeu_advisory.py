from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryCERTEUAdvisory")


@_attrs_define
class AdvisoryCERTEUAdvisory:
    """
    Attributes:
        advisory_id (Union[Unset, str]):
        affected_products (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        history (Union[Unset, list[str]]):
        link (Union[Unset, str]):
        recommendations (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        technical_details (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    advisory_id: Union[Unset, str] = UNSET
    affected_products: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    history: Union[Unset, list[str]] = UNSET
    link: Union[Unset, str] = UNSET
    recommendations: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    technical_details: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory_id = self.advisory_id

        affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        history: Union[Unset, list[str]] = UNSET
        if not isinstance(self.history, Unset):
            history = self.history

        link = self.link

        recommendations = self.recommendations

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary = self.summary

        technical_details = self.technical_details

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory_id is not UNSET:
            field_dict["advisoryId"] = advisory_id
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if history is not UNSET:
            field_dict["history"] = history
        if link is not UNSET:
            field_dict["link"] = link
        if recommendations is not UNSET:
            field_dict["recommendations"] = recommendations
        if references is not UNSET:
            field_dict["references"] = references
        if summary is not UNSET:
            field_dict["summary"] = summary
        if technical_details is not UNSET:
            field_dict["technicalDetails"] = technical_details
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        advisory_id = d.pop("advisoryId", UNSET)

        affected_products = d.pop("affectedProducts", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        history = cast(list[str], d.pop("history", UNSET))

        link = d.pop("link", UNSET)

        recommendations = d.pop("recommendations", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary = d.pop("summary", UNSET)

        technical_details = d.pop("technicalDetails", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_certeu_advisory = cls(
            advisory_id=advisory_id,
            affected_products=affected_products,
            cve=cve,
            date_added=date_added,
            history=history,
            link=link,
            recommendations=recommendations,
            references=references,
            summary=summary,
            technical_details=technical_details,
            title=title,
            updated_at=updated_at,
        )

        advisory_certeu_advisory.additional_properties = d
        return advisory_certeu_advisory

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
