from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryFortinetAdvisory")


@_attrs_define
class AdvisoryFortinetAdvisory:
    """
    Attributes:
        acknowledgement (Union[Unset, str]):
        affected_products (Union[Unset, list[str]]):
        cve (Union[Unset, list[str]]):
        cvssv3 (Union[Unset, str]):
        date_added (Union[Unset, str]):
        irnumber (Union[Unset, str]):
        link (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        solutions (Union[Unset, list[str]]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    acknowledgement: Union[Unset, str] = UNSET
    affected_products: Union[Unset, list[str]] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvssv3: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    irnumber: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    solutions: Union[Unset, list[str]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledgement = self.acknowledgement

        affected_products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_products, Unset):
            affected_products = self.affected_products

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvssv3 = self.cvssv3

        date_added = self.date_added

        irnumber = self.irnumber

        link = self.link

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        solutions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.solutions, Unset):
            solutions = self.solutions

        summary = self.summary

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledgement is not UNSET:
            field_dict["acknowledgement"] = acknowledgement
        if affected_products is not UNSET:
            field_dict["affectedProducts"] = affected_products
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvssv3 is not UNSET:
            field_dict["cvssv3"] = cvssv3
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if irnumber is not UNSET:
            field_dict["irnumber"] = irnumber
        if link is not UNSET:
            field_dict["link"] = link
        if references is not UNSET:
            field_dict["references"] = references
        if solutions is not UNSET:
            field_dict["solutions"] = solutions
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledgement = d.pop("acknowledgement", UNSET)

        affected_products = cast(list[str], d.pop("affectedProducts", UNSET))

        cve = cast(list[str], d.pop("cve", UNSET))

        cvssv3 = d.pop("cvssv3", UNSET)

        date_added = d.pop("date_added", UNSET)

        irnumber = d.pop("irnumber", UNSET)

        link = d.pop("link", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        solutions = cast(list[str], d.pop("solutions", UNSET))

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        advisory_fortinet_advisory = cls(
            acknowledgement=acknowledgement,
            affected_products=affected_products,
            cve=cve,
            cvssv3=cvssv3,
            date_added=date_added,
            irnumber=irnumber,
            link=link,
            references=references,
            solutions=solutions,
            summary=summary,
            title=title,
        )

        advisory_fortinet_advisory.additional_properties = d
        return advisory_fortinet_advisory

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
