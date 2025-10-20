from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPalantir")


@_attrs_define
class AdvisoryPalantir:
    """
    Attributes:
        affected_products (Union[Unset, str]):
        background (Union[Unset, str]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        details (Union[Unset, str]):
        summary (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affected_products: Union[Unset, str] = UNSET
    background: Union[Unset, str] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_products = self.affected_products

        background = self.background

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        details = self.details

        summary = self.summary

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_products is not UNSET:
            field_dict["affected_products"] = affected_products
        if background is not UNSET:
            field_dict["background"] = background
        if bulletin_id is not UNSET:
            field_dict["bulletin_id"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if details is not UNSET:
            field_dict["details"] = details
        if summary is not UNSET:
            field_dict["summary"] = summary
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_products = d.pop("affected_products", UNSET)

        background = d.pop("background", UNSET)

        bulletin_id = d.pop("bulletin_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        details = d.pop("details", UNSET)

        summary = d.pop("summary", UNSET)

        url = d.pop("url", UNSET)

        advisory_palantir = cls(
            affected_products=affected_products,
            background=background,
            bulletin_id=bulletin_id,
            cve=cve,
            date_added=date_added,
            details=details,
            summary=summary,
            url=url,
        )

        advisory_palantir.additional_properties = d
        return advisory_palantir

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
