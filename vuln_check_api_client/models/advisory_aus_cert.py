from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAusCert")


@_attrs_define
class AdvisoryAusCert:
    """
    Attributes:
        body (Union[Unset, str]):
        bulletin_id (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvss (Union[Unset, str]):
        date_added (Union[Unset, str]):
        link (Union[Unset, str]):
        operating_system (Union[Unset, str]):
        product (Union[Unset, str]):
        publisher (Union[Unset, str]):
        resolution (Union[Unset, str]):
    """

    body: Union[Unset, str] = UNSET
    bulletin_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    operating_system: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    publisher: Union[Unset, str] = UNSET
    resolution: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        bulletin_id = self.bulletin_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss = self.cvss

        date_added = self.date_added

        link = self.link

        operating_system = self.operating_system

        product = self.product

        publisher = self.publisher

        resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if bulletin_id is not UNSET:
            field_dict["bulletinId"] = bulletin_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if link is not UNSET:
            field_dict["link"] = link
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if product is not UNSET:
            field_dict["product"] = product
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        bulletin_id = d.pop("bulletinId", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvss = d.pop("cvss", UNSET)

        date_added = d.pop("date_added", UNSET)

        link = d.pop("link", UNSET)

        operating_system = d.pop("operatingSystem", UNSET)

        product = d.pop("product", UNSET)

        publisher = d.pop("publisher", UNSET)

        resolution = d.pop("resolution", UNSET)

        advisory_aus_cert = cls(
            body=body,
            bulletin_id=bulletin_id,
            cve=cve,
            cvss=cvss,
            date_added=date_added,
            link=link,
            operating_system=operating_system,
            product=product,
            publisher=publisher,
            resolution=resolution,
        )

        advisory_aus_cert.additional_properties = d
        return advisory_aus_cert

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
