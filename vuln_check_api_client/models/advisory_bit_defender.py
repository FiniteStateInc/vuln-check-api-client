from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryBitDefender")


@_attrs_define
class AdvisoryBitDefender:
    """
    Attributes:
        additional_details (Union[Unset, str]):
        affected_products (Union[Unset, str]):
        affected_vendors (Union[Unset, str]):
        credit (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        details (Union[Unset, str]):
        timeline (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    additional_details: Union[Unset, str] = UNSET
    affected_products: Union[Unset, str] = UNSET
    affected_vendors: Union[Unset, str] = UNSET
    credit: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    timeline: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_details = self.additional_details

        affected_products = self.affected_products

        affected_vendors = self.affected_vendors

        credit = self.credit

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        details = self.details

        timeline = self.timeline

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_details is not UNSET:
            field_dict["additional_details"] = additional_details
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if affected_vendors is not UNSET:
            field_dict["affected_vendors"] = affected_vendors
        if credit is not UNSET:
            field_dict["credit"] = credit
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details is not UNSET:
            field_dict["details"] = details
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_details = d.pop("additional_details", UNSET)

        affected_products = d.pop("affected_products", UNSET)

        affected_vendors = d.pop("affected_vendors", UNSET)

        credit = d.pop("credit", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        details = d.pop("details", UNSET)

        timeline = d.pop("timeline", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_bit_defender = cls(
            additional_details=additional_details,
            affected_products=affected_products,
            affected_vendors=affected_vendors,
            credit=credit,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            details=details,
            timeline=timeline,
            title=title,
            url=url,
        )

        advisory_bit_defender.additional_properties = d
        return advisory_bit_defender

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
